#PANDA Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

D_web= {'Days':['SUN','MON','TUE','WED','THR','FRI','SAT'],"Visitors":[1000,400,450,600,700,950,800],'Bounce_Rate':[200,200,222,300,312,200,150]}
df=pd.DataFrame(D_web)
print(df)

#Slicing
print("\n Slicing*********")
print(df.head(2))
print("\n ")
print(df.tail(2))

#Merge
print("\n Merging*********************\n")
df1=pd.DataFrame({"HPI":[80,90,60,50],"Int_Rate":[2,1,2,3],"IND_GDP":[50,60,45,55]},
                 index = [2001,2002,2003,2004])

df2=pd.DataFrame({"HPI":[80,90,60,50],"Int_Rate":[2,1,2,3],"IND_GDP":[50,60,45,55]},
                  index=[2005,2006,2007,2008])

merge=pd.merge(df1,df2)
merge1=pd.merge(df1,df2, on="HPI")
print(merge)
print(merge1)

#Join
print("\n Joine******************************\n")
df1=pd.DataFrame({"Int_Rate":[2,1,2,3],"IND_GDP":[50,60,45,55]},
                 index = [2001,2002,2003,2004])

df2=pd.DataFrame({"Low_Tier_Rate":[50,44,65,25],"Unemployment":[1,2,3,4]},
                  index=[2001,2003,2004,2004])

joined=df1.join(df2)
print(joined)

#Changing index & Column
D_web= pd.DataFrame({'Days':['SUN','MON','TUE','WED','THR','FRI','SAT'],"Visitors":[1000,400,450,600,700,950,800],'Bounce_Rate':[200,200,222,300,312,200,150]})
D_web.set_index("Days",inplace=True)
print(D_web)
D_web.rename(columns={'Visitors':'Users'},inplace=True)
print(D_web)

#Graph
D_web.plot()
plt.show()

#Cancatination
print('\n Cancatination******************\n')
df1=pd.DataFrame({"HPI":[80,90,60,50],"Int_Rate":[2,1,2,3],"IND_GDP":[50,60,45,55]},
                 index = [2001,2002,2003,2004])

df2=pd.DataFrame({"HPI":[80,90,60,50],"Int_Rate":[2,1,2,3],"IND_GDP":[50,60,45,55]},
                  index=[2005,2006,2007,2008])
concat=pd.concat([df1,df2])
print(concat)
