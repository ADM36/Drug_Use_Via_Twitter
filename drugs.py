import pandas as pd

#file to hold list or dictionary of drugs
DRUGS_LIST = []
DRUGS_DIC = {}


drug_file = pd.read_csv("drug_names_cleaned.csv")

print(drug_file.head())

#for drug in drug_file['PROPRIETARYNAME']:
#    if drug not in DRUGS_DIC:
#        DRUGS_DIC[drug] = []
#    else:
#        pass

# iterate over rows with iterrows()
for index, row in drug_file.iterrows():
    if row['PROPRIETARYNAME'] not in DRUGS_DIC:
        DRUGS_DIC[row['PROPRIETARYNAME']] = [row['NONPROPRIETARYNAME']]
    else:
        pass

print(DRUGS_DIC)
