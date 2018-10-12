# Cryptanalysis of Block Ciphers, Stream Ciphers, Modes of Operation for Block Ciphers

## Exhaustive Attacks on Block Ciphers

### Exhaustive Search

Brute-force search for the key is the simplest attack on a block cipher. Set $`N = |K|`$.

**Simple exhaustive search** (COA) - requires $`|K|`$ encryptions.

### Hellman's Time-memory Tradeoff

KPA that shortens search time by using a lot of memory.

- The attacker knows a plaintext/ciphertext pair (M_0, C_0)
- The goal is to find

### Meet-in-the-Middle Attack on Double Encryption

KPA on double encryption:

- Adversary has two known plaintext/ciphertext pairs (m_1, c_1) and (m_2, c_2)
- Double encryption, so $`c_i = E_{k_1} (E_{k_2}(m_i))`$ for $`i = 1, 2`$ and two unknown keys $`k_1, k_2`$

Compute a table of every $`E_k(m_i)`$. Decrypt $`C_1`$ with every key $`K`$.

### Linear Cryptanalysis

```
@todo: finish
```

#### Attacking Linear Cryptosystems

### Algebraic Attacks
