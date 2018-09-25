# Perfect Secrecy, One-Time Pad
```
@TODO: fix formatting
```

> Note: will need probablity theory

Outline:
* Information Theory
    * Intro
    * Probability Theory
    * Perfect Secrecy
* Computing $`p(C|M)`$ and $`p(C)`$

## Information Theory
*Claude Shannon* is widely hailed as the "father of information theory".
* Seminal work in the late 1940s and early 50s in this field
* Credidted with turning cryptography into a scientific discipline
* In addition, modern satellite transmition would not be possible without his work

**Information theory** measures the amount of the information conveyed by a piece of data. It captures how much partialinformation you need to have in order to obtain full information.

### Partial Information
For example, partial information reveals the full word or phrase in:
* abbreviations - lol
* contractions - I've
* Ommitted vowels - bstbll
* Glypths - emojis

How much partiall information is enough? e.g. "bll" could mean "ball", "bell", "bill" ...

### Definitions for Probablity Theory
**Sample Space** - a finite set $`X = \{X_1, X_2, ... X_n\}`$, whose elements are called *outcomes*

*Probability distribution* on $`X`$ - a complete set of probabilities, i.e.
```math
p(X_1), p(X_2),...,p(X_n) \ge 0 \space with \space \sum_{i=1}^{n} p(X_i) = 1
```

*Random variable* - a pair $`x`$ consisting of a sample space $`X`$ and a probability distribution $`p \space on \space X`$. The (*a priori*) *probability* that $`x`$ takes on the value $`x \in X`$ is denoted by $`p(X = x)`$ or simply $`p(x)`$.

#### Joint and Conditional Probability
Let $`x`$ and $`y`$ be random variables, $`x \in X`$, and $`y \in Y`$.

**Definition**:

*Joint Probability* $`p(x, y)`$ is the probability that $`p(X = x)`$ and $`p(Y = y)`$.

*Conditional Probability* $`p(x|y)`$ is the probability that $`p(X = x)`$ given that $`p(Y = y)`$.

Joint and conditional probabilities are related as follows:

```math
p(x, y) = p(x|y)p(y)
```

#### Bayes' Theorem
If $`p(y) > 0`$, then:

```math
p(x|y) = \frac{p(x)p(y|x)}{p(y)}
```

##### Proof
```math
p(x, y) = p(y, x) \newline
p(x | y)p(x) = p(y | x)p(x) \newline
\frac{p(x|y)p(y)}{p(x)} = p(y|x) \newline
```

> Assuming $`p(y) \not = 0`$

#### Independence
Two random variables $`x`$, $`y`$ are *independent* if $`p(x, y) = p(x)p(y) \space for \space all \space x \in X \space and \space y | Y`$.

##### Example
A fair coin toss is modeled by a random variable on the sample space $`X = \{heads, tails\}`$ so that $`p(heads) = p(tails) = \frac{1}{2}`$. Two fair coin tosses in a row represent independent events as each of the 4 possible outcomes has (joint) probability of $`\frac{1}{4}`$.

##### Corollary 2
X and Y are independent if and only if of p(x|y) = p(x) for all x \in X, y \in Y with p(y) > 0

## Idea of Perfect Secrecy
The notion of *unconditional security*, which requires that an adversary with unlimited computing power cannot defeat the system. relates to *perfect secrecy*.

Intuitively, for perfect secrecy, ciphertexts should reveal no information whatsoever about plaintexts.

Theoretically, unbreakable.

### Setup
We consider the following three probability distributions:
* A random variable on the message space $`M`$; plaintexts $`m`$ occur with probabilities $`p(m)`$ such that $`\sum_{m \in M} p(m) = 1`$.
* A random variable on the ciphertext space $`C`$; ciphertexts $`c`$ occur with probabilities $`p(c)`$ such that $`\sum_{c \in C} p(c) = 1`$.
* A random variable on the key space $`K`$; keys $`k`$ occur with probabilities $`p(k)`$ such that $`\sum_{k \in K} p(k) = 1`$.

We assume that the random variables on $`K`$ and $`M`$ are independent as keys are usually chosen before the plaintext is ever seen.
* Most of the time, each key is selected with equal likelyhood $`\frac{1}{|K|}`$, regardless of the nature of the messages to be encrypted.

### Notation
We consider the following probabilities
* $`p(m)`$ - (a priori) probability that plaintext $`m`$ is sent
* $`p(c)`$ - probability that ciphertext $`c`$ was received
* $`p(m | c)`$ - (a posteriori) probability that plaintext $`m`$ was sent, given that ciphertext $`c`$ was received
* $`p(c | m)`$ - probability that ciphertext $`c`$ was received, given that plaintext $`m`$ was sent
* $`p(k)`$ - probability that the key $`k`$ was chosen

## Perfect Secrecy
A cryptosystem provides perfect secrecy if $`p(m|c) = p(m)`$ for all $`m \in M`$ and $`c \in C`$ with $`p(c) > 0`$

```
@TODO: add notes from wednesday
```

### Necessary Condition for Perfect Secrecy
Mathematically can be correct, but impracticall

## One-Time Pad

### Bitwise XOR

### Security of the One Time Pad
**Theorem**: The one-time pad provides perfect secrecy if each key is chosen with equal likelihood. Under this assumption, each ciphertext occurs with equal likelihood (regardless of the probability distribution on the plaintext space).

This means that in the one-time pad, any given ciphertext can be decrypted to *any* plaintext with equal likelihood (definition of perfect secrecy). There's no "distinguished" (e.g. meaningful) decryption. Se even exhaustive search doesn't help.


