# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:08:46 2021

@author: bubri
"""

import requests

number_of_tests = 1000

implementation = "framework"
url = "http://localhost:57913/api/FrameworkTest/GetStudents"

for run in range(6):
    data = []

    for i in range(number_of_tests):
        response = requests.get(url)
        if response.status_code == 200:
            data.append(response.elapsed.total_seconds())
    
    with open(f"raw_data\\{implementation}_{number_of_tests}_{run}.txt","w") as f:
        f.write(str(data))