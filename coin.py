import numpy as np
import krippendorff as kf
import pandas as pd 

ls = ['info_source','news_source','identity','single_story','tone','frame','cons']

df1 = pd.read_excel('coded1.xlsx')
df1 = df1.fillna(-1)
coder1= [[] for i in range(7)]

#row = df.shape[0]
row = 29
for i in range(row):
    a = np.array(df1.iloc[[i],]).tolist()
    ques = [a[0][3:9],a[0][9:13],a[0][13:21],a[0][21:23],a[0][23:25],a[0][25:33],a[0][33:37]]

    for j in range(7):
        coder1[j].extend(ques[j])

#coder2
df2 = pd.read_excel('coded2.xlsx')
coder2= [[] for i in range(7)]

for i in range(row):
    a = np.array(df2.iloc[[i],]).tolist()
    ques = [a[0][3:9],a[0][9:13],a[0][13:21],a[0][21:23],a[0][23:25],a[0][25:33],a[0][33:37]]

    for j in range(7):
        coder2[j].extend(ques[j])

#coder3
df3 = pd.read_excel('coded4.xlsx')
df3 = df3.fillna(-1)
coder3= [[] for i in range(7)]

for i in range(row):
    a = np.array(df3.iloc[[i],]).tolist()
    '''
    info_source = a[0][3:9]
    news_source = a[0][9:13]
    identity = a[0][13:21]
    single_story = a[0][21:23]
    tone = a[0][23:25]
    frame = a[0][25:33]
    cons = a[0][33:37]
    '''
    ques = [a[0][3:9],a[0][9:13],a[0][13:21],a[0][21:23],a[0][23:25],a[0][25:33],a[0][33:37]]

    for j in range(7):
        coder3[j].extend(ques[j])

#coder.append(coder1)
for j in  range(7):
    coder = []
    coder.append(coder1[j])
    coder.append(coder2[j])
    #coder.append(coder3[j])
    print(ls[j],':')
    print(round(kf.alpha(reliability_data=coder, level_of_measurement='nominal'), 4))
    print()
'''
1-me
2-不高兴前29条信度：0.8164
3-腿毛 优秀！
'''

