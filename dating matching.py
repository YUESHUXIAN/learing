from numpy import *
import operator

# 3. 构建 KNN 分类器
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()

    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# 4. 读取数据
def file2matrix(filename):
    fr = open(filename, 'r', encoding='utf-8')
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0

    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

# 5. 数据预处理（归一化）
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals

# 6. 测试分类器性能
def datingClassTest():
    TestRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * TestRatio)
    errorCount = 0.0

    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:,:], datingLabels[numTestVecs:], 3)
        if classifierResult != datingLabels[i]:
            errorCount += 1.0
    print(f"分类器处理约会数据集的错误率是: {errorCount / float(numTestVecs):f}")
    print(f"分类错误的测试样本总数是: {errorCount}")

# 7. 分类器应用：约会对象筛选
def classifyPerson():
    resultList = ['一点也不喜欢', '有点喜欢', '比较喜欢']
    print("===请输入约会对象的信息 ===")
    percentTats = float(input("玩游戏、看视频消耗时间百分比："))
    ffMiles = float(input("每年飞行的里程数："))
    iceCream = float(input("每周消费冰淇淋的公升数："))

    datingDataMat, datingLabels = file2matrix('datingSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals)/ranges, normMat, datingLabels, 3)
    print(f"\n你对约会对象可能的喜欢程度：{resultList[classifierResult - 1]}")


print("---- 测试分类器性能 ----")
datingClassTest()

print("\n---- 分类器应用 ----")
classifyPerson()
