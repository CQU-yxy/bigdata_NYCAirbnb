from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.evaluation import RegressionMetrics
from pyspark.mllib.regression import LinearRegressionWithSGD
from pyspark.mllib.tree import GradientBoostedTrees, GradientBoostedTreesModel

sc = SparkContext("local")
spark = SparkSession(sc)

# 读取文本文件， 创建为DataFrame 结构
row_df = spark.read.csv(r"hdfs://master:9000/proj/AB_data.csv",header=True,inferSchema=True)
row_df.count()
# 7395



train_df, test_df = row_df.randomSplit([0.7, 0.3])
print(test_df)

labelpoint_train = train_df.rdd.map(lambda row:LabeledPoint(row[-1], row[:-1]))

labelpoint_test = test_df.rdd.map(lambda row:LabeledPoint(row[-1], row[:-1]))



from pyspark.mllib.tree import RandomForest
model = RandomForest.trainRegressor(labelpoint_train, {}, 2, seed=42)

#test_x=labelpoint_test.map(lambda lp: lp.features)
x=[2,40.75362,-73.98377,1,300,1,100]
predictions=model.predict(x)
print('the house is located in Manhattan')
print('the latitude and longitude of house is (40.75362,-73.98377)')
print('the type of house is entire home/apt')
print('the house is available in 300days')
print('the minimum_nights you need to stay is 1')
print('the views of the house is 200')
print(type(predictions))
print('the prediction of the Randomforest is',predictions)

model3=GradientBoostedTrees.trainRegressor(labelpoint_train,categoricalFeaturesInfo={}, numIterations=3)
pred3=model3.predict(x)
print('the prediction of the GBDT is',pred3)
'''
predictionAndLabels = labelpoint_test.map(lambda lp: (float(model.predict(lp.features)), lp.label))

metrics = RegressionMetrics(predictionAndLabels)
precision = metrics.meanSquaredError

print(precision)
'''

