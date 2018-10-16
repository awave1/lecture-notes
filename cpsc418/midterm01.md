# Midterm 1 - Study Guide

## 01: Introduction, Basic Terminology

**Definitions**:

- **Encrypt, encipher** - to render a messasge unintelligible except to the intended recipient
- **Decrypt, decipher** - to transform an encrypted message back into its unencrypted form
- **Plaintext** - the message or data to be encrypted
- **Ciphertext** - The message after encryption
- **Cipher, cryptosystem** - A particular method of encryption, capable of handling arbitrary messages

## 02:Basic Terminology, Classical Ciphers

**Information Security** - Measures to protect information security and information systems from unauthorized access, use, disclosure, disruption, modification or destruction.

Cryptography provides some such measures, but not all.

### Security Objectives

Cryptography provides services, that can achieve security objectives:

- Confidentiality (no one can steal)
- Data integrity (no one can alter it)
- Entity authentication (no one can impersonate)
- Access control (access control)
- Non-repudiation (non-repudiation)

### Security Mechanisms

Cryptographic security mechanisms discussed in this course include:

- Encryption systems (Confidentiality and limited data integrity)
- Hash functions, Message Authentication Codes (data integrity)
- Digital signatures (data origin authentication and non-repudiation)
- Authentication exchange/protocol (for entity authentication and access control)

### Security Attacks

**Security attack** - an action that compromises the security of information.

#### Types of attacks

- **Passive Attacks** - listening, eavesdroping on information without interaction with the system
- **Active Attacks** - interacting with the system, modifying information (changing content, DOS)

Cryptographic protocols should be designed to protect against as many attacks as possible, especially active ones.

### Terminologies

- **Cryptography** - the study of math techniques for providing information security services
- **Cryptanaltysis** - the study of math techniques for attempting to defeat cryptographic security mechanisms
- **Cryptology** - combined fields of cryptography and cryptanalysis
- **Cryptographic primitive** - tool that represents a cryptographuc security mechanism
- **Cryptographic protocol** - an algorithm to be undertaken by two or more entities to achieve a specific security objective
- **Message Space M** - set of all possible messages
- **Ciphertext Space C** - set of all possible encrypted messages
- **Key Space K** - the finite set of possible keys
- **Encryption transformation** - a left invertible map $`E_k: M \to C`$, indexed by some key $`k \in K`$.
- **Decryption transformation** - the left inverse map $`D_k`$ of $`E_k`$, so $`D_k(E_k(m)) = m`$ for all plaintexts $`m \in M`$

**Notes**:

- $`D_k(E_k(m)) = m`$ implies that $`D_k \circ E_k = I`$ is the _identity transformation_ on $`M`$.
- The fact that $`E_k`$ is left-invertible is equivalent to $`E_k`$ is an _injective map_ (i.e. one-to-one).

### The Idea of Encryption and Decryption

Gilles Brassard, the inventor of quantum cryptography, created _Alice_ and _Bob_. More characters joined, notably _Eve_.

The idea:

- A transmitter (Bob) generates a plaintext M to be communicated to a legitimate receiver (Alice) over an insecure channel
- To prevent an eavesdropper (Eve) from learning the content of M, Bob chooses a key $`k`$ and encrypts M with $`E_k`$ to produce the ciphertext $`C = E_k(M)`$.
- C is sent along the insecure channel. When Alice obtains C, she decrypts it by applyting $`D_k`$ to obtain $`M = D_k(C)`$

Encryption functions are first example of a cryptographic primitive.

The assumption is that $`E_k`$ and $`D_k`$ are not secret, but $`K`$ is.

### Shift cipher

- **Encryption** - $`E_{k}(m) \equiv m + k \mod 26`$
- **Decryption** - $`D_{k}(c) \equiv c - k \mod 26`$

Main problem of **shift cipher**: very small keyspace ($`|K| = 26`$). Falls to a brute force attack.

### Symmetric Cryptosystems

A **symmetric cryptosystem** consists of the following:

