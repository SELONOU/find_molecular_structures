#### This script check and convert molecules names or other identifiers (CAS No), ...... into smile format.... by using Chemical Identifier Resolver
import pandas as pd
from urllib.request import urlopen
from urllib.parse import quote
name=[]
smile=[]
def CIRconvert(mol_names_ids_cas_N0):
    try:
        url = 'http://cactus.nci.nih.gov/chemical/structure/' + quote(mol_names_ids_cas_N0) + '/smiles'  #(Chemical Identifier Resolver : https://cactus.nci.nih.gov/chemical/structure/"structure identifier"/"representation")
        check = urlopen(url).read().decode('utf8') #(This method is used to convert from one encoding scheme, in which argument string is encoded to the desired encoding scheme)
        return check
    except:
        return None

Molecules_names  = ['Chlorpromazine', 'Haloperidol', 'Sulpiride', 'Trifluoperazine', 'Amisulpride', 'Aripiprazole', 'Asenapine', 'Blonanserin', 'Brexpiprazole', 'Cariprazine', 'loperidone', 'Lumateperone', 'Lurasidone', 'Olanzapine', 'Paliperidone', 'Pimavanserin', 'Quetiapine', 'Risperidone', 'Ziprasidone']

for mol_names_ids_cas_N0 in Molecules_names :
    check=CIRconvert(mol_names_ids_cas_N0)
    if check:
        name.append(mol_names_ids_cas_N0)
        smile.append(check)
    print(mol_names_ids_cas_N0, CIRconvert(mol_names_ids_cas_N0))
df_results=pd.DataFrame()
df_results["Names"]=name
df_results["Smiles"]=smile
df_results.to_csv("output_selonou.csv", index=None)
