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
        DRUGS_DIC[row['PROPRIETARYNAME']] = [row['PROPRIETARYNAME'], str(row['PROPRIETARYNAME']).lower(),
        str(row['PROPRIETARYNAME']).upper(), row['NONPROPRIETARYNAME']]
    else:
        pass

drugs_data = pd.DataFrame(DRUGS_DIC.items())
drugs_data_final = pd.DataFrame(drugs_data[1].values.tolist())

columns = ["PROPRIETARYNAME", "Lower", "UPPER", "NONPROPRIETARYNAME"]

drugs_data_final.to_csv('final_drugs.csv', index=False, header = columns)

print(drugs_data_final.head())
#print(DRUGS_DIC)
#
# for index, row in drug_file.iterrows():
#     if str(row['PROPRIETARYNAME']).lower() not in DRUGS_LIST:
#         DRUGS_LIST.append(str(row['PROPRIETARYNAME']).lower())
#     if row['NONPROPRIETARYNAME']:
#         if row['NONPROPRIETARYNAME'] not in DRUGS_LIST:
#             DRUGS_LIST.append(row['NONPROPRIETARYNAME'])
#         else:
#             pass
#
# print(DRUGS_LIST.head())
