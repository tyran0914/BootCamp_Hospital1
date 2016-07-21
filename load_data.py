import csv
import pandas as pd
import numpy as np

def loadHeart(file,k):
    with open(file, 'rU') as csvIN:
        outCSV=[float(field) for row in csv.reader(csvIN, delimiter=' ') for field in row if field and field != 'name']
    outCSV_df = pd.DataFrame(zip(*[iter(outCSV)]*k))
    outCSV_df.replace(float(-9),np.nan,inplace=True)
    return outCSV_df

col_names = ['id','ccf','age','sex','painloc','painexer','relrest','pncaden',
             'cp','trestbps','htn','chol','smoke','cigs','years','fbs','dm',
             'famhist','restecg','ekgmo','ekgday','ekgyr','dig','prop','nitr',
             'pro','diuretic','proto','thaldur','thaltime','met','thalach',
             'thalrest','tpeakbps','tpeakbpd','trestbps','trestbpd','exang',
             'xhypo','oldpeak','slope','rldv5','rldv5e','ca','restckm',
             'exerckm','restef','restwm','exeref','exerwm','thal','thalsev',
             'thalpul','earlobe','cmo','cday','cyr','num','lmt','ladprox',
             'laddist','diag','cxmain','ramus','om1','om2','rcaprox','rcadist',
             'lvx1','lvx2','lvx3','lvx4','lvf','cathef','junk']  

col_types = ['int','int','int','bool','bool','bool','bool','category','category',
             'float','int','int','int','int','int','float','int','int',
             'category','int','int','int','int','int','int','int','int',
             'category','float','float','float','float','float','float',
             'float','float','float','int','int','float','float','float',
             'float','int','float','float','float','int','float','float',
             'category','int','int','int','int','int','int','category',
             'int','int','int','int','int','int','int','int','int','int','int',
             'int','int','int','int','float','float']


def assign_types(df, col_names,col_types):
    for i in range(10):  
        df[col_names[i]] = df[col_names[i]].astype(col_types[i])
    return df
  
file = './data/heart_disease/long-beach-va.data'    
VA_df = loadHeart(file,75)
VA_df.columns = col_names



VA_df = assign_types(VA_df,col_names,col_types)


i = 7
VA_df[col_names[i]].dtypes

VA_df[col_names[i]] = VA_df[col_names[i]].astype(col_types[i])
VA_df[col_names[i]].dtypes

VA_df[col_names[i]] = VA_df[col_names[i]].astype(col_types[i])



VA_df.replace('-9',np.nan)







file = './data/heart_disease/hungarian.data'
Hung_df = loadHeart(file,76)
Hung_df.columns = col_names

file = './data/heart_disease/switzerland.data'
Switz_df = loadHeart(file,76)
Switz_df.columns = col_names

file = './data/heart_disease/new.data'
CLE_df = loadHeart(file,90)  
  
VA_df = assign_types(VA_df,col_names,col_types)
  
 VA_df.replace(to_replace=['-9'], value=np.nan, inplace=True)
 
 VA_df.map({'-9':1})
  







