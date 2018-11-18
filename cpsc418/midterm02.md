# Midterm 2 - Study Guide

## Modern Symmetric Cryptography

### Purpose of stream ciphers

In contrast to block ciphers, stream ciphers don't trat incoming characters independently:

* encryption $`C_i`$ of plaintext character $`M_i`$ depends on internal state of device
* after encryption, the device changes state according to some rule

### SSC and self-SSC

- SSC: Synchronous Stream Ciphers:
  - State depends only on the previous state, not the input $`M_i`$.
  - $`C_i`$depends only on$`M_i`$and$`i`$, not in$`M_{i-1}, M_{i-2}`$
  - Implemented by boolean logic that should produce a pseudo random sequence $`R_i`$ synchronized by the key (e.g. a shift register)
  - Block ciphers as SSCs:
    - send an initial key value $`KS_0 = IV`$ to the receiver in the clear
    - Compute $`KS_i = E_K (KS_{i-1})`$and$`C_i = M_i \oplus KS_i`$
- Self-SSC: Self-Synchronyzing Stream Cipher
  - Similar to SSC, except the counter is replaced by a register containing the previous $`k`$ ciphertexts
  - self-synchronyzing after $`k`$ steps
  - can also be implemented with a block cipher as above
  - limited error propagation (k steps)

### Modes of operation and their purpose

- **ECB**: Electronic Code Book - blocks are encrypted sequentially, one at a time
- **CBC**: Cipher Block Chaining:
  - send initial random block $`C_0 = IV`$ (e.g. a plaintext encrypted in ECB mode, such as$`C_0 = E_k(00 ... 00)`$)
  - **Encryption**: $`C_i = E_K (M_i \oplus C_{i - 1})`$.$`M_i \oplus C_{i - 1}`$ called pre-whitening
  - **Decryption**: $`M_i = D_K(C_i) \oplus C_{i - 1}`$
  - Features:
    - Varying IV encrypts the same message differently
    - Repeated plaintexts will be encrypted differently in different repetitions
    - Plaintext errors propagate through the rest of encryption (good for message authentication)
    - Limited error propagation in decryption: error from incorrect ciphertext modification input propagates to the next block.

Note: CTR, CFB, and OFB turn block cipher into a stream cipher by generating a pseudorandom key stream \$`KS_i`$.$`KS_i = E_K(string)`$,$`C_i = M_i \oplus KS_i`\$.

Arguement of $`E_K`$ is:

- a counter value in CTR mode (synchronous)
- previous ciphertext bits in CFB mode (self-sync)
- previous key stream bits in OFB mode (sync)

Modes:

- **CTR**: Counter - SSC with key stream $`KS_i = E_K(CTR_i)`$ where $`CTR_i`$ is a counter of the same size as the plaintext block size.
  - Subsequent values of the counter are computed using an iterating function: $`CTR_{i+1} = CTR_i + 1 \pmod{2^n}`$.
  - Counter must be unique for each plaintext block:
    - keep count of number of plaintext blocks encrypted under a given counter sequence.
    - use a new block cipher key before exceeding $`2^n`$ blocks (n-bit blocks)
- **CFB**: Cipher Feedback
  - self-ssc
  - simplest form, one register: $`KS_i = E_K (C_{i - 1})`$ with $`C_0 = IV`$
  - in general, r cioher bits are fed back (for DES, r = 8 and IV is at least 48 random bits, right justified, padded  with 0's).
- **OFB**: Output Feedback
  - ssc
  - simplest form, one register: $`KS_i = E_K (KS_{i - 1})`$ with $`KS_0 = IV`$
  - in general, r keystream bits are fed back

## Hash Functions and MACs

### Definition and properties of a cryptographic hash function

### Iterated Hash Functions

### Sponge Design

### Basic overview of Keccak

#### Hash length

#### Number of rounds

#### Format of states

#### High Level Design

### Attacks on hash functions

#### Brute Force Attack

#### Birthday Attack

### Definition and properties of MAC

#### Services provided by MAC

### Basic idea of CMAC (CBC-MAC with special key in last round) and HMAC

### Attacks on MACs and their complexity

#### MAC space

#### Key space attacks

## Key Agreement

## Public Key Cryptosystems

## Number Theory
