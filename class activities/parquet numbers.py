import pandas as pd
file_text='F:\exercise\mycode\My-projects\Sample_data_2.parquet'
try:
    df_parquet=pd.read_parquet(file_text)
    num_features=df_parquet.shape[1]
    print(f"the number of features is {num_features}")
except FileNotFoundError:
    print(f"file {file_text} is not found ")
except Exception as e :
    print(f"Error reading file {e}")
