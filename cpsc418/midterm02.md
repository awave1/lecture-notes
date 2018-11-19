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

* Hash functions and MACs - for **data integrity**

### Definition and properties of a cryptographic hash function

* A function $`H: \{0, 1\}^* \to \{0, 1\}^m`$, $`m \in \N`$ that is easy to compute. An image $`x = H(M)`$ is referred to as a message digest or digital fingerprint or a checksum or simply a hash.
* Properties of hash functions:
  * Compression: $`H`$ maps an imput $`M`$ of arbitrary bit length to an output of fixed bit length.
  * Ease of computation: for any input $`M`$, $`H(M)`$ is easy to compute.
* Cryptographic requirements:
  * **Pre-image resistance**: Given any hash value x, it is computationally infeasible to find a **pre-image** of x, i.e. *any* input $`M`$ for which $`H(M) = x`$.
  * **Weak collision resistance**: given any input $`M`$, it is computationally infeasible to find a weak collision, i.e. an input $`M' \neq M`$ with $`H(M) = H(M')`$.
  * **(Strong) Collision resistance**: it is computationally infeasible to find a strong collision i.e. two disting inputs $`M`$ and $`M'`$ such that $`H(M) = H(M')`$.
  * Note:
    * Collision resistance does not imply pre-image resistance or vice versa
    * Weak collision resistance does not imply pre-image resistance or vice versa
    * Collision resistance implies weak collision resistance, but not vice versa
* A hash function is cryptographically secure if it is pre-image resistan and collision resistant

### Iterated Hash Functions

* Composed of rounds like DES or AES
* Repeated use of compression function f - takes m-bit input from the previous step (chaining variable) and r-bit block from M, produces m-bit output
* input to H: message M consisting of r-bit blocks $`P_1, ..., P_L`$ (padded if necessary, so the total length is a multiple of r).
* Iterated hash functions can be set up in such a way so that if f is collision resistant, so is H.
* *read about sha1 and md5 in notes*

### Sponge Design

- Hash function: arbitrary input length, fixed output length
- Stream cipher: fixed input length, arbitrary output length
- **Sponge function**: arbitrary input length, variable user-supplied output length

Sponges can be used to build various cryptographic primitives:

- Stream ciphers
- Hash functions
- MACs

#### Overview

Sponge function consists of:

- width b (an int)
- bit rate r (an int, r < b)
- input S (bit string of length b)
- fixed length permutation f that operates on S
- padding rule "pad" that pads blocks of length r to blocks of length b

The **capacity** of the sponge is the **padding amount**: $`c = b - r`$. The padding rule for Keccak simply appends the string 100 ... 01 ($`c - 2`$ zeros) to each r-bit block (called *multi-rate padding*).

##### Absorb

The input to the **absorbtion** phase is the message M - padded so the total length is a multiple of $`r`$ - consisting of r-bit blocks $`P_1, ..., P_{L}`$. The output is a string S of length b. **Absorbtion = xor & permute**.

##### Squeeze

The **squeezing** phase outputs on input S a hash message M whose bit length is a user-supplied value m. **Squeezing = append & permute**

### Basic overview of Keccak

- SHA3/Keccak specifies:
  - **hash lengths** m = 224, 256, 384, 512 (like SHA2)
  - **capacities** c = 2m
  - **widths** b = 25, 50, 100, 200, 400, 800, 1600 (1600 is default)

The **internal state** to the Keccak permutation f, denoted A is a 3d bit array of dimensions $`5 \times 5 \times 2^l`$, where $`0 \leq l \leq 6`$, yeilding the above widths (default is $`l = 6`$ with a state $`5 \times 5 \times 64`$).

The Keccak permutation f iterates over multiple rounds. In SHA3, the number of rounds $`N_r`$ is $`12 + 2l`$. Each round of f operates on the state A and is the composition of 5 functions: $`\iota \circ \chi \circ \pi \circ \rho \circ \theta`$.
$`\iota`$ incorporates round constants that vary by round.

### Attacks on hash functions

- Objectives:
  - find a pre-image: given any hash, create a corresponding message with that hash
  - find a weak collision: given a message, modify it to another message with the same hash
  - find a collision: find two messages with the same hash

#### Brute Force Attack

For an m-bit hash function:

- pre-images and weak collisions: $`2^m`$ attempts on average
- strong collisions: $`2^{m/2}`$ attempts on average due to **birthday paradox**.
  - birthday paradox: expected number of draw & replace trials from N objects required to draw an object twice approaches $`\sqrt{\pi N/2} \approx 1.25\sqrt{N}`$ as $`N`$ grows.
- recommended sizes of m: 224, 256, 394, 512 (provide 112, 128, 192, and 256 bits of security)

#### Weak vs Strong collision reistance

Let m be of a size where:

- searching a space of size $`2^m`$ is computationally infeasible
- searching a space of size $`2^{m/2}`$ is computationally feasible.