- A finite non-empty set $`M`$ called the plaintext space
- A finite non-empty set $`C`$ called the ciphertext space
- A finite non-empty set $`K`$ called the key space
- A single parameter family $`\{E_k\}_{k \in K}`$ of injective transormations:
  - $`E_k: M \to C`$ via $`m \mapsto c := E_k(m)`$ called encryption functions.
  - The left inverse of $`E_k`$, denoted $`D_k`$ is called the corresponding decryption function: $`D_k(E_k(m)) = m`$ for all $`m \in M`$ and $`k \in K`$.

### Key Channel

Key channels should be absolutely secure from the source to the transmitter. In the real world it is expensive.

Key channel can be dispensed. Why bother encrypting when secure channel exists?

- Time-shifting convinience - might use it later when the channel may not be available
- Speed, bandwidth - the secure channel may be slow or limited bitrate
- Cost - the secure channel may be expensive
- Feasibility - the secure channel may be impractical

### Goals of an attacker

- Deduce the key or portions of it **passive**
- Deduce one or more plaintexts or portions **passive**
- Modify a message **active**
- Replay a message **active**
- Impersonate another entity **active**

### Passive attacks on cryptosystems

- **Ciphertext Only Attack (COA)** - adversary has only ciphertext, but no plaintext
- **Known Plaintext Attack (KPA)** - adversary has some plaintext and corresponding ciphertext

**Note**: Adversary doesn't interact with the system and has no control over the text they are given.

### Active attacks on cryptosystems

- **Chosen Plaintext Attack (CPA)** - adversary chooses some plaintext (independently of the ciphertext that needs to be decrypted) and obtains the corresponding ciphertext.
- **Adaptive CPA** - adversary's choice of plaintext may depend on the ciphertext and on ciphertexts recieved from previous requests.
- **Chosen Ciphertext Attack (CCA1)** - adversary chooses some ciphertext (independently of the ciphertext that needs to be decrypted) and obtains corresponding plaintext.
- **Adaptive CCA (CCA2)** - adversary's choice of ciphertext may depend on the ciphertext that needs to be decrypted and on plaintexts received from previous requests. Adversary is not allowed to choose the ciphertext to decrypt.

CCA may refer to CCA1 or CCA2.

A good/secure cryptosystem should be secure against adaptive CCA's. Some attacks that are not protected by cryptography:

- Side Channel Attacks: exploit physical aspect of the cryptosystem.
- Clandestine Attack: bribe, blackmail.

### Notions of Security

#### Kerckhoff's Principle

**Kerckhoff's Principle** - The security of a cryptosystem should depend upon knowledge of the **key**, not of the method.

It implies that a cipher should be open and still be secure againsts everyone else and its own designer.

### Measures of security

Listed from strongest to weakest:

- **Unconditional security** - can an adversary with unlimited computing power defeat the system?
- **Provable Security** - breaking the system can be reduced (mathematically) to another, supposedly difficult problem: e.g. integer factorization
- **Computational Security** - does the perceived amount of computing power necessary to break the system (using the best known method) exceed the available computing power of the attacker.
- **Ad-hoc security** - security is proved via series of convincing arguments that every successful attack is impractical.

### Classical Ciphers

- **Substitution cipher** - a cipher for which encryption replaces each plaintext symbol by some ciphertext symbol without changing the order of the plaintext symbols.
- **Transposition cipher** - a cipher in which the ciphertext is a rearrangement (i.e. permutation) of the plaintext symbols.

#### Substitution ciphers

- **Monoalphabetic ciphers** - A substitution cipher that uses a single ciphertext alphabet in the replacement of the plaintext characters.
- **Polyalphabetic substitution ciphers** - a substitution cipher in which multiple cipher alphabets are used in the replacement of the plaintext characters.

Simplest example of monoalphabetic cipher is **shift cipher**.

###### Polyalphabetical

**Polyalphabetic substitution cipher** - a substitution cipher in which several cipher alphabets are used in the replacement of the plaintext characters.

###### Viginere cipher

- **Encryption**: The key represents column in the table. The ciphertext letter is located at the intersection of this column and the row given by the corresponding plaintext letter.
- **Decryption**: look up a ciphertext letter in the column given by the key. The corresponding plaintext letter is located at the beginning of that row.

