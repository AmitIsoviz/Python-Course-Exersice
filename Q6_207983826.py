#https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/



def Answer(T):
    length = len(T)
    # sum formula for all numbers
    sum_num = (length * (length + 1)) // 2
    # sum of square formula
    sum_sq = ((length * (length + 1) * (2 * length + 1)) // 6)

    # take off T[i] and stay with two equations
    for i in range(len(T)):
        sum_num -= T[i]
        sum_sq -= T[i] * T[i]
    double = (sum_num + sum_sq // sum_num) // 2
    missing = double - sum_num
    return double, missing

# run example
if __name__ == '__main__':

    print(Answer((1, 3, 10, 11, 5, 7, 8, 2, 6, 5, 9)))

