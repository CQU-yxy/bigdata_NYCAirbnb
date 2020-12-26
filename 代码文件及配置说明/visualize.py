#-*- coding:utf-8 -*-


import os
from wordcloud import WordCloud
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts import options as opts
from pyecharts.charts import Pie

SAVAPATH = '/home/hadoop/proj/results/'

class visualize:

    def rdd2dic(self,resRdd,topK):


        resDic = resRdd.collectAsMap()
        # 截取字典前K个
        K = 60 #自己指定一个值
        num=0
        wordDick = {}
        for key, value in resDic.items():
            # 完成循环截取
            num=num+1
            wordDick[key]=value
            if num>K:
                break

        return wordDick

    def drawWorcCloud(self, wordDic):
        """
        根据词频字典，进行词云可视化
        :param wordDic: 词频统计字典
        :return:
        """
        # 生成词云
        wc = WordCloud(font_path='/usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
                       background_color='white',
                       max_words=2000,
                       width=1920, height=1080,
                       margin=5)
        wc.generate_from_frequencies(wordDic)
        # 保存结果
        wc.to_file(os.path.join(SAVAPATH, '词云可视化2.png'))
        

