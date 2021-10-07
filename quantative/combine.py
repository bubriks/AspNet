# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:21:01 2021

@author: bubri
"""
import ast
import pandas as pd

def convert(value):
    return ast.literal_eval(value)

core_1000_0 = convert(open('raw_data/core_1000_0.txt').read())
core_1000_1 = convert(open('raw_data/core_1000_1.txt').read())
core_1000_2 = convert(open('raw_data/core_1000_2.txt').read())
core_1000_3 = convert(open('raw_data/core_1000_3.txt').read())
core_1000_4 = convert(open('raw_data/core_1000_4.txt').read())
core_1000_5 = convert(open('raw_data/core_1000_5.txt').read())
core = core_1000_0 + core_1000_1 + core_1000_2 + core_1000_3 + core_1000_4 + core_1000_5
core = [x * 1000 for x in core] #to make it millisecond

framework_1000_0 = convert(open('raw_data/framework_1000_0.txt').read())
framework_1000_1 = convert(open('raw_data/framework_1000_1.txt').read())
framework_1000_2 = convert(open('raw_data/framework_1000_2.txt').read())
framework_1000_3 = convert(open('raw_data/framework_1000_3.txt').read())
framework_1000_4 = convert(open('raw_data/framework_1000_4.txt').read())
framework_1000_5 = convert(open('raw_data/framework_1000_5.txt').read())
framework = framework_1000_0 + framework_1000_1 + framework_1000_2 + framework_1000_3 + framework_1000_4 + framework_1000_5
framework = [x * 1000 for x in framework] #to make it millisecond

df = pd.DataFrame(list(zip(core, framework)),
               columns =['core', 'framework'])

df.to_csv("results.csv")