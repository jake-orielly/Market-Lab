def filter_df(df,column,comparator,value):
    if comparator == '>':
        matching = df[column] > comparator
    elif comparator == '>=':
        matching = df[column] >= comparator
    elif comparator == '<':
        matching = df[column] < comparator
    elif comparator == '<=':
        matching = df[column] <= comparator
    elif comparator == '==':
        matching = df[column] == comparator

    return df[matching]