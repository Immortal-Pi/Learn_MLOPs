from mlflow_utils import create_dataset
from hyperopt import fmin, tpe, hp, Trials, STATUS_OK

def objective(params:dict)->dict:
    """
    Objective function for hyperopt.
    :param params: dict
    :return: dict
    """
    y=(params['x']+3)**2+2
    #y=(params['x']-3)**2+2
    #y=(params['x']+1)**2+2
    return y 



if __name__=='__main__':
    df=create_dataset()
    #print(df.head())

    space={'x':hp.uniform('x',-10,10)}

    trials=Trials()
    best=fmin(
        fn=objective,
        space=space,
        algo=tpe.suggest,   # use json optimization in the search space
        max_evals=100,      # number of iterations
        trials=trials       # store the results
        )
    
    print(best)