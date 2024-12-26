from typing import Tuple
from typing import List
import pandas as pd 
from sklearn.model_selection import train_test_split

def get_train_test_score_set(df:pd.DataFrame)->Tuple:
    """ 
    Get training and testing sets
    :param df: Dataframe
    :return: Training, testing and validation dataframes 
    """
    xtrain,xtest,ytrain,ytest=train_test_split(
        df.drop('target',axis=1),
        df['target'],
        test_size=0.3,
        random_state=42
        )
    xtest,xscore,ytest,yscore=train_test_split(
        xtest,ytest,test_size=0.5,random_state=42
    )

    return xtrain,xtest,xscore,ytrain,ytest,yscore