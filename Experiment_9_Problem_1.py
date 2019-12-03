import pandas as pd
data1 = {'Student':['Ice Bear','Panda','Grizly'],'Math':[80,95,79]}
data2 = {'Student':['Ice Bear','Panda','Grizly'],'Electronics':[85,81,83]}
data3 = {'Student':['Ice Bear','Panda','Grizly'],'GEAS':[90,79,93]}
data4 = {'Student':['Ice Bear','Panda','Grizly'],'ESAT':[93,89,88]}
df1 = pd.DataFrame(data1,columns=['Student','Math'])
df2 = pd.DataFrame(data2,columns=['Student','Electronics'])
df3 = pd.DataFrame(data3,columns=['Student','GEAS'])
df4 = pd.DataFrame(data4,columns=['Student','ESAT'])
df_merge = pd.merge(df1,df2, how='right',on='Student')
df_merge1 = pd.merge(df_merge,df3, how='right',on='Student')
df_merge2 = pd.merge(df_merge1,df4, how='right',on='Student')
print(df1)
print(df2)
print(df3)
print(df4)
print(df_merge2)

