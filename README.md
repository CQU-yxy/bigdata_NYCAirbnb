# bigdata_NYCAirbnb
这是一个基于纽约Airbnb房源信息的数据可视化和房价预测项目
运行本项目所需要的环境为：

python==3.7

Hadoop+Spark完全分布式环境

与数据读取相关的第三方库：pandas，numpy

与数据可视化相关的第三方库：matplotlib，seaborn，missingno，pycharts，wordcloud

与机器学习模型相关的第三方库：pyspark.mllib，jieba

## 数据预处理

预处理文件为AB_analysis.py，把python文件与数据集AB_NYC_2019.csv放在同一目录下直接运行即可，可以把文件上传至服务器（但要保证在同一目录下），在目录下打开终端，输入python AB_analysis.py即可，但因为不涉及分布式环境，更推荐在本地运行。

其中后面的图如需显示需自行在相关代码后添加plt.show()即可。

## 数据可视化

可视化文件为Abdata_vis.py，把python文件与数据集AB_NYC_2019.csv放在同一目录下直接运行即可，可以把文件上传至服务器（但要保证在同一目录下），在目录下打开终端，输入python Abdata_vis.py即可，但因为不涉及分布式环境，更推荐在本地运行。

其中后面的图如需显示需自行在相关代码后添加plt.show()即可。

## 词云可视化

首先到hadoop目录下新建文件夹proj，proj文件夹下再包括src文件夹和results文件夹，推荐使用vnc工具更方便。

然后使用filezilla将需要的文件上传到src目录下，一共四个文件，事先整理的街区名字AB_data.txt，英语常见停止词stop_words.py，两个python文件。

首先要启动分布式集群：

//启动hadoop集群

cd /usr/local/hadoop
sbin/start-all.sh

//启动spark集群

cd /usr/local/spark
sbin/start-master.sh
sbin/start-slaves.sh

输入bin/spark-submit /home/hadoop/proj/WordCount.py即可

## 算法实现

首先要获取处理后的数据集AB_data.csv，我们在数据预处理文件AB_analysis.py中第76行输出了处理后的csv文件。

先把文件上传到服务器上然后上传至hdfs上，具体操作如下

先输入.bin/hadoop fs -mkdir -p /proj 创建文件夹

再把.bin/hadoop fs -put /home/hadoop/AB_data.csv /proj 上传到hdfs上

然后提交代码即可：

cd /usr/local/spark bin/spark-submit --master spark://master:7077 --py-files /home/hadoop/big_data.py --executor-memory 1G 

注：若服务器内存不够可对运行内存做适当调整，我们运行时使用的是512M
