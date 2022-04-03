import pandas as pd
import logging

logging.basicConfig(filename = 'example.log', level = logging.INFO)

def create_dataframe():
    
    logging.info('Executing Function')
    logging.info('Creating Data')
    
    df = pd.DataFrame({"col_1":[1,2,3,4,5],
                        "col_2":["A","B","C","D","E"]
    })
    
    df.info()
    
    logging.info('Data Created')
    logging.info('Exiting')
    return df
    
create_dataframe()