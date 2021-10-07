# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:56:25 2021

@author: bubri
"""
from statsmodels.stats.power import TTestIndPower
import numpy as np
import ast

def convert(value):
    return ast.literal_eval(value)

core = convert(open('raw_data/core_1000.txt').read())
framework = convert(open('raw_data/framework_1000.txt').read())

def pooled_standard_deviation(sample1,sample2):
    #calculate the sample size
    n1, n2 = len(sample1), len(sample2)
    #calculate the variances
    var1, var2 = np.var(sample1, ddof=1), np.var(sample2, ddof=1)
    #calculate the pooled standard deviation
    numerator = ((n1-1) * var1) + ((n2-1) * var2)
    denominator = n1+n2-2
    return np.sqrt(numerator/denominator)

def Cohens_d(sample1, sample2):
    u1, u2 = np.mean(sample1), np.mean(sample2)
    s_pooled = pooled_standard_deviation(sample1, sample2)
    #print(s_pooled)
    return ((u1 - u2) / s_pooled)

# parameters for power analysis
effect_size = Cohens_d(framework,core)
alpha = 0.05
power = 0.8
ratio_ = 1
print('Effect size is {0}'.format(effect_size))
analysis = TTestIndPower()
sample_size = analysis.solve_power(effect_size, power=power, nobs1=None, ratio=ratio_, alpha=alpha)
print('Sample Size: %.3f' % sample_size)