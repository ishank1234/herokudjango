import numpy as np
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import os
def training():
    df=pd.read_csv('heart.csv')
    y=df['target']
    df.drop('target',axis="columns",inplace=True)
    X=df
    model=RandomForestClassifier()
    X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=5,test_size=0.1)
    model.fit(X_train,y_train)

    pkl_filename="pickle_model.pkl"
    with open(pkl_filename,'wb') as file:
        pickle.dump(model,file)

    print(model.score(X_test,y_test))
    yp=model.predict(X_test)
    print("hear_disease ",sum(yp==1))
    print("Not heart ",sum(yp==0))
    print(confusion_matrix(y_test,yp))

def prediction(ob):
    dl=ob.to_dict()
    df=pd.DataFrame(dl,index=[0])
    df.drop("target",axis="columns", inplace=True)
    pkl_filename="pickle_model.pkl"
    pkl_filename=os.path.dirname(__file__)+"/"+pkl_filename
    with open(pkl_filename,'rb') as file:
        model=pickle.load(file)
    pred=model.predict(df)
    return pred
if __name__=='__main__':
    training()
#training()
