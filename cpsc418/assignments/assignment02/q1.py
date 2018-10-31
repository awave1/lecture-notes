import itertools


def list_binary_polynomials(degree):
    """
    a.i
    """

    possible_bin_polynomials = list(itertools.product([0, 1], repeat=degree + 1))

    result = []

    for poly in possible_bin_polynomials:
        poly_str = []
        for i, x in enumerate(poly):
            if x == 1:
                term = ""
                if i != 0:
                    term = "x^" + str(i)
                else:
                    term = "1"

                poly_str.append(term)
        
        if len(poly_str):
            result.append('+'.join(poly_str[::-1]))

    return result

def a_ii():
    pass

def main():
    polys = sorted(list_binary_polynomials(3))[::-1]
    for p in polys:
       print(p)
    
if __name__ == "__main__":
    main()
