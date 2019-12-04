def percentage_total(dataframe, column='total'):
    dataframe['total %'] = dataframe[column].apply(percentage(dataframe[column].sum()))
    return dataframe.set_index('name')


def percentage(total):
    return lambda x: round(100 * float(x) / float(total), 2)


def average(total):
    return lambda x: int(float(x) / float(total))
