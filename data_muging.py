#USE CASE***********
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

country= pd.read_csv('/root/Downloads/API_ILO_country_YU.csv', index_col=0)
df=country.head(5)
df= df.set_index(["Country Code"])

sd=df.reindex(columns=['2010','2011'])
db=sd.diff(axis=1)
db.plot(kind='bar')
plt.show()
