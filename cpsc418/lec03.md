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

```
@TODO: Finish
```
