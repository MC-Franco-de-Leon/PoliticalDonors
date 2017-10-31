
# coding: utf-8

# In[1]:


import os
import time
import mmap
import numpy as np
import pandas as pd
import re
import datetime
from numpy import median


# In[ ]:





# In[2]:


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d%m%Y')
        return True
    except ValueError:
        raise ValueError("Incorrect data format, should be DDMMYYYY")
        return False



# In[3]:


def medbyzip(CMTE_ID,ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID):
    global dfzip

    zipcode_string = str(ZIP_CODE)
    ZIP=zipcode_string[0:5]
  
    if len(ZIP)==5:
        
        if dfzip.loc[(dfzip['CMTE_ID'] == CMTE_ID) & (dfzip['ZIP'] == ZIP)].empty:
            print('NEW ENTRY')
        else:
            print('New contribution of exixting unique ID')
        dfzip.loc[len(dfzip)] =[CMTE_ID, ZIP, 0, 0, 0,TRANSACTION_AMT]#initialize media and contributions for this entry
        alltransactions=(dfzip.loc[(dfzip['CMTE_ID'] == CMTE_ID) & (dfzip['ZIP'] == ZIP),'TRANSACTION'])
        median=alltransactions.median()
        amttransactions=alltransactions.count()
        sumtransactions=alltransactions.sum()
  
        dfzip.loc[len(dfzip)-1] =[CMTE_ID, ZIP, round(median), amttransactions, sumtransactions,TRANSACTION_AMT]#write values to data frame  

    else:
        print('INCORRECT ZIP CODE FORMAT')


# In[4]:


def medbydate(CMTE_ID,ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID):
    global dfdate
    if len(TRANSACTION_DT)==8:
        YEAR=TRANSACTION_DT[4:8]
        DAY=TRANSACTION_DT[2:4]
        MONTH=TRANSACTION_DT[0:2]

        date=DAY+MONTH+YEAR
        print(date)
        if (validate(DAY+MONTH+YEAR)):#valid format of date
        
            if dfdate.loc[(dfdate['CMTE_ID'] == CMTE_ID) & (dfdate['DATE'] == date)].empty:
                print('NEW ENTRY')
            else:
                print('New contribution of exixting unique ID')
            dfdate.loc[len(dfdate)] =[CMTE_ID, date, 0, 0, 0,TRANSACTION_AMT]#initialize media and contributions for this entry
            alltransactions=(dfdate.loc[(dfdate['CMTE_ID'] == CMTE_ID) & (dfdate['DATE'] == date),'TRANSACTION'])
            median=alltransactions.median()
            amttransactions=alltransactions.count()
            sumtransactions=alltransactions.sum()
  
            dfdate.loc[len(dfdate)-1] =[CMTE_ID, date, round(median), amttransactions, sumtransactions,TRANSACTION_AMT]#write values to data frame  
        else:
            print('IGNORED, INCORRECT FORMAT FOR DATE, SHOULD BE DDMMYYYY')
    else:
         print('IGNORED, INCORRECT FORMAT FOR DATE, SHOULD BE DDMMYYYY')


# In[5]:



with open('/home/cristobal/Desktop/dataengineering/input') as f:
    columns=['CMTE_ID', 'ZIP','MEDIAN','TRANSACTIONS','CONTRIBUTION', 'TRANSACTION']
    dfzip = pd.DataFrame(columns=columns, index=[])
    columnsd=['CMTE_ID', 'DATE','MEDIAN','TRANSACTIONS','CONTRIBUTION', 'TRANSACTION']
    dfdate = pd.DataFrame(columns=columnsd, index=[])
    
    for line in f:
        x=line.split("|")
        print ("")

        if len(x)>1:
            CMTE_ID=x[0]
            ZIP_CODE=x[10]
            TRANSACTION_DT=x[13]
            TRANSACTION_AMT=float(x[14])
            OTHER_ID=str(x[15])
  
            if (OTHER_ID == ""):
                OTHER_ID="empty"
                if  (CMTE_ID == "") or (TRANSACTION_AMT==""):
                    print ('IGNORED bec CMTE_ID or TRANSACTION_AMT is empty')
                else: #after we check OTHER_ID=empty and both CMTE_ID,TRANSACTION_AMT  non empty  

                    medbyzip(CMTE_ID,ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)
                    medbydate(CMTE_ID,ZIP_CODE, TRANSACTION_DT, TRANSACTION_AMT, OTHER_ID)
                    print(dfzip)
                    print(dfdate)
                    
            else:
                    print('EXLUDED ID :',OTHER_ID)
                    
    file = open('dfzip.txt','w')   
    del dfzip['TRANSACTION']
    np.savetxt(r'/home/cristobal/Desktop/dataengineering/medzip.txt', dfzip, fmt='%s', delimiter='|')  
               
    file = open('dfdate.txt','w')   
    del dfdate['TRANSACTION']
    np.savetxt(r'/home/cristobal/Desktop/dataengineering/meddate.txt', dfdate, fmt='%s', delimiter='|')           

