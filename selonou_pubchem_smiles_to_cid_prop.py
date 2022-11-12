#go to https://anaconda.org/bioconda/pubchempy and install with conda puchmepy: conda install -c bioconda pubchempy or !pip install pubchempy to install the library pubchempy

#https://www.kaggle.com/code/divyansh22/chemical-feature-extraction-using-pubchempy#5.-Getting-all-the-available-properties
import pubchempy as pcp
import pandas as pd
df=pd.read_csv('kinase.csv', sep=',')
print(df.shape)
data=[]
for mol in df['SMILES']:
    properties=pcp.get_properties(['MolecularFormula', 'MolecularWeight','InChI', 'InChIKey', 'IUPACName',
                                'XLogP', 'ExactMass', 'MonoisotopicMass', 'TPSA', 'Complexity', 'Charge',
                                'HBondDonorCount', 'HBondAcceptorCount', 'RotatableBondCount',
                                'HeavyAtomCount', 'IsotopeAtomCount', 'AtomStereoCount',
                                'DefinedAtomStereoCount', 'UndefinedAtomStereoCount', 'BondStereoCount',
                                'DefinedBondStereoCount', 'UndefinedBondStereoCount', 'CovalentUnitCount',
                                'Volume3D', 'XStericQuadrupole3D', 'YStericQuadrupole3D',
                                'ZStericQuadrupole3D', 'FeatureCount3D', 'FeatureAcceptorCount3D',
                                'FeatureDonorCount3D', 'FeatureAnionCount3D', 'FeatureCationCount3D',
                                'FeatureRingCount3D', 'FeatureHydrophobeCount3D', 'ConformerModelRMSD3D',
                                'EffectiveRotorCount3D', 'ConformerCount3D'], mol, 'smiles')
    data.append(properties)
len(data[0][0].keys())
rows=[]
columns=data[0][0].keys()
for mol in range(86):
    rows.append(data[mol][0].values())
df_results=pd.DataFrame(data=rows, columns=columns)
df_results.insert(1, 'SMILES', df['SMILES'], True)
df_results['Compound No.'] = df['Compound No.']
df_results['IC50 (nM)'] = df['IC50 (nM)']
df_results['delta G kcal'] = df['delta G kcal']
df_results.to_csv('properties_kinases.csv', index=False)