Substitution ciphers are insecure:

- Highly vulnerable to KPA's. Each portion of corresponding plaintext and ciphertext reveals some of the sipher
- Each plaintext letter is encrypted to the same ciphertext letter
- Redundancy in any language yeilds the key, given a sufficient amount of ciphertext (**COA**).

**Code**: A technique by which words or letter combinations are replaced by a set of predetermined codewords.

###### Cryptanaltysis of Vigenere

1. Determine the number n of cipher alphabets (length of the key word), using kappa text or Kasiski's factoring method.
2. Once n is known, consider $`1 \leq i \leq n`$ the $`i^{th}`$ subtext considering of the ciphertext letters in positions $`i, i + n, i + 2n, ...`$

- Each of these is simply text encrypted via a shift cipher whose key is the $`i^{th}`$ letter in the Vigenere key word.
- Cryptanalyze each letter

**Other poly. sub. ciphers**:

- Beauford cipher - slight variant on Vigenere
- Mixed Vigenere - works with a Vigenere tableau in which the columns are scrambled according to some key word. Harder to cryptanalyze -> need to use _symmetry of position_.
- Coherent Running Key cipher - like vigenere, but with a running (very long) key usually taken from available text. Still fals under frequency analysis.

#### Transposition ciphers

- **Transposition cipher** - a rearrangement of the plaintext letters
- **Route cipher** - a Transposition cipher where the plaintext is arranged in some geometric figure and the ciphertext is obtained by rearranging the plaintext according to some route through the figure.
- **Columnar Transposition** - the message is arranged horizontally in a rectangele. The key is used to generate a permutation of the columns. The ciphertext is read vertically from the permuted columns.

##### Cryptanalysis of Columnar Transposition

Vulnerable to a COA:

- guess the dimensions of the rectangle
- determine the order of the columns via frequency counts. Place columns adjacent to each other if they pronounce common letter pairs.

## 02: Perfect Secrecy, One-Time Pad

### Information theory

**Information theory** measures the amount of information conveyed by a piece of data. It captures how much partial information you need to have in order to obtain full information.

### Probability Theory

A **sample space** - a finite set X whose elements are called outcomes. Probability distribution on X - a complete set of probabilities:

```math
\sigma^{n}_{i = 1} p(x_i) = 1
```

**Random variable** - a pair x consisting of a sample space X and a probability distribution p on X. The (a priori) probability that X takes on the value $`x \in X`$ is denoted by p(X = x) or p(x).

#### Joint and Conditional probability

- **Joint probability** - p(x, y) where p(X = x) and p(Y = y)
- **Conditional probability** - p(x|y) probability that p(x) given that p(y).

Related as follows:

```math
p(x,y) = p(x|y)p(y)
```

#### Bayes' Theorem

**Bayes' Theorem** - if p(y) > 0, then:

```math
p(x|y) = \frac{p(x)p(y|x)}{p(y)}
```

**Proof**: p(x, y) = p(y, x), so p(x|y)p(y) = p(y|x)p(x). now divide by p(y).

#### Independence

Two random variables X, Y are independent if p(x, y) = p(x)p(y) for all $`x \in X`$ and $`y \in Y`$.

X and Y are independent iff p(x|y) = p(x) for all $`x \in X`$, $`y \in Y`$ with p(y) > 0.

### Perfect Secrecy

**Perfect secrecy** - a cryptosystem provides **perfect secrecy** if $`p(m|c) = p(m)`$ for all $`m \in M`$ and $`c \in C`$ with $`p(c) > 0`$.

Formally, perfect secrecy means exactly that the random variables on $`M`$ and $`C`$ care independent. Informally, this implies that knowing hte ciphertext $`c`$ gives us no information about $`m`$.

The probabilities $`p(m|c)`$ and $`p(m)`$ are hard to quantify. Bayes' theorem relates these quantities to $`p(c|m)`$ and $`p(c)`$ and these probabilities turn out easier to quantify..

#### Equiv. Definition

