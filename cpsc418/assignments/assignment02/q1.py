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


def left_rotate(n, d = 8, bits = 32):
    """
    left rotate n by d bits
    """

    return (n << d) | (n >> (bits - d))


def format_binary(str_bin, n = 8):
    return [str_bin[i:i+n] for i in range(0, len(str_bin), n)]


def main():
    print("q1.a.1")
    polys = sorted(list_binary_polynomials(3))
    for p in polys:
        print(p)


if __name__ == "__main__":
    main()
