import pandas as pd


def preProcessFile(filename):
    df = pd.read_excel(filename)
    for column in df.columns:
        colname = 'Sex'
        if column == colname:
            print('Its a declared column: Sex')
            x = df[colname]
            x = x.fillna("NA")
            FinalValue = lambda a: 'F' if a == 'f' or a == 'female' else ('M' if a == 'm' or a == 'male' else 'NA')
            for ind in range(len(x)):
                value = str(x[ind])
                if value.isnumeric() == True:
                    valueInAge = df['Age'][ind]
                    valueInAge = str(valueInAge)
                    if valueInAge.isnumeric() == False:
                        valueInAge = valueInAge.lower().replace(" ", "")

                    else:
                        print('Do Nothing as age column value is other than alphabates', ind)
                    value = valueInAge
                else:
                    value = value.lower().replace(" ", "")
                value = FinalValue(value)
                x[ind] = value

            df[colname] = x
            print(df[colname].unique())
            print(df[colname].isnull().sum())
            print(df[colname].value_counts())
        else:
            print('Column name Mismatched')


preProcessFile('./Datasets/Form-B-Subset.xlsx')
