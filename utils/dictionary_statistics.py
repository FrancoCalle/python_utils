# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 11:28:57 2018

@author: Franco
"""

#Summart statistics of Variables from Colombia Project:

import numpy as np
from pandas import DataFrame as df
from scipy.stats import trim_mean, kurtosis
from scipy.stats.mstats import mode, gmean, hmean

def statistics(Dictionary):
    
    Stat_List = []
    stat = []
    colname = []
    k = {}
    for i in range(0,len(Dictionary)):                                   # i selects the number i keyword in the dictionary
                

        if type(Dictionary[list(Dictionary.keys())[i]]) !=  int:

            if np.size(Dictionary[list(Dictionary.keys())[i]],1) == 1:         # if the number of columns is equal to one, then
                 
                s1 = np.nanmean(Dictionary[list(Dictionary.keys())[i]])          #average value in row
                s2 = np.nanstd(Dictionary[list(Dictionary.keys())[i]])           #standard deviation in row
                s3 = np.nanmin(Dictionary[list(Dictionary.keys())[i]])           #minimum value in row
                s4 = np.nanmax(Dictionary[list(Dictionary.keys())[i]])           #maximum value in row
                s5 = np.size(Dictionary[list(Dictionary.keys())[i]],0)        #number of elements in row
                v = np.array([s1, s2, s3, s4, s5])
                stat.append(v)
                colname.append(list(Dictionary.keys())[i])
                
            elif np.size(Dictionary[list(Dictionary.keys())[i]],1) > 1 and np.size(Dictionary[list(Dictionary.keys())[i]],1) <= 100:
                
                for j in range(0,np.size(Dictionary[list(Dictionary.keys())[i]],1)):
                    s1 = np.nanmean(Dictionary[list(Dictionary.keys())[i]][:,j])          #average value in row
                    s2 = np.nanstd(Dictionary[list(Dictionary.keys())[i]][:,j])           #standard deviation in row
                    s3 = np.nanmin(Dictionary[list(Dictionary.keys())[i]][:,j])           #minimum value in row
                    s4 = np.nanmax(Dictionary[list(Dictionary.keys())[i]][:,j])           #maximum value in row
                    s5 = np.size(Dictionary[list(Dictionary.keys())[i]][:,j],0)        #number of elements in row
                    k["Column %s" % (j)] = np.array([s1, s2, s3, s4, s5])                 #statistics compilation
                    stat.append(k["Column %s" % (j)])
                    colname.append(list(Dictionary.keys())[i]+': '+str(j+1))
# "Maximum Likelihood of iteration %s is %s" % (i, cost_history[i])           
            else :
                print('not appendable variable')
            
        else:
            print('not appendable variable')
    
    stat_array = np.asarray(stat).T      
    rownames = ['Mean', 'Std', 'Min', 'Max', 'Size']
    df = pd.DataFrame(stat_array, index=rownames, columns=colname)

    return df