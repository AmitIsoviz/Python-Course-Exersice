# https://www.cut-the-knot.org/nim_theory.shtml

def mynim(A):
    try:
        n =A[0]
        m = A[1]
        k = A[2]
        XOR = (n^m)

        # if k == 1 the output depend on if m+k is even or not
        if k == 1:
            if (m+n)%2 == 0:
                return False
            else:
                return True
        # if one of the towers {n,m} is 0 and k is smaller in 1 from the non-zero value
        # variable, the second will win
        if (k == n-1 and m == 0) or (k == m-1 and n == 0):
            return False

        #XOR = 0 -> SECOND WIN
        # if the XOR in my turn is 0 I can make sure the XOR will be 0 all the time
        # it means equal towers until they will be equally zero
        if XOR == 0:
            return False
        else:
            if (n+m+k) == (2 * max(n, m)) - 1:
                return False
            return True
    except:
        print("The input is not correct")



# run examples
if __name__ == '__main__':

    print(mynim([5,5,3]),mynim([5,4,3]),mynim([5,4,4]),mynim([5,0,4]))
    for i in range(1,10):
        for j in range(1,5):
            for k in range(1,5):
                x = input()
                if x is not None:
                    print(f'mynim([{i},{j},{k}]')
                    print(mynim([i,j,k]))