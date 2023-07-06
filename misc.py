import json
from sklearn.metrics import recall_score, roc_auc_score, confusion_matrix
from sklearn.base import BaseEstimator, TransformerMixin

def construct_line(model_name , dataset, scores, y, best_parameters):
  
    row=[]
    row.append(model_name)
    row.append(dataset)

    if scores is not None:
        for i in scores:
            row.append(i)
    else:        
        if 'predicted' in y.keys():
            row.append(100*recall_score(y['input'],y['predicted'],pos_label=1))   
            row.append(None)     
            row.append(100*recall_score(y['input'],y['predicted'],pos_label=0))        
            row.append(None)
        else:
            row.append(None)
            row.append(None)
            row.append(None)
            row.append(None)
        if 'scores' in y.keys():
            row.append(100*roc_auc_score(y['input'],y['scores']))
        else:
            row.append(None)
        row.append(None)    
            
    table = confusion_matrix(y['input'], y['predicted'])
    row.append(table[0][0])
    row.append(table[0][1])
    row.append(table[1][0])
    row.append(table[1][1])
    row.append(json.dumps(best_parameters))
    return row

class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values