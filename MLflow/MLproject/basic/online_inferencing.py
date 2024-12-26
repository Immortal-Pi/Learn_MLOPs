from package.feature.data_processing import get_feature_dataframe
from package.ml_training.retrieval import get_train_test_score_set
import json 
import requests
from pprint import pprint

if __name__=='__main__':
    df=get_feature_dataframe()
    xtrain,xtest,xscore,ytrain,ytest,yscore=get_train_test_score_set(df)
    features=[f for f in xtrain.columns if f not in ['id','target','MedHouseVal']]
    features_values=json.loads(xscore[features].iloc[1:2].to_json(orient='split'))
    # print(features_values)

    payload={'dataframe_split':features_values}
    # pprint(
    #     payload,
    #     indent=4,
    #     depth=10,
    #     compact=True
    # )
   
    # host the model on the local machine 
    # mlflow models serve --model-uri models:/resgistered_model/latest --no-conda 

    # API request 
    BASE_URI='http://127.0.0.1:5000/'
    headers={'Content-Type':'application/json'}
    endpoint=BASE_URI+'invocations'
    r=requests.post(endpoint,data=json.dumps(payload),headers=headers)
    print(f'STATUS CODE: {r.status_code}')
    print(f'PREDICTION: {r.text}')
    print(f'TARGET: {yscore.iloc[1:2]}')
