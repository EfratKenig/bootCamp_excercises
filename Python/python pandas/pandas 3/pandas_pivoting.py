import numpy as np
import pandas as pd

airbnb_df = pd.read_csv("data.csv")


def ex1():
    # pivot table to show the count of available listings of each neighborhood:
    first_pv_table = airbnb_df.pivot_table(index="neighbourhood_group", values='availability_365',
                                           aggfunc=lambda x: len(x[x > 0]), margins=True)
    # another pivot table to show the average and the standard deviation of the listing prices of each neighborhood:
    second_pv_table = airbnb_df.pivot_table(index="neighbourhood_group", values='price', aggfunc=[np.mean, np.std],
                                            margins=True)
    # concatenate both to show everything together:
    final_piv_table = pd.concat((first_pv_table, second_pv_table), axis=1)
    final_piv_table.columns = ['available_listings', 'average_price', 'std_price']
    return final_piv_table


def ex2():
    pv_table = airbnb_df.pivot_table(index=["neighbourhood_group", "room_type"], values='price', margins=True)
    pv_table = pv_table.round()
    ex2_1 = pv_table['price'].min()
    ex2_2 = pv_table['price'].max()
    ret_str = "Pivot Table:\n" + str(pv_table) + "\n1. Cheapest:\n" + str(ex2_1) + "\n2. Most Expensive:\n" + str(ex2_2)
    return ret_str


def ex3():
    pv_table = airbnb_df.pivot_table(index="neighbourhood_group",
                                     values=["minimum_nights", "availability_365"], margins=True)
    return pv_table


def ex4():
    pv_table = airbnb_df.pivot_table(index="neighbourhood_group",
                                     values=["minimum_nights", "availability_365"], aggfunc='median', margins=True)
    return pv_table


# print(ex1())
# print(ex2())
# print(ex3())
# print(ex4())
