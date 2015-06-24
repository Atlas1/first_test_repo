# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>
import pandas as pd
pd.__version_
pd.__version__
data = [1,2,3,4,5]
type(data)
s = pd.Series(data)
s
s.index
import numpy as np
lis =  [1,3,5,7]
lis = np.array( [1,3,5,7])
lis
s.index
type(s.index)
s= pd.Series(data, index = ['a', 'b', 'c', 'd', 'd'])
s
s['d']
s['d']
s[4]
s['d'][0]
type(s['d'][0])
s[[4]]
int(s['d'][0])
s['d'][0].int
s['d'][0].asint
s.index = [1,2,3,4,5]
s
s[[3]]
s[[4]]
data
data = dict({'a':1, 'b':2, 'c':3})
data
s = pd.Series(data)
s
type(s)
type(data)
s = pd.Series(np.random.uniform(size=10))
s
s*5
np.exp(s)
s.apply(np.log)
s.apply(sum)
s = np.exp(s)
s
s.mean()
s.applu(np.mean)
s.applu(mean)
s.plot()
s.plot
s.plot()
import matplotlib al mpl
import matplotlib at mpl
import matplotlib as mpl
s.plot()
s
plt.show()
mpl.show()
import matplotlib at plt
import matplotlib as plt
s
s.plot()
mpl.Show()
mpl.show()
s.show()
clear()
s1 = pd.Series([1,2,3,4,5], index = list('edcbh'))
data = {'one': s1**s1, 'two':s1+1}
data
df = pd.DataFrame(data)
df
df.columns
df.index
df.columns = ['First', 'Second']
df.index = [1,2,1,2,4]
df
df.index
df['three'] = pd.Series([1,2,3,4,5], index=list('edchn'))
df
df['three'] = pd.Series([1,2,3,4,5], index=list('edchn'))
df['three'] = pd.Series([1,2,3,4,5], index=[3,2,1,2,4])
df['three'] = pd.Series([1,2,3,4,5], index=[3,2,1,2])
df['three'] = pd.Series([1,2,3,4,5], index=[3,2,1,4,5])
df
data = np.random.randn(5,2)
df = pd.DataFrame(data, index = list('abcde'), columns=['One', 'Two'])
df
df.one
col = df.one
df.One
col = df.'One'
col = df.One
row = df.xs('b')
type(row)
row
df
df.ix[['a','b'], 'Two']
type(df.ix[['a','b'], 'Two']-)
type(df.ix[['a','b'], 'Two'])
type(df.ix[['a','b'],:])
df.ix[['a','b'],:]
df.ix[['a','b'],]
df.plot()
matplotlib.show()
matplotlib.Show()
import matplotlib as mpl
df.show()
df1 = pd.DataFrame(np.random.randn(6,3), columns=['A','B','C'])
df2 = pd.DataFrame(np.random.randn(6,3), columns=['D','E','F'])
df3 = df1.copy()
df1
df = pd.concat([df1, df2])
df
df = pd.append([df1, df2])
help(pd.concat)
df = pd.append([df1, df2], join='Inner')
df = pd.concat([df1, df2], join='Inner')
df = pd.concat([df1, df2], join=inner)
df = pd.concat([df1, df2], join='inner')
df
df = pd.concat([df1, df2], join_axes='inner')
df = df1.append(df2)
df
df = pd.concat([df1, df2], axes=1)
df = df1.append(df2, axis=1)
df = df1.append(df2, ignore_index=1)
df
df = df1.append(df2, ignore_index=0)
df
df = pd.concat([df1, df2])
df
df = pd.concat([df1, df2], axis=0)
df
df = pd.concat([df1, df2], axis=1)
df
save
%notebook [-e] pandatry1.py

