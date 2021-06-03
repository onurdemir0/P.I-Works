# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("country_vaccination_stats.csv")

#print(data.columns)
#print(data[(data["country"]=="Kuwait")])

noHaveAnyValidVac = data.groupby('country')['daily_vaccinations'].min() #here only Kuwait is reached as missing data
noHaveAnyValidVacDf = pd.DataFrame(noHaveAnyValidVac)

print(noHaveAnyValidVacDf)

noHaveAnyValidVacDf['daily_vaccinations'].fillna(value=0 ,inplace=True) #here only missing data in kuwait is replaced
print(noHaveAnyValidVacDf)

data['daily_vaccinations'].fillna(data.groupby('country')['daily_vaccinations'].min(), inplace=True)