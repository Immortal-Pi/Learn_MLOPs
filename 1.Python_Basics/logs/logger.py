import logging

## Configure the basic loggin settings 
## kernel needs to be restarted every time we change the basic config 
logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S" 
                    )
