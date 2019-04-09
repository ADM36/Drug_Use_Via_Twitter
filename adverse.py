import pandas as pd

adverse_data = pd.read_csv('REAC18Q4.txt', sep="$")
#QUARTERLY DATA EXTRACT (QDE) FROM THEFDA ADVERSE EVENT REPORTING SYSTEM (FAERS)
# contains all "Medical Dictionary for RegulatoryActivities" (MedDRA) terms coded for the event (1 or more)

adverse_data.columns = ['primary_id', 'case_id', 'adverse_reaction', 'delete']
adverse_data.drop(['delete'], axis=1, inplace = True)
adverse_data['adverse_reaction'] = adverse_data['adverse_reaction'].str.lower()

#CREATING A LIST OF UNIQUE ADVERSE REACTIONS
#print(adverse_data.shape)
adverse_list = adverse_data['adverse_reaction'].unique().tolist()
#print(adverse_list[:10])

adverse_data.drop_duplicates(subset=['primary_id'], inplace = True)
#print(adverse_data.shape)
#print(adverse_data.head(n=10))

#CREATING A DICTIONARY WHOSE KEYS ARE ADVERSE REACTIONS AND VALUES ARE MEDRA CODES
ADVERSE_DIC = {}
for index, row in adverse_data.iterrows():
    if row['adverse_reaction'] not in ADVERSE_DIC:
        ADVERSE_DIC[row['adverse_reaction']] = [row['primary_id'], row['case_id']]
    else:
        pass
#print(ADVERSE_DIC)


#BELOW IS A NEW DATA SET
#The Patient-Friendly Term List is a subset of MedDRA Lowest Level Terms (LLTs) that has been derived from the most frequently reported adverse events by patients and consumers in a variety of pharmacovigilance databases. It is available in English and currently comprises approximately 1,400 LLTs.

# MUST INSTALL xlrd module for below to work - pip install xlrd
patient_data = pd.read_excel('patient-friendly_term_list.xlsx')
patient_data.columns = ['adverse_reaction', 'LLT_code']
#print(patient_data.head())

#CREATING A DICTIONARY WHOSE KEYS ARE COMMON, PATIENT FRINDLY LANGUAGE ADVERSE REACTIONS AND VALUES ARE MEDRA CODES
PATIENT_FRIENDLY_DIC = {}
for index, row in patient_data.iterrows():
    if row['adverse_reaction'] not in ADVERSE_DIC:
        PATIENT_FRIENDLY_DIC[row['adverse_reaction'].lower()] = [row['LLT_code']]
    else:
        pass
#print(PATIENT_FRIENDLY_DIC)

adverse_data = pd.DataFrame(PATIENT_FRIENDLY_DIC.items())
columns = ['adverse', 'LLT']
adverse_data.to_csv('final_adverse.csv', index=False, header = columns)
