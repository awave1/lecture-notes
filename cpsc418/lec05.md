# Entropy, Product Ciphers, Block Ciphers

**Outline**:
* Entropy
* Product Ciphers
* Error Propagation
* Block Ciphers
* The Data Encryption Standard
    * Triple DES
* History Post-DES


> Entropy: The average amount of uncertainty. 0 entropy == certainty

## Entropy
Let $x$ be a random variable taking on the values $x_1, x_2, ..., x_n$ with a probability distribution:

$$
p(x_1), p(x_2), ...,p(x_n) \space where \space \sum_{i = 1}^{n} p(x_i) = 1
$$

The entropy of $x$ is defined by the weighted average:

$$
H(x) = \sum_{i = 1 \\ p(x_i) \neq 0} p(x_i)
$$
