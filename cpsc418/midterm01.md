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
  - $`E_k: M \to C`$ via $`m \mapto c := E_k(m)`$ called encryption functions.
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

####### Cryptanaltysis of Vigenere

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

## Discrete Math Topics

### Congruences & Integer modular arithmetic

### Modular arithemtic on polynomials with binary coefficients

### Proof techniques
