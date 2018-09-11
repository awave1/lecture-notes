# Basic Terminology, Classical Ciphers

**Outline**:
1. Cryptography as a part of InfoSec
2. Encryption and Decryption
3. Cryptographic attacks
4. Cryptographic security
5. Introduction to ciphers (Substitution ciphers)
6. Substitution ciphers (Monoalphabetic sub. ciphers, Polyalphabetic sub. ciphers)
7. Transposition ciphers

---

## Information Security
> InfoSec: Measures to protect information and information systems from unauthorized access, use, disclosure, disruption, modification or destruction.

Cryptography provides some such measures:
* Important part of complete security systems, but not all of it
* Addresses mainly technological questions.
* Doesn't do it all

## Security Mechanisms
Cryptography provides services that can achieve *security* objectives.
Services provided by modern cryptography:
* Data confidentiality - data only readable to legitimate parties
* Data integrity - data has not been modified
* Non-repudiation - protection against denial by one of the parties in a communication
* Authentication - communicating entity is the one claimed
* Access Control

Encryption is just one of many *security* mechanisms that achieve one or more of the aboce security objective.
Cryptography security mechanisms discussed in this course include:
* Encryption systems - for confidentiality and limited data integrity
* Hash functions, Message Authentication Codes (**MAC**) - for data integrity
* Digital signatures - for data origin authentication and non-repudiation
* Authentication exchange/protocol - for entity authentication and access control.

Cryptography provides many security mechanismsm but not all:
* Necessary, but not sufficient for InfoSec

Reference: *Why Cryptosystems fail*, Russ Anderson

## Security Attacks
Security mechanisms are designed to detect, prevent, or recover from a *security attack*, i.e. an acction that compromises the security of information by an organization.

In cryptography we distinguish **two types** of attacks:
1. **Passive attacks** - listening, eavesdropping on information without interaction with the system
2. **Active attacks** - interacting with the system, modifying information (for impersonation, replaying messages, changing contents, or denieal of service).

Successfull cryptographic protocols typically combine several mechanisms to guard against as many different attacks as possible (especially active ones).

## Modern Terminology of Cryptography
* **Cryptography** - the study of mathematical techniques for providing information security services.
* **Cryptanalysis** - the study of mathematical techniques for attempting to **defeat** cryptographic security mechanisms.
* **Cryptology** - Combined fields of cryptology and cryptanalysis
* **Cryptographic primitive** - tool that represents a cryptographic security mechanism
  - For example: an encryption scheme
* **Cryptographic protocol** - an algorithm to be undertaken by two or more entities t oachieve a specific security objective

Reference: *Handbook of Applied Cryptography*

* **Message space** $`M`$ - set of all possible plaintext messages
* **Cipher space** $`C`$ - set of all possible encrypted messages
* **Key space** $`K`$ - the finite set of possible keys
* **Encryption transformation** - a left invertible map $`E_k: M \to C`$, indexed by some key $`k \in K`$
* **Decryption transformation** - the left inverse map $`D_k`$ of $`E_k`$, so $`D_k(E_k(M)) = M`$ for all plaintexts $`m \in M`$

> Note: $`D_{k}(E_{k}(M)) = M`$ implies that $`D_k \space \circ \space E_k = I`$ is the identity transformation on $`M`$.
> Note: The fact that $`E_k`$ is left-invertible is equivalent to $`E_k`$ is an injective (i.e. one-to-one) map.

## The idea of encryption and decryption
Gilles Brassard, prof at the U of Montreal, the inventor of quantum cryptography, created the protagonists *Alice and Bob*. Since then, more characters joined the crypto game, most notably *Eve - the eavesdropper*.

**Idea**:
* A transmitter (Bob) generates a plaintext message `m (partof) M` to be communicated to a legitimate receiver (Alice) over an insecure channel.
* To prevent Eve from learining the contents of `m`, Bob chooses a key `k (partof) K` and encrypts `m` with `Ek` to produce the ciphertext `C = Ek(m)`.
* `C` is sent along the insecure channel. When Alice obtains `C`, she deciphers it by applying `Dk` to `C` to obtain `M = Dk(C)`.

### Issues
Encryption functons are our first example of a cryptographic primitive
* could easily formalize the above description to create a crypto. protocol.

Note that Bob must somehow communicate the secure key to Alice without Eve obtaining it, i.e. over a **secure channel**. The assumption is that the workings of `Ek` and `Dk` are not secret, but `k` is secret, so only Alice can decrypt, but no one else can.

#### Example: Shift Cipher
* $`M = C = \{A, B, ... Z\}`$
* Keys represent shifts by a position between 0 and 25.
* Encryption is forward circular shift of a plaintext letter by `k`.
* Decryption is the corresponding backward circular shift of a ciphertext letter by `k`.

More formally, first assign each letter a numerical equivalent, as follows:
```
0 1 2 3 ... 25
A B C D     Z
```
- With that, we have $`M = C = K = Z_{26}`$ (the integeras module 26)
- Encryption: $`E_k(m) = (m + k) \space \% \space 26`$ (remainder between 0 and 25)
- Decryption: $`D_k(c) = (c - k) \space \% \space 26`$ (remainder between 0 and 25)
> Note: For the Caesar cipher, k = 3.

##### Issues with the Shift Cipher
Main problem: very small key space ($`|K| = 26`$)
- Easily falls to a *brute force attack* by simply typing each key in turn. (assuming you know that a shift cipher is used).

**How small is small?**:
- With modern technology, one tenth of a billion billion: $`10^{17} = 2^{56}`$ is small (DES has $`|K| = 2^{56}`$)
- Clearly $`26 < 2^{56}`$.
