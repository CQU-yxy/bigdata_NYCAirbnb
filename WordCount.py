#-*- coding:utf-8 -*-

from pyspark import SparkConf, SparkContext
from visualize import visualize
import jieba

SRCPATH = '/home/hadoop/proj/src/'


conf = SparkConf().setAppName("proj").setMaster("local")
sc = SparkContext(conf=conf)

def getStopWords(stopWords_filePath):
    stopwords = [line.strip() for line in open(stopWords_filePath, 'r', encoding='utf-8').readlines()]
    return stopwords

def jiebaCut(filePath):

    # 读取answers.txt
    answersRdd = sc.textFile(filePath) # answersRdd每一个元素对应answers.txt每一行


    str = answersRdd.reduce(lambda x,y:x+y)

    # jieba分词
    words_list = jieba.lcut(str)
    return words_list

def wordcount(isvisualize=False):
    """
    对所有答案进行
    :param visualize: 是否进行可视化
    :return: 将序排序结果RDD
    """
    # 读取停用词表
    stopwords = getStopWords(SRCPATH + 'stop_words.txt')

    # 结巴分词
    words_list = jiebaCut("file://" + SRCPATH + "AB_data.txt")

    # 词频统计
    wordsRdd = sc.parallelize(words_list)

    resRdd = wordsRdd.filter(lambda word: len(word)!=1) \
                     .filter(lambda word: word not in stopwords)\
                     .map(lambda word: (word,1)) \
                     .reduceByKey(lambda a, b: a+b) \
                     .sortBy(ascending=False, numPartitions=None, keyfunc=lambda x:x[1]) \

    

    # 可视化展示
    if isvisualize:
        v = visualize()
        # 词云可视化
        wwDic = v.rdd2dic(resRdd,50)
        v.drawWorcCloud(wwDic)
    return  resRdd

if __name__ == '__main__':

    resRdd = wordcount(isvisualize=True)
    print(resRdd.take(10))  


