import pandas as pd

#file to hold list or dictionary of drugs
DRUGS_LIST = []
DRUGS_DIC = {}

#DATA FROM FDA
drug_file = pd.read_csv("drug_names_cleaned.csv")

print(drug_file.head())


# CREATING A DICTIONARY, DRUGS_DIC, WHOSE KEYS ARE THE PROPRITARY NAME OF A DRUG, AND WHOSE VALUES ARE NONPROPRIETARY NAMES FOR THAT SAME DRUG
# iterate over rows with iterrows()
for index, row in drug_file.iterrows():
    if row['PROPRIETARYNAME'] not in DRUGS_DIC:
        DRUGS_DIC[row['PROPRIETARYNAME']] = [row['NONPROPRIETARYNAME']]
    else:
        pass

#print(DRUGS_DIC)
