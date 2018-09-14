# Components of a Cryptosystem
* `$M$` - message / plaintext space
* `$C$` - ciphertext space
* `$K$` - key space

> **Shift Ciphers**: `$M + C + K = \Z_{26}$`

## Symmetric Cryptosystems
```
@TODO: Finish
```
A symmetric cryptosystem consists of the following:
* A finite non-empty set `$M$` called the *plaintext* space
* A finite non-empty set `$C$` called the *ciphertext*  space
* A finite non-empty set `$K$` called the *key* space
* A single-parameter family `$\{E_k\}_{k \in K}$` off injective transformations

```math
E_k: M \to C \space via \space M \mapsto C := E_k(M)
```

Called *encryption functions*. The left inverse `$E_k$`, denoted `$D_k$`, is called the corresponding *decryption function*. That is:

```math
D_k(E_k(m)) = m \space for all \space m \in M \space and \space k \in K
```

### Schematic of a Symmetric Cryptosystem

> Conventional or private key cryptosystems

![Schematic of a symmetric cryptosystem](cpsc418/img/lec03/01_symmetric_cryptosystem.png)

## Key Channel
In order for the encryption to be secure, *key channels* must be absolutely secure, as the channel from the source to the transmitter. In the real world, this usually means expensive. For example, the keys to the Moscow-Washington htline are transmitted by means of highly paid couriers, who fly there and back every week.

It woulde be nice to dispense with the key channel. Why bother encrypting when we have a secure channel already?

```
@TODO: Finish
```

* Time-shifting, convinience
* Speed, bandwidth
* Cost
* Feasibility

## Goals of an Attacker
Notions of attacks on cryptosystems. Goals of an **attacker**:
* Deduce the key or portions thereof
* Deduce one or more plaintexts or portions thereof
* Modify a message
* Replay a message
* Impersonate another entity

The first two are passive attacks, the last three active attacks.

### Passive Attacks on Cryptosystems
Depends on what adversary has available and what attacker can do

* **Cipher Only Attack** (COA) - Adversary has only ciphertex, but no plaintext
* **Known Plaintext Attack** (KPA) - Adversary has some plaintext and corresponding ciphertext

**Note**: These two attacks are *passive*: adversary does not interact with the systems and has no control over the text an attacker is given.

### Active Attacks on Cryptosystems
* **Chosen Plaintext Attack** (CPA) - Adversary chooses some plaintext (independently of the ciphertext an attacker wishes to decrypt) and obtains the corresponding ciphertext.
* **Adaptive CPA** - Adversary's choice of plaintext may depend on ciphertext to be decrypted and other ciphertext received.
* **Chosen Ciphertext Attack** (CCA or CCA1) - Adversary chooses some ciphertext (independenty of the desired decryption) and obtains the corresponding plaintext.
* **Adaptive Chosen Ciphertext Attack** (CCA or CCA2) - Adversary's choice of ciphertext may depend on the ciphertext an attacker wishes to decrypt and on plaintexts received from previous requests. Attacker is not allowed to choose the ciphertext to decrypt.

**Note**: These attacks are *active*: adversary interacts with the system.

### More on attacks

**Note**: A good/secure cryptosystem should be secure against adaptive CCA's (as strong as possible)

Some attacks that cryptography cannot protect against, include:
* **Side Channel Attacks** - adversary exploits some physical aspect of the cryptosystem implementation to extract the ky.
* **Clandestine Attack** (AKA Rubber Hose Cryptography) - adversary bribes, blackmails, threatens, steals, or beats the key out of the recepient.

## Notions of Security
There are different notions of security. Security includes a lot of aspects: physical, psychological. It means different things for different people.

**Kerchoff's Principle**:
The security of a cryptosystem should depend entirely upon knowledge of the key, not the method.

From "La Cryptographie Militarie" (1883), one of the first scientific treatments of cryptography.

> As long as you don't know the key, the system shouldn't be crackable

This principle implies that a cipher should be completely published/open source and *still* be secure (against its own designer and everyone else).

## Measures of Security
Listed from strongest to weakest:
* **Unconditional Security** - can an adversary with unlimited computing power defeat the system?
* **Provable Security** - breaking the system can be reduced (mathematically) to another, supposedly, difficult problem: e.g. integer factorization.
    * Finding factor is one way of cracking the system
    * Can still be other ways of doing that
* **Computational Security** - does the perceived amount of computing power necessary to break the system (using the best known method) exceed (by a comfortable margin) the available computing power of the attacker.
* **Ad-hoc Security** - security is "proved" via a series of convincing arguments that every successful attack is impractical (nowadays no longer accepted)

### Remarks
Computational security often used in conjunction with provable security
* E.g. a typical security claim might read something like "a cryptosystem is provably secure against an adaptive CCA assuming integer factorization is hard"

Provable security does *not* mean that a cryptography `@TODO: finish`

## Classical ciphers
```
@TODO: Finish
```
Classical ciphers usually beong to one of the following two types: substitution or transposition ciphers.

**Substitution cipher** - a cipher for which encryption replaces each plaintext symbol by some ciphertext symbol without changing the order of the plaintext symbols

**Transposition cipher** - a cipher in which the ciphertext is a rearrangement (i.e. permutation) of the plaintext symbols

### Modern Usage
Individually, substitution ciphers and transposition ciphers are generally insecure. However, when alternating them repeatedly, they become secure.

```
@TODO: img and finish
```
