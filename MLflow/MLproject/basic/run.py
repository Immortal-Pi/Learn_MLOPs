from package.package.feature.data_processing import get_feature_dataframe

if __name__=='__main__':
    experiment_name='house_pricing_classifier'
    run_name='testing_classifier'
    df=get_feature_dataframe()
    print(df.head())