A cryptosystem provides perfect secrecy iff $`p(c|m) = p(c)`$ for all $`m \in M`$, $`c \in C`$ with $`p(m) > 0`$ and $`p(c) > 0`$.

**Proof**: let $`m \in M`$ and $`c \in C`$ with $`p(c) > 0`$. If $`p(m) = 0`$ then $`p(m|c) = 0`$. Suppose $`p(m) > 0`$, therefore:

```math
p(c|m) = \frac{p(c)p(m|c)}{p(m)}
```

so $`p(c|m) = p(c)`$ iff perfect secrecy means exavtly that $`p(m|c) = p(m)`$, which is the case iff $`p(c|m) = p(c)`$.

### Computing p(c|m) and p(c)

For any message $`m \in M`$:

```math
p(c|m) = \sigma_{E_k(m) = c} p(k)
```

$`p(c|m)`$ is the sum of probabilities $`p(k)`$ over keys $`k \in K`$ that encipher m to c.

#### computing p(c)

For a key $`k`$ and ciphertext $`c \in E_k(M)`$, consider $`p(D_k(c))`$ that $`M = D_k (c)`$ was sent, then:

```math
p(c) = \sigma_{c \in E_k (M)} p(k)p(D_k (c))
```

That is, $`p(c)`$ is the sum of probabilities over all those keys $`k \in K`$ under which $`c`$ has a decryption under key $`k`$, each weighted by the probability that $`k`$ was chosen.

### Conditions for perfect secrecy

If a cryptosystem has perfect secrecy, then $`|K| \geq |M|`$.

Suppose $`|K| < |M|`$:

- pick $`c`$ with $`p(c) > 0`$
- since $`|K| < |M|`$, there is some message $`m`$ that has no key $`k`$ that encrypts $`m`$ to $`c`$.
- this means that the sum defining $`p(c|m)`$ is empty, so $`p(c|m) = 0`$
- since $`p(c) > 0`$, we have no perfect secrecy

Consider a cryptosystem where keys ar ebit strings (0s and 1s) of some length $`k`$ and messages are bit string of some length $`m`$. Then $`|K| = 2^k`$ and $`|M| = 2^m`$, The throrem shows that in order for such system to provide perfect secrecy, we must have $`k \geq m`$ => keys must be as long as messages.

### One-time pad

$`M = C = K = \{0, 1\} ^n`$, $`n \in \N`$.
- **Encryption** of $`m \in \{0, 1\}^n`$ under key $`k \in \{0, 1\}^n`$ is bitwise XOR: $`c = m \oplus k`$.
- **Decryption**: $`m = c \oplus k`$.

The one-time pad provides perfect secrecy if each key is chosen with equal likelihood. Under this assumption, each ciphertext occurs with equal likelihood (regardless of the probability distribution on the plaintext space).

This means that in one-time pad, any given ciphertext can be decrypted to any plaintext with qual likelihood. There's no distinguished (meaningful) decryption. Exhaustive search doesn't help.

#### Cryptanaltysis

It is imperative that each key is only used once:

- falls to a KPA: if a plaintext/ciphertext pair (M, C) is known, then the key is $`k = \oplus c`$.
- suppose the key is use4d twice: $`c_1 = m_1 \oplus k`$, $`c_2 = m_2 \oplus k`$, therefore $`c_1 \oplus c_2 = m_1 \oplus m_2`$

For the same reason we can't use shorter keys and reuse portions of them. Keys _must_ be chosen randomly and at least as long as messages. This makes the one time pad impractical.

#### Issues

- Requires random key which is as long as message
- each key can be used only once

One time schemes are used when perfect secrecy is crucial and precticality is less of a concern.

Given a pair $`(m, c)`$, and $`c = m \oplus k`$, and $`k`$ is unknown, $`k`$ can be found:

```math
k = m \oplus c
```
 
### Encodings

Measured by the average number of bits needed to encode all possible messages in optimal prefix-free encoding:

- optimaal - the avg number of bits is as small as possible
- prefix free - no code word is the beginning of another code word

The amt of information in an outcome is measured by the entropy of the outcome.

