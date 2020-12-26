import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder
import seaborn as sns


df = pd.read_csv('AB_NYC_2019.csv')
df = df.drop(['id','name','host_name','last_review','reviews_per_month'],axis=1)
print(df.shape)
df['neighbourhood_group'].unique()

df = df.drop(['host_id','neighbourhood','calculated_host_listings_count'],axis=1)
print(df.columns)
print(df.info())

cols = ['room_type','neighbourhood_group']
end = LabelEncoder()
for col in cols:
    df[col] = end.fit_transform(df[col])
    mapping = dict(zip(end.classes_,end.transform(end.classes_)))
    print("column : ", col)
    print("Mapping is : ", mapping)

print(df.shape)
df.boxplot(rot=45)

print("Latitude")
print(30*'-')
print(df['latitude'].quantile(0.1))
print(df['latitude'].quantile(0.9))
print('\n')

print('Longitude')
print(30*'-')
print(df['longitude'].quantile(0.1))
print(df['longitude'].quantile(0.9))
print('\n')

print('Minimum Nights')
print(30*'-')
print(df['minimum_nights'].quantile(0.1))
print(df['minimum_nights'].quantile(0.9))
print('\n')


print("Number of reviews")
print(30*'-')
print(df['number_of_reviews'].quantile(0.1))
print(df['number_of_reviews'].quantile(0.9))
print('/n')

print('Price')
print(30*'-')
print(df['price'].quantile(0.1))
print(df['price'].quantile(0.9))

df['latitude'] = np.where(df['latitude']<40.66799,40.66799,df['latitude'])
df['latitude'] = np.where(df['latitude']>40.80489,40.80489,df['latitude'])

df['longitude'] = np.where(df['longitude']<-73.99669,-73.99669,df['longitude'])
df['longitude'] = np.where(df['longitude']> -73.90781,-73.90781,df['longitude'])

df['minimum_nights'] = np.where(df['minimum_nights'] < 1.0,1.0,df['minimum_nights'])
df['minimum_nights'] = np.where(df['minimum_nights'] > 28.0,28.0,df['minimum_nights'])

df['number_of_reviews'] = np.where(df['number_of_reviews'] < 1.0 , 1.0 , df['number_of_reviews'])
df['number_of_reviews'] = np.where(df['number_of_reviews'] > 70.0 , 70.0 , df['number_of_reviews'])

df['price'] = np.where(df['price'] < 49.0 , 49.0 , df['price'])
df['price'] = np.where(df['price'] > 269.0 , 269.0 , df['price'])

print(df.shape)

#df.to_csv('AB_data.csv')

#打印筛选后特征的箱线图
df.boxplot(rot=45)
#plt.show()

#打印热力矩阵
sns.heatmap(df.corr(),annot=True)
#plt.show()

#打印minimum_nights对应的分布图
fig,ax=plt.subplots(figsize=(16,8))
sns.distplot(df['minimum_nights'],kde=False,rug=True)
ax.set_title('Counts of minimum nights',fontsize=16)
ax.tick_params(labelsize=13)
ax.set_xlabel('minimum nights', fontsize=15)
ax.set_ylabel('Sample size statistics',fontsize=15)