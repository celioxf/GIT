import pandas as pd


def create_dataframe():
    
    df = pd.DataFrame({"col_1":[1,2,3,4,5],
                        "col_2":["A","B","C","D","E"]
    })
    
    return df