# imports
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import label_binarize
from sklearn.cluster import AgglomerativeClustering
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#%matplotlib inline

import load_data

def model_diag(X, y):
    models = [Pipeline([('impute', Imputer()), ('fit',LogisticRegression())]),
              Pipeline([('impute', Imputer()), ('fit',GaussianNB())]), 
              Pipeline([('impute', Imputer()), ('fit',SVC(gamma=2, C=1))]), 
              Pipeline([('impute', Imputer()), ('fit',RandomForestClassifier())])]
    model_names = ['Logistic', 'GaussianNB', 'SVC', 'Forest']
    metrics = ['roc_auc', 'precision', 'recall', 'f1']
    
    fig, axarray = plt.subplots(nrows=2, ncols=2)
    axarray = axarray.flatten()
    fig.set_size_inches((10,5))
    
    for cur_ax, cur_metric, metric_name in zip(axarray, metrics, metrics):
        model_score_dict = {}
        for cur_model, cur_model_name in zip(models, model_names):
            cur_score = cross_val_score(estimator=cur_model, X=X, y=y, scoring=cur_metric)
            model_score_dict[cur_model_name] = cur_score.mean()
            
            pd.Series(model_score_dict)[model_names].plot(kind='bar', ax=cur_ax)
            cur_ax.set_title(cur_metric)
            cur_ax.set_xticklabels(model_names, rotation=0)
            cur_ax.set_ylim((0, 1))
            
    plt.tight_layout();


def run_new_model():
    df, ind_cols = load_data.data_pipeline()
    df['num_smaller'] = 'Yes'
    df.loc[df.num == 0.0, 'num_smaller'] = 'No'
    y = pd.Series(label_binarize(df['num_smaller'], classes=['No', 'Yes']).transpose()[0])
    ind_cols = ['age', 'sex', 'painloc', 'painexer', 'relrest', 'pncaden', 
            'trestbps', 'chol', 'smoke', 'cigs', 'fbs', 'dm', 'famhist']
    model_diag(df[ind_cols], y)

run_new_model()

# old model -- needs to be refactored
#ind_cols = ['age', 'sex']


#df_for_model = df.loc[:, ind_cols + ['num_smaller']]
#df_for_model = df_for_model.dropna(axis=0, how='any')
#y = pd.Series(label_binarize(df_for_model['num_smaller'], classes=['No', 'Yes']).transpose()[0])


#df_for_model['gender_yn'] = pd.get_dummies(df_for_model['sex'])[0]
#df_for_model['pain_yn'] = pd.get_dummies(df_for_model['painexer'])[0]

#ind_cols = ['age', 'gender_yn']

#model_diag(df[ind_cols], y)

# try clustering
#clusters = AgglomerativeClustering().fit(df_for_model[ind_cols])