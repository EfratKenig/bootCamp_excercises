import pandas as pd
airbnb_df = pd.read_csv("AB_NYC_2019.csv")


def ex1():
    professional_hosts = airbnb_df[airbnb_df['calculated_host_listings_count'] > 9][
        ['host_id', 'neighbourhood', 'neighbourhood_group']]
    grouped_table = professional_hosts.groupby('host_id').nunique()
    ex_1 = grouped_table
    ex_2 = grouped_table.describe()
    ex_2 = ex_2.to_string(formatters={
        'neighbourhood': '{:,.2f}'.format,
        'neighbourhood_group': '{:,.2f}'.format
    })
    ret_str = "1. Grouped Table:\n" + str(ex_1) + "\n2. Stats:\n" + str(ex_2)
    return ret_str


def ex2():
    grouped_table = airbnb_df.groupby(airbnb_df['name'].str.contains('cozy'))[['calculated_host_listings_count',
                                                                               'price']]
    ex_1 = grouped_table.agg({'calculated_host_listings_count': 'count',
                              'price': ['median', 'mean']
                              })
    ret_str = "Grouped Table:\n" + str(ex_1)
    return ret_str


def ex3():
    grouped_table = airbnb_df.groupby(['room_type', airbnb_df['name'].str.contains('cozy')])[['calculated_host_listings_count',
                                                                               'price']]
    ex_1 = grouped_table.agg({'calculated_host_listings_count': 'count',
                              'price': ['median', 'mean']
                              })
    ret_str = "Grouped Table:\n" + str(ex_1)
    return ret_str


def ex4():
    # hosts with at least 3 listings:
    new_df = airbnb_df[airbnb_df['calculated_host_listings_count'] > 2][['host_id', 'room_type']]
    grouped_table = new_df.groupby('host_id').nunique()
    ret_str = "Grouped Table:\n" + str(grouped_table)
    return ret_str


# print(ex1())
# print(ex2())
# print(ex3())
# print(ex4())
