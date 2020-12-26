import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import missingno as msno
import seaborn as sns

#打印数据信息
df = pd.read_csv('AB_NYC_2019.csv')
print(df.shape)
print(df.info())

#房主id排名前十五
host = df['neighbourhood_group'].value_counts().head(5)
fig_1 = host.plot(kind='bar')
fig_1.set_title("Top 5 neighbourhood_group in NYC")
fig_1.set_xlabel('neighbourhood_group')
fig_1.set_ylabel('Count of Listing')
fig_1.set_xticklabels(fig_1.get_xticklabels(),rotation=45)
plt.show()

#打印散点图阵
sns.pairplot(df, height=3, diag_kind="hist")

#各区拥有房源数量可视化
sns.set_context('talk')
ax=sns.barplot(x = df['neighbourhood_group'],y = df['price'],ci=None)
plt.xlabel("Neighbourhood_Group",color='r')
plt.ylabel("Price($)",color='g')
plt.title("Prices in Major Region",color='magenta',size=15)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x()+0.30, p.get_height()+1), va='bottom',
                    color= 'black')

#缺失值可视化
msno.matrix(df)
plt.show()

#不同房间类型对应的平均价格
sns.set_context('poster')
ax = sns.barplot(df['room_type'],df['price'],ci=None)
plt.xlabel("Room Types",color='r')
plt.ylabel("Price($)",color='r')
plt.title("Prices for Each RoomType",color='magenta',size=15)

for p in ax.patches:
    ax.annotate(int(p.get_height()), (p.get_x()+0.30, p.get_height()-0.05), va='bottom',
                    color= 'black')


#纽约各区与房价间的关系的小提琴图
sub_1=df[df.price < 500]
#using violinplot to showcase density and distribtuion of prices
viz_2=sns.violinplot(data=sub_1, x='neighbourhood_group', y='price')
viz_2.set_title('Density and distribution of prices for each neighberhood_group')

#经纬度与房价的关系
viz_3=sub_1.plot(kind='scatter', x='longitude', y='latitude', label='availability_365', c='price',
                  cmap=plt.get_cmap('jet'), colorbar=True, alpha=0.4, figsize=(10,8))
viz_3.legend()