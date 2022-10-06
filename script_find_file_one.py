import os
import pandas as pd
import csv
smiles_hypo_fund=[]
smiles_zinc_fund=[]
df1=pd.read_csv('all_smiles_format.csv', delimiter=',')
df2=pd.read_csv('AAAA.csv', delimiter=' ')
print(df1)
print(df2)
column_hypo = (df1["smiles_formats"]) 
column_zinc = (df2["smiles"])
for  col_hypo in column_hypo:
    for col_zinc in column_zinc:
        if col_hypo == col_zinc:
            print(True,col_hypo, col_zinc)
            smiles_hypo_fund.append(col_hypo)
            smiles_zinc_fund.append(col_zinc)
        else:
            print("False")
df_results = pd.DataFrame()
df_results["molecules_hypothetic"]=smiles_hypo_fund
df_results["molecules_fund"]=smiles_zinc_fund
df_results.to_csv("all_compounds_fund.csv",index=False)
