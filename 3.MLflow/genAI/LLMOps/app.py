from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os 
from dotenv import load_dotenv

load_dotenv()



os.environ["OPENAI_API_BASE"] = "https://llmops-amruth.openai.azure.com/"
os.environ["OPENAI_DEPLOYMENT_NAME"] = "gpt-4"
os.environ["OPENAI_API_VERSION"] = os.getenv('AZURE_OpenAI_API_VERSION')
#os.environ["OPENAI_API_KEY"] = os.getenv('GRAPHRAG_API_KEY')
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv('GRAPHRAG_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')


prompt=ChatPromptTemplate.from_messages(
    [
        ('system','you are a sarcastic assistant, please be sarcastic to every question the user asks based on the given context'),
        ('user','Question:{question}\nContext:{context}')
    ]
)
model=AzureChatOpenAI(
    openai_api_version=os.getenv('AZURE_OpenAI_API_VERSION'),
    azure_deployment=os.getenv('AZURE_OPENAI_DEPLOYMENT_MODEL'),
    model_name=os.getenv('AZURE_OPENAI_DEPLOYMENT_MODEL'),
    api_key=os.getenv('GRAPHRAG_API_KEY')
)
output_parser=StrOutputParser()

chain=prompt|model|output_parser


question='what is the point if this is a dream?'
context='''Life is nothing but a dream. I’m just kidding. Life is not just a dream. It feels pretty real to me. Nature, sun, rain, pain, food, sex, keyboard, kissing, blood, it all feels very real to me.

Not only my body, also my mind, my consciousness, relationships with people that I love, they all feel very real, even though I can’t touch my mind and I can’t see the relationship bonds.

Don’t get bored, this blog post is not about arguing why life isn’t just a dream or why that could be true. You can find many philosophical debates about that online, from solipsism to discussions over whether Matrix could be real, and responses to Elon Musk saying that life is only a simulation and that we live in a video game.

In this blog post, I’ll talk about how perceiving life as a dream can be a good mental trick you can use to stay more (1) flexible and (2) creative. We will start with the creativity, but first what kind of a problem are we even trying to solve with this mental exercise.

The main problem is that because life feels very real, you take yourself and the world around you very seriously, including your limiting beliefs, assumptions, convictions and values that you’re emotionally heavily invested in.

To free yourself from the emotional pains, to open your mind and to play with different ideas, versions of yourself and potential future realities, it sometimes helps to see life as nothing but a dream.'''

print(chain.invoke({'question':question,'context':context}))