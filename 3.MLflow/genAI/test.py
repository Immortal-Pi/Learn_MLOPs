import mlflow
import os 
# from langchain.chat_models import AzureChatOpenAI
# from openai import AzureOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv
import dagshub
import pandas as pd 
import openai 

load_dotenv()
# creating test data 
eval_data=pd.DataFrame(
    {
        'inputs':[
            "what is MLflow?",
            "What is Spark?",
        ],
        "ground_truth":[
            "DagsHub is a collaborative platform for data science and machine learning projects, designed to streamline and centralize workflows. It integrates version control, data management, and collaboration tools into a single platform, making it easier for teams to work together on projects involving code, data, and models.",
            "Apache Spark is an open-source, distributed computing system designed for big data processing and analytics. It provides a fast and general-purpose engine for processing large-scale data with high efficiency and scalability."
        ]
    }
)

mlflow.set_experiment('LLM Evaluation')
openai.api_type='azure'
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_BASE"] = "https://llmops-amruth.openai.azure.com/"
os.environ["OPENAI_DEPLOYMENT_NAME"] = "gpt-4"
os.environ["OPENAI_API_VERSION"] = os.getenv('AZURE_OpenAI_API_VERSION')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('GRAPHRAG_API_KEY')
os.environ["OPENAI_API_KEY"] = os.getenv('GRAPHRAG_API_KEY')
with mlflow.start_run() as run:
    system_prompt='Answer the following questions in 2 sentences'
    logged_model_info=mlflow.openai.log_model(
        model='gpt-4',
        task=openai.chat.completions,
        artifact_path='model',
        messages=[
            {'role':'system','content':system_prompt},
            {'role':'user','content':"{question}"}
        ]
    )

    #use predefined question-answer metrics to evaluate our model
    results=logged_model_info=mlflow.evaluate(
        logged_model_info.model_uri,
        eval_data,
        targets='ground_truth',
        model_type='question-answering',
        extra_metrics=[mlflow.metrics.toxicity(),mlflow.metrics.latency(),mlflow.metrics.genai.answer_similarity()]
    

    )
    print(f'see the aggregate results below: \n{results.metrics}')

    # Evaluation result for each data record is available in results.tables
    eval_table=results.tables['eval_results_table']
    df=pd.DataFrame(eval_table)
    df.to_csv('eval.csv')
    print(f'see evaluation table below: \n{eval_table}')