## 03: Entropy, Product Ciphers, Block Ciphers

### Entropy

Let x be a random variable, with probability distribution $`p(x_1), p(x_2), ...`$:

```math
\sum^{n}_{i = 1} p(x_i) = 1
```

The entropy of x is defined by the weighted average:

```math
H(x) = \sum^{n}_{i = 1} p(x_i) \log_2 (\frac{1}{p(x_i)}) = - \sum^{n}_{i = 1} p(x_i) \log_2 (p(x_i))
```

The weighted H(x) is the expected number of biits in an optimal encoding of x. if x1, x2, ... xn are outcomes, occuring with probabilities p(xn), then H(x) is the amount of information **discovered abouut these outcomes**.

#### Extremal Entropy

H(x) is maximized iff all outcomes are equally likely. That is for any n, H(x) = log2(n) is maximal iff p(x_i) = 1/n for all $`1 \leq i \leq n`$.

H(x) is minimized iff p(x_i) = 1 for **exactly one** i p(x_j) = 0 for all j != i.

Intuitively, H(x) decreases as the distribution of messages becomes increasingly skewed.

#### Entropy of keys

For a key space $`K`$, $`H(K)`$ measures the amount of partial information that must be learned about a key to actually uncover it (e.g. number of bits that must be guessed correctly to recover the whole key).

For a $`k-bit`$ key, the best scenario is that all $`k`$ bits must be guessed correctly to know the whole key (i.e. no amt of partial information reveals the key, only full information does).

- Entropy of the random variable on the keyspace **should be maximal**
- Prev. theorem: happens exactly when each key is equally likely
- best to select keys in order to give away as little as possible is to choose them with equal likelihood (uniformly at random).

Cryptosystems are assessed by their key entropy, which ideally should just be the key length in bits (i.e. maximal)

#### Stuff Learned

- security level (i.e. key entropy) of a cryptosystem may not tell the whole story in some applications and may in fact convey a false sense of security
- small message spaces are problematic
- the concept of indistinguishability is crucial in the content of security

### Product Ciphers

The product of two ciphers is the result of applying one cipher followed by the other.

aka multiple encryption or superencipherment.

_Note_: all modern symmetric key ciphers in use are product ciphers.

#### Properties

If different ciphers are used in a product cipher, ciphertext on one cipher need to have the correct format to be plaintexts for the next cipher to be applied. -> Composition of encryption maps.

#### Caveat

The product of two substitution ciphers is a substitution cipher.

ususally multiple encryption under different keys provides no extra security.

#### Confusion and diffusion

- **Confusion** - make the relationship between the key and ciphertext as complex as possible (accomplished by applying substitutions or **S-boxes**).
- **Diffuusion** - dissipate the statistical properties of the plaintext across teh ciphertext (accomplished by applying transposition or **P-boxes**).

#### Examples

- IBM Lucifer - used permutations (transpositions) on large blocks for mixing transformation, and substitution on small blocks for confusion. used p-boxes and s-boxes, (permutations and substitutions).

The Lucifer system simply consisted of a number of P and S boxes in alternation.

#### Error propagation

- **Error propagation** - the degree to which a change in the input leads to changes in the output
- **Avalanche effect** - changing one input bit leads to significant changes in the output

Good error propagation is desirable property of a cryptosystem (user can tell if a message has been modified).

### Block ciphers

All modern ciphers in use are block ciphers.

**Block cipher** - encrypts plaintext blocks of some fixed length to ciphertext blocks of some fixed (possibly different) length.

Ususally a message m will be larger that the plaintext block length and must be divided into a series of message blocks: M1, M2, ... Mn. A block vipher operates a block at a time.

### DES

- developed in FIPS by IBM
- Block cipher that encrypts 64bits plaintext int o 64bit ciphertext using 64bit keys (**Note**: 8 of the key bits are parity bits, resulting in 56 actual bits of the key).
- $`M = C = \{0, 1\}^{64}`$ and $`K = \{0, 1\}^56`$
- Algorithm consists of 16 rounds of permutations and substitutions

#### Multiple DES encryption

- double DES is not secure, but twice as slow

