
import sympy
from sympy import Max
from sympy.abc import x

#function that finds the maximum area (integral value)
# between all the polynoms in input

def mymaxint(polys):
    x = sympy.Symbol('x')

    # make sure valid input
    try:
        ans = sympy.integrate(Max(*polys), (x, -1, 1))
        return float(ans)
    except:
        print("The input is not correct")

# running examples
if __name__ == '__main__':
    polyExample = [(0.545634758253165 - x) * (x + 0.454365241746835) + 10,
                   (0.706936695145996 - x) * (x + 0.293063304854004) + 10,
                   (0.599303627947032 - x) * (x + 0.400696372052968) + 10]

    print(mymaxint(polyExample))

