import pandas as pd


def preProcessFile(filename):
    df = pd.read_excel(filename)
    for column in df.columns:
        colname = 'Sex'
        if colname in df.columns:
            def normalizeData(value):
                value = str(value)
                value = value.lower().replace(" ", "")
                if value == 'f' or value == 'female':
                    return 'F'
                elif value == 'm' or value == 'male':
                    return 'M'
                else:
                    return 'NA'

            x = df[colname]
            x = x.fillna("NA")
            x = x.apply(normalizeData)
            df[colname] = x
            return print(df[colname].unique())
        else:
            return 'Column mismatch'


preProcessFile('./Datasets/Form-B-Subset.xlsx')