Then we expect m-bit hash function to be:

- pre-image resistant
- weakly collision resistant
- **not** strongly collision resistant

#### Birthday Attack on signature schemes with hash functions

- Attacker geenrates $`2^{m/2}`$ variations of a valid message
- Attacker generates $`2^{m/2}`$ variations of a desired fraudelent message
- The two sets of messages are compared to find a pair with the same hash
- Attacker has the victim sign the hash of the valid message - the signature will also be valid for the fraudelent message

### Definition and properties of MAC

* **MAC**: a small, fixed size key-dependent block that is appended to a message to check data integrity - AKA keyed hash function or tag.
* MAC definition:
  * A single parameter family $`\{C_K\}_{K \in K}`$ of many-to-one functions $`C_K: M \to \{0, 1\}^n`$, $`n \in \N`$, satisfying:
    * Ease of computation with knowledge of K: For any $`m \in M`$ and $`k \in K`$, $`C_K(M)`$ is easy to compute.
    * Computation resistance: for any $`k \in K`$, given zero or more message/MAC pairs $`(m_i, C_k(m_i))`$, it is computationally infeasible to compute any new message/mac pair $`(m, C_k(m))`$, $`m \neq m_i`$ for all $`i`$, without knowledge of $`k`$.

#### Services provided by MAC

* Computation-resistance implies **data integrity** (without secrecy):
  - sender and receiver share a secret key $`k`$
  - sender computes $`MAC = C_k(m)`$ and sends (m, mac) (unencrypted)
  - receiver computes the same thing and checks $`mac' = mac`$. If they match and $`C_k`$ is computation resistant, the integrity of $`m`$ is preserved.
* Active attack:
  - attacker suppresses (m, mac) and instead sends a pair (m'', mac'') to the receiver
  - receiver checks if $`C_k(m'') = mac''`$. If it holds, the attacker must have defeated computational resistance -> generated new pair (m'', mac'') from (m, mac).
* MACs provide limited sender authentication in a similar manner to encryption:
  - only sender or reciver who knows k could generate the mac.
* non-repudiation of data origin is not provided:
  - either party possesing k can generate macs.

### Basic idea of CMAC (CBC-MAC with special key in last round) and HMAC

MAC can be applied first and then encrypt the message or encrypt the message first and apply MAC to the ciphertext.

- Encrypt then MAC
  - formally secure, it preserves the integrity of the ciphertext and protects against malleability
  - prone to implementation errors
- MAC then encrypt
  - more natural, less error prone
  - can be more practical if encryption is defeated, message integrity is still preserved

* **CMAC**: a secure block cipher can be used to generate MACs
  - **CBC-MAC**:
    - Encrypt the message (zero IV, last block padded with 0s) using CBC mode
    - the last cipher block (whose bits are dependent on all the key bits and message bits) is the MAC
  - Only secure if messages of one fixed length are processed. Solution:
    - use three keysm one at each step of chaining, two for the last block
    - second two keys may be derived from the encryption key
  - Properties:
    - specified for use with AES and 3DES.
    - can be proven secure as long as the underlying block cipher's output is indistinguishanle from a random permutation
    - no known weaknesses
* **HMAC**: $`MAC = H(M||K)`$ where H is a cryptographic hash function and K is a secret key.
  - advantage over CMAC: hash functions are faster than block ciphers
  - provable security

### Attacks on MACs and their complexity

- Compute a new message / MAC pair (M, Ck(M)) for some message M != Mi given one or more pairs (Mi, Ck(Mi)).
- Known-text, chosen-text, and adaprive chosen text variations are possible.

#### MAC space attack

Assume n-bit MACs, m-bit keys:

- pick a message, guess the MAC value (probability $`2^{-n}`$ of being correct)
- requires black-box MAC verifier to confirm guesses
- expected number of attempts is 2^n
- does not find the MAC key

#### Key space attacks

Assumes m > n (longer keys than MACs, reasonable). This is KPA:

- given M1 and MAC1 = Ck(M1), compute MACi1 = Cki(M1) for all possible keys ki $`1 \leq i \leq 2^m`$
- expect $`2^{m - n}`$ keys to produce a match MAC1 = MACi1 ($`2^m`$ MACs produced, only $`2^n`$ possible MACs)
- repeat with M2 and MAC2 = Ck(M2) reducing the number of possible keys to $`2^{m - 2n}`$. Iterate with Mj and MACj = Ck(Mj), j = 3, 4, .. .
- Requirements:
  - [m/n] message/MAC pairs
  - [m/n] * 2^m MAC computations but these can be conducted offline if M1, M2 are known in advance.
- Brute force attacks (n bit MACs, m-bit keys):
  - $`2^n`$ to defeat computation resistance (find a valid message/mac pair)
  - [m/n] $`2^m`$ to find a MAC key.
