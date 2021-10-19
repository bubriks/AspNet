# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:30:15 2021

@author: bubri
"""
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind
from scipy import stats

df = pd.read_csv('results.csv', header=0)

print(df.describe())

def standardDeviationRange(data, sd_nr, median, sd):
    return [x for x in data if (x <= median + sd_nr * sd)]

def percentage(data1, data2):
    return str(len(data1)/len(data2)*100)

for imp in ["core", "framework"]:
    data = df[imp]
    mean = np.mean(data)
    mode = stats.mode(data)
    median = np.median(data)
    sd = np.std(data)
    minimum = np.min(data)
    maximum = np.max(data)
    print(f"{imp} mean: " + str(mean))
    print(f"{imp} mode: " + str(mode))
    print(f"{imp} median: " + str(median))
    print(f"{imp} std: " + str(sd))
    print(f"{imp} min: " + str(minimum))
    print(f"{imp} max: " + str(maximum))
    print(f"{imp} failed requests: " + str(6000-len(data)))
    percent = percentage(standardDeviationRange(data, 1, median, sd), data)
    print(f"{imp} 1 standard deviation away: " + percent)
    percent = percentage(standardDeviationRange(data, 2, median, sd), data)
    print(f"{imp} 2 standard deviation away: " + percent)
    print()

a = df.loc[df['core'] > np.min(df["framework"]),'core'].count() / df['core'].count() * 100
print(f'% of values in core with value higher than min of framework={a}')

tstatistic, pvalue = ttest_ind(df["core"], df["framework"])
print(f't-statistic={tstatistic}, p-value={pvalue}')