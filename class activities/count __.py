import pandas as pd
file_path='F:\exercise\mycode\My-projects\sample_text.txt'
try:
    df_text=pd.read_csv(file_path,header=None,sep='/n')
    text=df_text[0].str.cat(sep=' ')
    count=text.count('__')
    print(f"Number of occurrences of '__': {count}")
except FileNotFoundError:
    print(f"This file is not found")
except Exception as e :
    print("Error reading file")