# Advanced Encryption Standard

**Outline**

- Arithmetic on Bytes and 4byte vectors
- The Rijndael algorithm
  - Overview
  - Description of the algorithm
- AES Key Schedule and Decryption
- Strengths and weknesses of Rijndael

## Arithmetic on bytes

Consider a byte $b = (b_7, b_6, ..., b_1, b0)$ (an 8bit vector) as a polynomial with coefficients in $\{0, 1\}$

$$
b \mapto b(x) = b_7x^7 + b_6x^6 + ... + b_1x + b_0
$$

Rijndael makes use of the following operations on bytes, interpreting them as polynomials:

1. Addition
2. Modular multiplication
3. Inversion

Under these operations, polynomials of degree $\leq 7$ with coefficients in $\{0, 1\}$ form the field $GF(2^8)$. By associating bytes with these polynomials, we obtain operation on bytes.

### Addition of bytes in Rijndael

Polynomial addition by taking XOR of coefficients:

```
  bnx^n
+ cnx^n
  --------------
  (bn xor cn)x^n
```

Where $ 7 \leq n \leq 0$a.

The sum of two polynomials taken in this manner yeilds another polynomial of degree $\leq 7$.

### Modular multiplication in Rijndael

Polynomial multiplication (coefficients are in $\{0, 1\}$) modulo

$$
m(x) = x^8 + x^4 + x^3 + x + 1
$$

remainder when dividing by m(x), analogus to modulo arithmetic with ints.

The remainder when dividing by a degree 8 polynomial will have degree $\leq 7$. Thus the "product" of two bytes is associated with the product of their polynomial equivalents modulo $m(x)$.

$m(x)$ is lexicographically first polynomial that is _irreducible_ over $GF(2)$, i.e. does not split into two polynomials of smaller positive degree with coefficients in $\{0, 1\}$.

### Inversion of bytes in Rijndael

## Arithmetic on 4byte vectors

### Operations on 4byte vectors

### Examples of Rijndael arithmetic
