# -*- coding: utf-8 -*-
"""
Created on % 27/02/2024

@author: % Md. Waheduzzaman Nouman
"""

# This code may not work in case of different well numbers and well arrangement

import pandas as pd
import matplotlib.pyplot as plt


def prod_well_temp(file):
    #file = 'C:\\Users\\USER\\Desktop\\TVS\Petrasim_reservoir_modeling\\Hetaroginious\\FOFT'
    
    df = pd.read_csv(file,header=None)
    index_of_prod_well = []
    time = df.iloc[:, 1]/31536000
    total_number_aqua_layer = 4
    
    
    # 5--> no of column per element in FOFT file
    # 4--> there are four grids around the wells (for rectangular blocks grid) in each layer
    no_of_well = 2
    column_number = 5*4*total_number_aqua_layer * no_of_well+2
    
    
    current_num = 24 #starting column no for the well temp in the FOFT file
    flag = 0
    while(current_num <= column_number):
        
        if flag == 4:
            current_num = current_num + 20
            flag = 0
            
        else:
            flag += 1
            index_of_prod_well.append(current_num)
            current_num = current_num + 5
            
    pro_well_temp = 0
        
    for index in index_of_prod_well:
        pro_well_temp += df.iloc[:, index]
    
    pro_well_temp /= (4*total_number_aqua_layer)
    
    
    
    
    index_of_prod_well = []
    current_num = 4 #starting column no for the well temp in the FOFT file
    flag = 0
    while(current_num <= column_number):
        
        if flag == 4:
            current_num = current_num + 20
            flag = 0
            
        else:
            flag += 1
            index_of_prod_well.append(current_num)
            current_num = current_num + 5
            
    inj_well_temp = 0
        
    for index in index_of_prod_well:
        inj_well_temp += df.iloc[:, index]
    
    inj_well_temp /= (4*total_number_aqua_layer)
    
    
    return time, pro_well_temp,inj_well_temp
