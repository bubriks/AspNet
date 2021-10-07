# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 17:02:45 2021

@author: bubri
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('results.csv', header=0)

implementations = ["core", "framework"]
for imp in implementations:
    df[imp] = df[imp][df[imp].between(0, df[imp].quantile(.99))]

df = pd.melt(df, value_vars=['core','framework'], var_name='Implementation', value_name="time (ms)")

###########################################################################
# histogram

def hist():
    sns.displot(data=df, hue='Implementation',x='time (ms)',
            kind="kde", fill=True)

##########################################################################
# boxplot

def box():
    sns.boxplot(data=df, x='time (ms)', y="Implementation")

#########################################################################
# culmilative distribution

def cul():
    ax = sns.kdeplot(
        data=df, x="time (ms)", hue="Implementation",
        cumulative=True, common_norm=False, common_grid=True, fill=True
    )
    ax.legend_.set_bbox_to_anchor((1, 0.6))
    ax.legend_._set_loc(2)

hist()