import pandas as pd
data = {'Box':['Box 1','Box 1','Box 1','Box 2','Box 2','Box 2'], 'Dimension':['Length','Width','Height','Length','Width','Height'], 'Values':[6,4,2,5,3,4]}
df = pd.DataFrame(data, columns=['Box','Dimension','Values'])
print(df)
tidy = df.pivot(index='Box', columns='Dimension', values='Values')
print(tidy)
tidy['Volume'] = tidy['Height']*tidy['Length']*tidy['Width']
print(tidy)