##### Triple DES

- Use 3 successive DES operations: $`c = DES_{k1}(DES^{-1}_{k2}(DES_{k3}(m)))`$.
- Advantages
  - same as single key, if $`k2 = k1`$ or $`k2 = k3`$
  - exhaustive search has complexity of $`2^{112}`$ via meet in the middle attack but with a 168 bit key and a factor of 3 in speed
  - can use $`k1 = k3`$ with no loss of security
  - no other known practical attacks
- Disadvantage: 3 times slower than DES while only doubling the key size

### AES Competition

Requirements for new cipher:

- possible key sizes of 128, 192, 256 bits
- plaintexts and ciphertexts of 128 bits
- should work on different hardware
- fast
- secure
- availability

**Criteria**

- resistance to all known attacks
- speed and code compactness on diff platforms
- simple design

#### Rijndael

Uses two different types on arithmetic:

- arithmetic on bytes (8 bit vectors, elements of finite field $`GF(2^8)`$ of 256 elements)
- 4 byte vectors (polynomial operations over $`GC(2^8)`$)

The algorithm uses addition, multiplication and inversion on bytes as well as addition and multiplication of 4 byte vectors.

Rijndael is a **product cipher**, but not a Feistel cipher, like DES. Instead it has 3 layers per round:

1. linear mixing layer (ShiftRows, transposition and MixColumns, a linear transformation; for diffusion over multiple rounds)
2. non-linear layer (SubBytes, substitution done with S-box)
3. key addition layer (AddRoundKey, XOR with key)

## 04: Advanced Encryption Standard

### Arithmetic on Bytes and 4 byte Vectors

Consider a byte $`b = (b_7, b_6, b_5, ..., b_0)`$ (an 8 bit vector) as a polynomial with coefficients $`\{0, 1\}`$:

```math
b \mapsto b(x) = b_{7}x^7 + b_{6}x^6 + ... + b_{1}x + b_0
```

Under addition, modular multiplication, inversion, polynomials of degree $`\leq 7`$ with coefficients in $`\{0, 1\}`$\* form the field $`GF(2^8)`$.

#### Addition

Polynomial addition done by taking XOR of coefficients.

![01.png](cpsc418/img/lec05/01.png)

The sum of two polynomials taken in this manner yeilds another polynomial of degree $`\leg 7`$. Component-wise XOR of bytes is identified with this addition operation on polynomials.

#### Modular Multiplication

Polynomial multiplication (coefficients are in $`\{0, 1\}`$) modulo:

```math
m(x) = x^8 + x^4 + x^3 + x + 1
```

> remainder when dividing by m(x), analogous to modulo arithmetic with integers

The remainder when dividing by a degree 8 polynomial will have degree $`\leq 7`$. Thus the product of two bytes is associated with the product of their polynomial equivalents modulo $`m(x)`$.

**Note**: $`m(x)`$ is the lexicographically first polynomial that is irreducable over $`GF(2)`$ i.e. does not split in two polynomials of smaller degree with coefficients in $`\{0, 1\}`$.

#### Inversion

$`b(x)^{-1}`$, the inverse of $`b(x) = (b_7x^7, b_6x^6, ..., b_1x + b_0)`$ is the polynomial of degree $`\leq 7`$with coefficients in $`\{0, 1\}`$ such that:

```math
b(x)b(x)^{-1} \equiv 1 \pmod m(x)
```

This is analogous to the case of integer arithmetic modulo $`n`$. The inverse of the byte $`b = (b_7, b_6, b_5, ..., b_0)`$ is the byte associated with the inverse of $`b(x) = (b_7x^7, b_6x^6, ..., b_1x + b_0)`$.

Rijndael uses inverse as above in **SubByte** operation.

#### Arithmetic on 4 byte vectors

### Rijndael Algorithm

### AES Key Schedule and Decryption

### Strengths and Weaknesses of Rijndael

## 05: Attacks on Block Ciphers

## Discrete Math Topics

### Congruences & Integer modular arithmetic

### Modular arithemtic on polynomials with binary coefficients

### Proof techniques
