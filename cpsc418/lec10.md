# Week 8: One-Way Functions and Cryptographic Key Agreement

## One-way functions

**One-way function**: A function $`f`$ that satisfies the following two properties:

1. **Ease of computation**: $`f(x)`$ is easy to evaluate for a given $`x`$
2. **Pre-image resistance**: Given $`y = f(x)`$, it is computationally infeasible to find $`x`$

It is not known whether one way functions exist, but several that are believed to be one-way are used in cryptography.


### Examples

- A **pre image resistant** hash function is a one-way function
- A secure cryptosystem provides a one-way function as follows:
  - Define $`C = f(x) = E_x(M)`$ where $`M`$ is a known plaintextand $`x`$ is a key. Given $`M`$ and $`C`$ (KPA), it should be computationally infeasible to find the key $`x`$.
- If $`p`$ is a large prime $`\approx 2^{1024}`$ and $`g`$ a suitably chosen integer, then the function $`f(x) = g^x` \pmod{p}$ seems to be a one-way function, provided $`p - 1`$ has at least one large prime factor. Computing $`x`$, given $`f(x)`$ and $`g`$ is known as **discrete logarithm problem (DLP)**.

### Application: Access Control

Secure login via one-way functions: Computer stores a table: $`(uid_i, f(P_i))`$ that contains user ids and images of passwords under a one-way function $`f`$ (safer than storing cleartext).

When a user logs in, the user submits the id, and password $`P`$.

The computer generates $`f(P)`$ and checks if $`( uid, f(P) )`$ exists. If it does the access is granted.

## Diffie-Hellman Key Exchange: Idea

Alice and Bob establish a common key over a public channel in a way that it cannot be determined.

Alice and Bob agre on:

- a large prime $`p`$
- an integer $`g`$ with $`1 < g < p`$
- both are public

Modulo is necessary to keep the number bounded.

### Description

- Alice selects $`1 < a < p - 1`$
- Bob selects $`1 < b < p - 1`$
- Alice calculates: $`y_a \equiv g^a \pmod{p}`$
- Bob calculates: $`y_b \equiv g^b \pmod{p}`$
- $`y_a`$ and $`y_b`$ are exchanged through public channel
- Then, Alice computes $`K \equiv y_{b}^{a} \pmod{p}`$ 
- Bob computes $`K \equiv y_{a}^{b} \pmod{p}`$
- Where: $`y_{b}^{a} \equiv (g^b)`^a \equiv (g^b)^a \equiv y_{a}^{b} \pmod{p}$
- Can use the low order 128 bits of $`H(K)`$ for an AES key, where $`H`$ is a cryptographically secure hash function

## Primitive Roots

For any prime $`p`$:

- $`\Z_p = \{0, 1, 2, ..., p - 1\}`$
- $`\Z_{p}^{*} := Z_{p} \ \{0\} = \{1, 2, ..., p - 1\}`$

#### Theorem 1 (Fermat's Little Theorem)

If $`a`$ is an integer and $`p`$ is a prime $`p \nmid a`$, then $`a^{p - 3} \equiv 1 \pmod{p}`$

#### Primitive Root - Definition

For a prime $`p`$, a primitive root of $`p`$ is an integer $`g \in \Z_{p}^{*}`$ such that the smallest positive exponent $`k`$ with $`g^{k} \equiv 1 \pmod{p}`$ is $`p - 1`$.

Mathematically, $`g`$ is a generator of the multiplicative group $`\Z_{p}^{*}`$

### Finding Primitive Roots

Suppose $`p`$ is prime. To obtain a primitive root of $`p`$:

1. Select some $`g \in \Z_{p}^{*}`$
2. Run the primitive root test on $`g`$. If it fails, go back to step 1.

$`g`$ is a primitive root of p iff:

```math
g^{(p - 1)/q} \not\equiv 1 \pmod{p}
```

for every primve factor $`q`$ if $`p - 1`$.

#### Example

### Properties of Primitive Roots

## Discrete Logarithms
