import pandas as pd

df = pd.read_excel('./Datasets/Form-B-Subset.xlsx')
df.Sex = df['Sex'].fillna('NA')

def getGender(value):
    value = str(value)
    value = value.lower().replace(" ", "")
    if value == 'f' or value == 'female':
        return 'F'
    elif value == 'm' or value == 'male':
        return 'M'
    else:
        return 'NA'


print(df['Sex'].unique())

df["Sex"] = df['Sex'].apply(getGender)
print(df['Sex'].unique())
print(df.isnull().sum())
