import numpy as np
from scipy.stats import norm
import scipy.stats
from sklearn.decomposition import PCA
import operator
import matplotlib as mpl
mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False
import matplotlib.pyplot as plt
from PyQt5.QtCore import *


def text_save1(filename, data):
    file = open(filename, 'w+')
    for item in data:
        file.write("\t".join(list(map(str, item))) + "\n")
    file.close()


def text_save(filename, data):
    file = open(filename, 'w+')
    for i in range(len(data)):
        s = str(data[i]).replace('[', '').replace(']', '')
        s = s.replace("'", '').replace(',', '') + '\n'
        file.write(s)
    file.close()


def trainPCA(refData, pcacomp=3):
    tData = refData.T
    pca = PCA(n_components=pcacomp)
    pca.fit(tData)
    PCA(copy=True, whiten=False)
    transformed = pca.transform(tData)
    inversed = pca.inverse_transform(transformed)
    corrected = tData / inversed
    return corrected.T, pca


def applyPCA(sampleData, mean, components):
    pca = PCA(n_components=components.shape[0])
    pca.components_ = components
    pca.mean_ = mean
    transform = pca.transform(np.array([sampleData]))
    reconstructed = np.dot(transform, pca.components_) + pca.mean_
    reconstructed = reconstructed[0]
    return sampleData / reconstructed


def maxminnorm(array):
    maxcols = array.max(axis=0)
    mincols = array.min(axis=0)
    data_shape = array.shape
    data_rows = data_shape[0]
    data_cols = data_shape[1]
    t = np.empty((data_rows, data_cols))
    for i in range(data_cols):
        t[:, i] = (array[:, i] - mincols[i]) / (maxcols[i] - mincols[i])
    return t


def z_test(x, binmean, binstd):
    z = (x - binmean) / binstd
    pval = 2 * (1 - norm.cdf(abs(z)))
    return pval


def z_score(x, binmean, binstd):
    z = (x - binmean) / binstd
    return z


