import matplotlib as mt
import numpy as np

#-----------------------------------------------------
# Statistics:
def ex1():
    arr = np.random.randint(low=1, high=101, size=20)
    med = np.median(arr)
    avg = np.mean(arr)
    std = np.std(arr)
    ret_str = "array:  {}\nmedian: {}\naverage: {}\nstandard deviation: {}".format(str(arr), str(med), str(avg), str(std))
    return ret_str

#-----------------------------------------------------
# Operations:
def ex2():
    arr1 = np.random.rand(15)+4
    arr2 = np.random.uniform(low=5, high=7,size=20)
    ret_str = "array 1:\n"+str(arr1)+ "\n\narray 2:\n" +str(arr2)
    return ret_str

#-----------------------------------------------------
# Sorting:
def ex3():
    arr = np.random.randint(10,21,15)
    arr2 = np.sort(arr)
    ret_str = "array:\n"+str(arr)+ "\n\nsorted array:\n"+str(arr2)
    return ret_str

#-----------------------------------------------------
# Filters:
def ex4():
    arr = np.random.randint(1,101,36).reshape(6,6)
    odds = arr[np.where(arr % 2 != 0)]
    arr2 = np.copy(arr)
    arr2[np.where(arr % 2 != 0)] = -1
    bin_arr = np.random.randint(0,2,20)
    bin_arr[np.where(bin_arr == 1)] = -1
    ret_str = "array:\n{}\n\nodd numbers:\n{}\n\n" \
              "array with odds replaced:\n{}\n\nbinary 1's replaced array:\n{}".format(str(arr),
                                                                                       str(odds), str(arr2), str(bin_arr))
    return ret_str

def ex5():
    arr = np.array([[10, 12,  3, 12],
       [ 3,  5, 19, 14],
       [ 4,  3,  5,  4],
       [ 7, 15, 13, 10],
       [15,  4,  4,  9],
       [11,  5,  9,  8],
       [10, 16,  9,  4],
       [14, 15,  8,  6],
       [12, 10, 19, 17],
       [ 3, 12, 13,  9],
       [ 6, 17, 16, 17],
       [12, 19, 15, 18],
       [ 6, 13, 16, 13],
       [ 9,  9, 19,  9],
       [ 5, 10,  5, 19],
       [15, 16, 13, 17],
       [ 5,  5,  7,  3],
       [16,  7, 10, 16],
       [11, 19,  5, 14],
       [15, 14, 12,  4]])
    max_columns = arr.max(0)
    two_cols = arr[:, [0,3]]
    less_6 = np.sum([np.any(a=two_cols[i,:]<6) for i in range(len(arr))])
    avg = np.mean(a=arr,axis=0)
    avg = np.sort(avg)
    arr = arr.astype('float')
    arr[-3::,:] *= 0.9
    b = np.array([16,  4, 18, 19, 14,  9, 11,  3, 18,  4, 17,  7,  5,  4,  5, 16, 10, 11, 13, 16])\
        .astype('float').reshape(20,1)
    new_arr = np.append(arr, b, 1)
    std = np.std(new_arr[:, [0,1,3,4]])
    ret_str = "{7} 1. {7}{0}{1}{0}{7} 2. {7}\n{2}{0}{7} 3. {7}\n{3}{0}{7} 4. {7}{0}{4}{0}{7} 5. {7}{0}{5}{0}{7} 5.1 {7}\n{6}"\
        .format("\n\n",max_columns, less_6, avg[-2],arr, new_arr,std,"~~~~")
    return ret_str

# print(ex1())
# print(ex2())
# print(ex3())
# print(ex4())
# print(ex5())
