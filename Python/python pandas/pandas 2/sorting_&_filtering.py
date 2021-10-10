import numpy as np
import pandas as pd

airbnb_df = pd.read_csv("AB_NYC_2019.csv")


def ex1():
    ex1_1 = airbnb_df.sort_values(by=["price"]).tail(3)
    ex1_2 = airbnb_df['neighbourhood_group'].value_counts()
    ex1_3 = airbnb_df[airbnb_df['neighbourhood_group'] == "Manhattan"]["price"].mean()
    ex1_4 = airbnb_df[airbnb_df['neighbourhood_group'] == "Manhattan"]["price"].describe()
    ret_str = "1.\n" + str(ex1_1) + "\n2.\n" + str(ex1_2) + "\n3.\n" + str(ex1_3) + "\n4.\n" + str(ex1_4)
    return ret_str


def ex2():
    ex1_1 = airbnb_df[((airbnb_df['last_review'].isnull()) | (airbnb_df['last_review'] < "1/1/2019"))]
    updated_df = ex1_1
    ex1_2 = updated_df.sort_values(by=["host_id", "id"])
    ret_str = "1.\n" + str(ex1_1) + "\n2.\n" + str(ex1_2)
    return ret_str


def ex3():
    hosts = airbnb_df[
        ((airbnb_df['neighbourhood_group'] == "Manhattan") | (airbnb_df['neighbourhood_group'] == "Brooklyn"))
        & (airbnb_df['calculated_host_listings_count'] > 9)]
    new_df = pd.DataFrame(
        {"host_id": hosts['host_id'],
         "host_name": hosts['host_name'],
         "number_of_listings": hosts['calculated_host_listings_count']})
    new_df = new_df.sort_values(by=["number_of_listings"], ascending=False)
    new_df = new_df.drop_duplicates()
    return new_df

# print(ex1())
# print(ex2())
# print(ex3())
