import csv
import pandas as pd
import numpy as np

def loadHeart(file):
    with open(file, 'rU') as csvIN:
        outCSV=[float(field) for row in csv.reader(csvIN, delimiter=' ') for field in row if field and field != 'name']
    outCSV_df = pd.DataFrame(zip(*[iter(outCSV)]*75))
    outCSV_df.replace(float(-9),np.nan,inplace=True)
    return outCSV_df
   
def loadCLE(file):
    outCSV =[]
    with open(file, 'rU') as csvIN:
        for row in csv.reader(csvIN, delimiter=' '):
            for field in row:
                if field.isalpha() == False:
                    outCSV.append(float(field))
    outCSV_df = pd.DataFrame(zip(*[iter(outCSV)]*89))
    outCSV_df.replace(float(-9),np.nan,inplace=True)
    return outCSV_df

#col_types = ['int','int','int','category','category',
#             'category','category','int','category','float',
#             'category','category','category','int','int',
#             'float','int','int','category','int',
#             'int','int','int','int','int',
#             'float','category','category','category','int',
#             'int','int','category','category','category',
#             'category','category','category','float','float',
#             'float','float','float','float','float',
#             'float','float','category','category','float',
#             'float','float','float','int','float',
#             'float','float','int','float','float',
#             'category','int','int','int','int',
#             'int','int','category','int','int',
#             'int','int','int','float','float']
#
#def assign_types(df, col_names,col_types):
#    for i in range(10):  
#        df[col_names[i]] = df[col_names[i]].astype(col_types[i])
#    return df

def data_pipeline():
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
    ind_cols = ['id','ccf','age','sex','painloc','painexer','relrest','pncaden',
                 'cp','trestbps','htn','chol','smoke','cigs','years','fbs','dm',
                 'famhist','restecg','ekgmo','ekgday','ekgyr','dig','prop','nitr',
                 'pro','diuretic','proto','thaldur','thaltime','met','thalach',
                 'thalrest','tpeakbps','tpeakbpd','trestbps','trestbpd','exang',
                 'xhypo','oldpeak','slope','rldv5','rldv5e','ca','restckm',
                 'exerckm','restef','restwm','exeref','exerwm','thal','thalsev',
                 'thalpul','earlobe','cmo','cday','cyr', 'lmt','ladprox',
                 'laddist','diag','cxmain','ramus','om1','om2','rcaprox','rcadist',
                 'lvx1','lvx2','lvx3','lvx4','lvf','cathef','junk']
    file = './data/long-beach-va.data'    
    VA_df = loadHeart(file)
    VA_df.columns = col_names
    
    file = './data/hungarian.data'
    Hung_df = loadHeart(file)
    Hung_df.columns = col_names
    
    file = './data/switzerland.data'
    Switz_df = loadHeart(file)
    Switz_df.columns = col_names
    
    file = './data/new.data'
    CLE_df = loadCLE(file) 
    CLE_df.drop(CLE_df.columns[xrange(75,89)], axis=1, inplace=True)
    CLE_df.columns = col_names
    
    df = pd.concat([VA_df, Hung_df, Switz_df, CLE_df])
    
    return df, ind_cols