- for CMAC possible to attack cipher
- for HMAC possible to attack hash function

## Key Agreement

### One way functions

One way function is a function that satisfies two following properties:

- Ease of computation: $`f(x)`$ is easy to evaluate for a given $`x`$.
- Pre-image resistance: Given $`y = f(x)`$ it is computationally infeasible to find $`x`$
- Examples:
  - pre-image resistant hash function is a one-way function

### Diffie Hellman protocol

![Diffie-Hellman Protocol](cpsc418/img/m2/dhp.png)

- A and B get the same number K because $`y_{b}^{a} \equiv (g^b)^a \equiv g^{ba} \equiv y_{a}^{b} \pmod{p}`$
- Can use the low order 128 bits of $`H(K)`$ for an AES key, where H is a cryptographically secure hash function

### Discrete Logarithm Problem

For a prime $`p`$:

- The function $`f(x) = g^x \pmod{p}`$ is a one-way function. This means that the **discrete logarithm problem** - extracting discrete logs is computationally hard since it's equivalent of computing a pre-image of a one-way function.

### Diffie-Hellman Security

#### Best choice of p

* The best choice for $`p`$ is a safe prime, a prime of the form: $`p = 2q + 1`$, with $`q`$ prime.
* $`q`$ is called **Sophie Germain** prime.

#### Best choice of g

* A primitive root of p
  - maximizes the number of possible values K

### MITM attacks on "textbook" DH

* Attacker gets a hold of $`g^a`$ and $`g^b`$.
  - select $`1 < e < p`$ and seng $`g^e`$ to A and B
* A computes $`g^{ea}`$
* B computes $`g^{eb}`$
* Attacker can compute $`g^{ae}`$ and $`g^{be}`$ which are keys for A and B
* Results:
  - attacker can intercept $`g^{ea}`$ from A and decrypt messages encrypted using $`g^{ea}`$, re-encrypt it with $`g^{eb}`$ and send to B
  - B decrypts it correctly using $`g^{eb}`$

## Public Key Cryptosystems

- Every user has **2 keys**:
  - **encryption** key is **public**
  - **decryption** key is **only known to the receiver**
- Deducing the decryption key from the encryption key should be computationally infeasible

### Trapdoor one-way functions

- A function f that satisfies the following properties:
  - **Ease of computation**: $`f(x)`$ is easy to compute for any given $`x`$
  - **Pre-image Resistance with Trap-door**: Given $`y = f(x)`$, it is computationally infeasible to determine $`x`$ unless certain special information used in the design of $`f`$ is known.
    - When this **trap-door** $`k`$ is known, there exists a function $`g`$ which is easy to compute such that $`x = g(k, y)`$
- key to designing public-key cryptosystems: decryption key acts as a trap door for the encryption function

### Definition of a PKC

- A PKC consists of a plaintext space $`M`$, a ciphertext space $`C`$, a public key space $`K`$, and encryption functions $`E_{k_1} : M \to C`$, indexed by public keys $`k_1 \in K`$ with following properties:
  1. every encryption function $`E_{k_1}`$ has a left inverse $`D_{k_2}`$, where $`k_2`$ is the private key corresponding to the public key $`k_1`$.
  2. $`E_{k_1}(m)`$ and $`D_{k_2}(c)`$ are easy to compute when $`k_1`$ and $`k_2`$ are known.
  3. $`D_{k_2}(E_{k_1}(m)) = m`$ for all $`m \in M`$
  4. Given $`k_1`$, $`E_{k_1}`$, and $`c = $`E_{k_1}(m)`$, it is computationally infeasible to find $`m`$ or $`k_1`$
- properties 2 - 4 describe $`E_{k_1}`$ as a trapdoot one-way function
- in a PKC it is **not necessary** for the key channel to be secure

#### Properties of PKC

- unlike convenional cryptosystems, messages encrypted using public key cryptosystems contain sufficient information to uniquely determine the plaintext and the key (given enough ciphertext, resources, etc)
  - the **entropy** contained in these systems is **zero**
  - this is the **exact opposite** of a perfectly secret system like **one time pad**
- security of a PKC lies in the computational cost of computing the plaintext and/or private key from the ciphertext (computational security)

#### Services provided by PKC

- PKC's in use today are **much slower** than systems like AES (by a factor of 1000-1500), generally not used for bulk encryption. Common uses:
  - **Encryption** and transmission of keys for conventional cryptosystems (**hybrid** encryption)
  - Authentication and non-repudiation via digital signatures

### RSA

#### Security of "textbook" RSA

##### Equivalence of factoring n

##### Computing $`\phi(n)`$ and finding $`d`$

##### Choice of parameters

### Multiplicative attacks on RSA

#### CCA

#### Meet in the middle

### Randomized encryption

- ElGamal key generation, encryption and decryption procedures (no details about those)

### Facts and assumptions about ElGamal

## Number Theory

**in notebook**