class DetectionCNV(QThread):
    cur = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.dealNpz()
        self.dealGene()

    def dealSearchRegion(self,region):
        chr=region[0]
        start=region[1]
        end=region[2]
        curChrRegions=self.chrExonRegion[chr]
        left=0
        right=len(curChrRegions)-1
        while left<right:
            mid=(left+right)//2
            if start < curChrRegions[mid][1]:
                right=mid
                if mid>0 and start > curChrRegions[mid-1][1]:
                    left=mid-1
                    break
            elif start > curChrRegions[mid][1]:
                left=mid
                if mid <= right and start < curChrRegions[mid+1][1]:
                    break
            else:
                left=mid
                break
        searchRegion=[]
        searchIdx=[]
        if curChrRegions[left][2] >= start:
            searchRegion.append(curChrRegions[left])
            searchIdx.append(left)
        for cur in range(left+1,len(curChrRegions)):
            if curChrRegions[cur][1] <= end:
                searchRegion.append(curChrRegions[cur])
                searchIdx.append(cur)
            else:
                break
        searchIdxStart=self.chromSum[chr]
        idx=[]
        region=[]
        flag=[]
        for cur in range(len(searchIdx)):
            realIdx = searchIdx[cur]+searchIdxStart
            if self.mask[realIdx]:
                if realIdx in self.gain_idx :
                    idx.append(realIdx)
                    region.append(searchRegion[cur])
                    flag.append(1)
                elif realIdx in self.loss_idx:
                    idx.append(realIdx)
                    region.append(searchRegion[cur])
                    flag.append(-1)



        curChrGene = self.geneChr[chr]
        left = 0
        right = len(curChrGene) - 1
        while left < right:
            mid = (left + right) // 2
            if start < curChrGene[mid][1]:
                right = mid
                if mid > 0 and start > curChrGene[mid - 1][1]:
                    left = mid - 1
                    break
            elif start > curChrGene[mid][1]:
                left = mid
                if mid <= right and start < curChrGene[mid + 1][1]:
                    break
            else:
                left = mid
                break
        geneRegion = []
        if curChrGene[left][2] >= start:
            geneRegion.append(curChrGene[left])
        for cur in range(left + 1, len(curChrGene)):
            if curChrGene[cur][1] <= end:
                geneRegion.append(curChrGene[cur])
            else:
                break





        x_data=[]
        y_refMean=[]
        y_refMedian = []
        y_test=[]
        x=np.arange(len(idx))
        bar_width = 0.35
        for cur in range(len(idx)):
            x_data.append(str(cur+1))
            y_refMean.append(self.refMean[idx[cur]])
            y_refMedian.append(self.refMedian[idx[cur]])
            y_test.append(self.testSample[idx[cur]])
        plt.bar(x, y_refMean,bar_width, label='ref外显子reads count均值',align="center", color='indianred', alpha=0.8)
        plt.bar(x+bar_width, y_test,bar_width, label='test样本外显子reads count',align="center", color='steelblue', alpha=0.8)
        plt.title("外显子reads count")
        # 为两条坐标轴设置名称
        plt.xlabel("外显子")
        plt.ylabel("reads count")
        plt.xticks(x + bar_width / 2, x_data)
        # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        plt.savefig("temp/refMean.png")
        plt.close()



        x_data = []
        x = np.arange(len(flag))
        for cur in range(len(flag)):
            x_data.append(str(cur + 1))
        plt.bar(x, flag, bar_width*2, label='外显子拷贝数变异', align="center", color='indianred', alpha=0.8)
        plt.title("外显子拷贝数变异")
        # 为两条坐标轴设置名称
        plt.xlabel("外显子")
        plt.ylabel("外显子拷贝数状态")
        plt.xticks(x, x_data)
        ax = plt.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        # ax.yaxis.set_ticks_position('left')
        ax.spines['bottom'].set_position(('data', 0))
        # ax.spines['left'].set_position(('data', 0))



        plt.yticks([1,0,-1], ["扩增","正常","删除"])
        # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
        plt.savefig("temp/exonCNV.png")
        plt.close()
        return region,geneRegion





    def dealGene(self):
        with open("file/geneUniq.txt") as f1:
            gene_region = f1.readlines()
        geneNum=len(gene_region)
        self.geneChr=[]
        pre="1"
        temp = []
        for i in range(geneNum):
            ones = gene_region[i].split()
            chr=ones[0]
            start=int(ones[1])
            end=int(ones[2])
            geneName=ones[3]
            if chr!=pre:
                self.geneChr.append(temp)
                temp=[]
            temp.append([chr, start, end,geneName])
            pre=chr
        self.geneChr.append(temp)




    def dealNpz(self):
        npzdata=np.load("file/COAD_10A_v2.npz")
        allData = npzdata['allData']
        chromBins = npzdata['chromBins']
        self.chromSum = [0]
        sum = 0
        for perBins in chromBins:
            sum += perBins
            self.chromSum.append(sum)
        del npzdata

        with open("file/v2hg38.bed") as f1:
            exome_region = f1.readlines()
        with open("file/gc_v2.txt") as f2:
            gc = f2.readlines()

        num = len(exome_region)
        exon_mask = [True] * num
        exon_region = []
        for i in range(num):
            ones = exome_region[i].split()
            chr = int(ones[0])
            exome_start = int(ones[1])
            exome_end = int(ones[2])
            temp = [chr, exome_start, exome_end]
            exon_region.append(temp)
            if exome_end - exome_start < 20:
                exon_mask[i] = False
                continue
            curExon_gc = float(gc[i])
            if curExon_gc < 0.1 or curExon_gc > 0.9:
                exon_mask[i] = False

        self.chrExonRegion = []
        for i in range(1, len(self.chromSum)):
            self.chrExonRegion.append(exon_region[self.chromSum[i - 1]:self.chromSum[i]])

        median = np.median(allData, axis=1)
        read_num_mask = median > 20
        mask = np.logical_and(exon_mask, read_num_mask)

        ref_maskedData = allData[mask, :]
        sumPerSample = np.sum(ref_maskedData, 0)
        medianSamples = np.median(sumPerSample)
        tmpdata = allData * 1.0 / sumPerSample * medianSamples
        tmp_std = np.std(tmpdata, axis=1)
        tmp_mean = np.mean(tmpdata, axis=1)
        for i in range(allData.shape[0]):
            if tmp_mean[i] == 0:
                tmp_mean[i] = 1
        cv_array = tmp_std / tmp_mean
        del tmpdata

        cv_mask = cv_array < 1
        mask = np.logical_and(mask, cv_mask)
        ref_maskedData = allData[mask, :]
        sumPerSample = np.sum(ref_maskedData, 0)
        medianSamples = np.median(sumPerSample)
        ref_maskedData = ref_maskedData * 1.0 / sumPerSample * medianSamples

        npzdata_test = np.load("file/6137_01A_v2hg38.npz")
        testsamplesData = npzdata_test['allData']
        del npzdata_test

        testsamplesData = testsamplesData[mask, :]
        testSumReads = np.sum(testsamplesData, 0)
        testsamplesData = testsamplesData * 1.0 / testSumReads * medianSamples
        refsamples_num = ref_maskedData.shape[1]
        testsamples_num = testsamplesData.shape[1]
        for i_testsample in range(testsamples_num):
            testData = testsamplesData[:, i_testsample]
            q = np.array(testData)
            js = []
            for i in range(refsamples_num):
                p = np.asarray(ref_maskedData[:, i])
                M = (p + q) / 2
                js2 = 0.5 * scipy.stats.entropy(p, M) + 0.5 * scipy.stats.entropy(q, M)
                js.append([js2, i])
            js.sort(key=operator.itemgetter(0))
            samples_mask = [False] * refsamples_num
            for i in range(150):
                samples_mask[js[i][1]] = True
            maskedData = ref_maskedData[:, samples_mask]

            self.refMean=[]
            self.refMedian = []
            maskedData_median = np.median(maskedData, axis=1)
            maskedData_mean = np.mean(maskedData, axis=1)
            self.testSample=[]
            self.mask = mask
            j=0
            for i in range(sum):
                if mask[i]:
                    self.refMean.append(maskedData_mean[j])
                    self.refMedian.append(maskedData_median[j])
                    self.testSample.append(testData[j])
                    j+=1
                else:
                    self.refMean.append(0)
                    self.refMedian.append(0)
                    self.testSample.append(0)


            refData, pca = trainPCA(maskedData)
            ref_std = np.std(refData, axis=1)
            ref_mean = np.mean(refData, axis=1)
            testData_corrected = applyPCA(testData, pca.mean_, pca.components_)





            z_scores = []
            j = 0
            for i in range(sum):
                if mask[i] == True:
                    z = z_score(testData_corrected[j], ref_mean[j], ref_std[j])
                    z_scores.append(z)
                    j += 1
                else:
                    z_scores.append(0)

            z_threshold = 3.0
            chr_idx = 1
            i = 0
            gain = []
            loss = []
            while i < sum:
                if i >= self.chromSum[chr_idx]:
                    chr_idx += 1
                if mask[i] == True and abs(z_scores[i]) > z_threshold:
                    j = i + 1
                    k = i
                    z_sum = z_scores[i]
                    z_tmp = [z_scores[i]]
                    z_num = 1
                    contrary = 0
                    fail = 0
                    while (j < self.chromSum[chr_idx]):
                        if z_scores[i] * z_scores[j] != 0:
                            z_sum += z_scores[j]
                            z_tmp.append(z_scores[j])
                            z_num += 1
                            z_cur = z_sum / z_num
                            if abs(z_cur) > z_threshold and abs(z_scores[j]) > z_threshold and abs(
                                    np.median(z_tmp)) > z_threshold:
                                k = j
                                fail = 0
                                contrary = 0
                            elif abs(z_scores[j]) <= z_threshold:
                                fail += 1
                            elif z_scores[i] * z_scores[j] < 0:
                                contrary += 1
                        if fail > 5 or contrary > 1:
                            break
                        j += 1
                    if k - i >= 2:
                        if z_scores[i] > 0:
                            gain.append([i, k])
                        else:
                            loss.append([i, k])
                        i = k
                i += 1

            dup_cnv = []
            if len(gain) > 0:
                dup_cnv.append(gain[0])
                for i in range(1, len(gain)):
                    start = dup_cnv[len(dup_cnv) - 1][1] + 1
                    end = gain[i][0]
                    if exon_region[start - 1][0] == exon_region[end][0]:
                        tmp = np.array(z_scores[start:end])
                        p = np.sum(tmp > 1)
                        n = np.sum(tmp < -3)
                        zero = np.sum(tmp == 0)
                        if (end - start - zero) <= 0 or (p / (end - start - zero) > 0.66 and n <= p // 3):
                            dup_cnv[len(dup_cnv) - 1][1] = gain[i][1]
                        else:
                            dup_cnv.append(gain[i])
                    else:
                        dup_cnv.append(gain[i])

            del_cnv = []
            if len(loss) > 0:
                del_cnv.append(loss[0])
                for i in range(1, len(loss)):
                    start = del_cnv[len(del_cnv) - 1][1] + 1
                    end = loss[i][0]
                    if exon_region[start - 1][0] == exon_region[end][0]:
                        tmp = np.array(z_scores[start:end])
                        p = np.sum(tmp > 3)
                        n = np.sum(tmp < -1)
                        zero = np.sum(tmp == 0)
                        if (end - start - zero) <= 0 or (n / (end - start - zero) > 0.66 and p <= n // 3):
                            del_cnv[len(del_cnv) - 1][1] = loss[i][1]
                        else:
                            del_cnv.append(loss[i])
                    else:
                        del_cnv.append(loss[i])

            self.gain_idx = set()
            self.loss_idx = set()
            for per in dup_cnv:
                for i in range(per[0],per[1]+1):
                    self.gain_idx.add(i)
            for per in del_cnv:
                for i in range(per[0],per[1]+1):
                    self.loss_idx.add(i)




