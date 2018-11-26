# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 11:30:42 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd
from scipy import stats

#Question: Are gender and education level dependent at 5% level of significance?

  #Null Hypothesis(Ho): No dependency(association)
  #Alternative Hypothesis(Ha): There is dependecy(association)
  
# Data organization

    #*******The Raw Data*****
     #High School Bachelors Masters Ph.d. Total
     #Female 60 54 46 41 201
     #Male   40 44 53 57 194
     # Total 100 98 99 98 395

    #Creating data frame
table = pd.DataFrame({'gender':['Female', 'Male'], 'High School' :[60,40],'Bachelors' : [54,44],'Masters':[46,53],'Ph_d':[41,57]})

data=pd.melt(table,id_vars='gender',value_vars=['High School','Bachelors','Masters','Ph_d'],var_name='education',value_name='counts')

# creating a crosstab for chi square test

crosstab = pd.pivot_table(data,values='counts',index='education',columns='gender')

stats.chi2_contingency(crosstab)

# The Chi square test out:
    # chi square value=8
    # p-value=0.046
    # degrees of freedom=3

# Conclusion
   # p-value is approximately 0.05 which is thesame as 5% level of significance
   # The dependency of gender and education level exist but not significant   
