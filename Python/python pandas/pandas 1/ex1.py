import pandas as pd
pets_df = pd.read_csv("lost-found-adoptable-pets.csv")


def ex1():
    ex1_1 = len(pets_df.index)
    ex1_2 = pets_df.tail(3)
    ret_str = "1.\n"+str(ex1_1)+"\n2.\n"+str(ex1_2)
    return ret_str


def ex2():
    ex1_1 = pets_df['animal_type'].value_counts()
    ex1_2 = pets_df.iloc[99]['Animal_Name']
    ex1_3 = pets_df.loc[20:28, ['Current_Location', 'Date']]
    ret_str = "1.\n"+str(ex1_1)+"\n2.\n"+str(ex1_2)+"\n3.\n"+str(ex1_3)
    return ret_str


def ex3():
    ex1_1 = pets_df.loc[1::2, 'Animal_Name':'Animal_Color']
    ex1_2 = pets_df.iloc[:4].loc[:,['Animal_Name','animal_type','Record_Type']]
    ex1_3 = pets_df.iloc[:, 0:5:2]
    ret_str = "1.\n"+str(ex1_1)+"\n2.\n"+str(ex1_2)+"\n3.\n"+str(ex1_3)
    return ret_str


# print(ex1())
# print(ex2())
# print(ex3())
