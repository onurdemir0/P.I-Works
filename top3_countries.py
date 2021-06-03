# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("country_vaccination_stats.csv")

print(data.groupby('country')['daily_vaccinations'].median().sort_values(ascending=False).head(3))