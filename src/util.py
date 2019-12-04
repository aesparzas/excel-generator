from random import randint, random


def snake_case(name):
    return name.lower().replace(' ', '_')


def upper(name):
    return name.upper().replace('_', ' ')


def insert_row(row_number, df, row_value):
    start_upper = 0
    end_upper = row_number
    start_lower = row_number
    end_lower = df.shape[0]
    upper_half = [*range(start_upper, end_upper, 1)]
    lower_half = [*range(start_lower, end_lower, 1)]
    lower_half = [x.__add__(1) for x in lower_half]
    index_ = upper_half + lower_half
    df.index = index_
    df.loc[row_number] = row_value
    df = df.sort_index()
    return df


def field_empty_on_probability(probability, field):
    dice = random(0, 1)
    return field if dice > probability else ''
