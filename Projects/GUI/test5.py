import numpy as np
import pandas as pd
x= np.array(range(0,240))
y= np.array(range(60,200))

x1 = []
y1= []
stress1 =[]
print(x)

def  getStress(x,y):
    # print(item2)
    if (16 < x < 130 and 90 < y < 120):
            print('Stressad', x, y)
            # x1.append(x)
            # y1.append(y)
            return 2
    else:
        print('Inte stressad', x, y)
        # x1.append(x)
        # y1.append(y)
        return 1

x=129
y=93
x1.append(x)
y1.append(y)
stress1.append(getStress(x,y))

getStress(15,89)
getStress(17,93)
getStress(19,119)
getStress(23,78)



df = pd.DataFrame()
df['X'] = x1
df['Y'] =y1
df['Stress'] = stress1
print(df)