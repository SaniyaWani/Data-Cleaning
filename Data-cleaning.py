import pandas as pd

df = pd.read_csv("Total_Stars.csv")


del df['Star_name1']
del df['Distance1']
del df['Mass1']
del df['Radius1']

df.to_csv('Final.csv')


    