import numpy as np


# ============================
# Part 1: Creating Arrays

def ex1_a():
    return np.eye(3)


def ex1_b():
    return np.zeros((4, 5))


def ex2_a():
    return np.random.rand(20)


def ex2_b():
    return np.linspace(1, 20)


def ex2_c():
    return np.random.randint(low=10, high=20, size=20)


def ex3_a():
    return np.arange(10, 21, 2)


def ex3_b():
    return np.arange(0, 10, 1).reshape(2, 5)


def ex4():
    return np.random.rand(24).reshape(3, 4, 2)


def ex5_a():
    return np.eye(4)


def ex5_b():
    return np.zeros(20).reshape(4, 5)


# ======================================
# Part 2: Accessing Values

def ex6():
    mat = np.random.randint(low=50, high=100, size=25).reshape(5, 5)
    ex_a = mat[-1, -1]
    ex_b = mat[2, 1]
    ex_c = mat[0, [1, 2]]
    ex_d = mat[-2, [0, 3]]
    ex_e = mat[3, :3]
    return "mat:\n\n{}\n\n1: {}  2:  {}  3:  {}  4:  {}  5:  {}  ".format(mat, ex_a, ex_b, ex_c, ex_d, ex_e)


def ex7():
    mat = np.arange(1, 51).reshape(5, 10)
    ex_a = mat[1]
    ex_b = mat[[0, -1]]
    ex_c = mat[-3:]
    ex_d = mat[[0, 2, 4], :2]
    ex_e = mat[:, [1, -1]]
    return "mat:\n\n{}\n\n1:\n{}\n2:\n{}\n3:\n{}\n4:\n{}\n5:\n{}  ".format(mat, ex_a, ex_b, ex_c, ex_d, ex_e)


# ============================================
# Part 3: Updating Arrays


def ex8():
    mat = np.ones(18).reshape(3, 6)
    mat[-2, :] = 2
    mat[:2, :2] = 0
    mat[:, [3, 4]] = 5
    return mat


def ex9():
    mat = np.random.randint(low=1, high=10, size=18).reshape(3, 3, 2)
    mat[:, :, 1] = -1
    return mat


# ======================================
# Extensions:


def ex10():
    mat = np.arange(25, 50).reshape(5, 5)
    print(mat)
    mat[:, [1, 2]] = mat[:, [2, 1]]
    print(mat)
    mat[[0, -1], :] = mat[[-1, 0], :]
    return mat


def ex11():
    return np.random.uniform(low=5, high=10, size=16).reshape(4, 4)

# print(ex1_a())
# print(ex1_b())
# print(ex2_a())
# print(ex2_b())
# print(ex2_c())
# print(ex3_a())
# print(ex3_b())
# print(ex4())
# print(ex5_a())
# print(ex5_b())
# print(ex6())
# print(ex7())
# print(ex8())
# print(ex9())
# print(ex10())
# print(ex11())
