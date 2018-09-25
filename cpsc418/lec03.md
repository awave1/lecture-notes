# Components of a Cryptosystem
* $`M`$ - message / plaintext space
* $`C`$ - ciphertext space
* $`K`$ - key space

> **Shift Ciphers**: $`M + C + K = \Z_{26}`$

## Symmetric Cryptosystems
A symmetric cryptosystem consists of the following:
* A finite non-empty set $`M`$ called the *plaintext* space
* A finite non-empty set $`C`$ called the *ciphertext*  space
* A finite non-empty set $`K`$ called the *key* space
* A single-parameter family $`\{E_k\}_{k \in K}`$ off injective transformations

```math
E_k: M \to C \space via \space M \mapsto C := E_k(M)
```

Called *encryption functions*. The left inverse $`E_k`$, denoted $`D_k`$, is called the corresponding *decryption function*. That is:

```math
D_k(E_k(m)) = m \space for \space all \space m \in M \space and \space k \in K
```

### Schematic of a Symmetric Cryptosystem

> Conventional or private key cryptosystems

![Schematic of a symmetric cryptosystem](cpsc418/img/lec03/01_symmetric_cryptosystem.png)

## Key Channel
In order for the encryption to be secure, *key channels* must be absolutely secure, as the channel from the source to the transmitter. In the real world, this usually means expensive. For example, the keys to the Moscow-Washington htline are transmitted by means of highly paid couriers, who fly there and back every week.

It woulde be nice to dispense with the key channel. Why bother encrypting when we have a secure channel already?

* **Time-shifting, convinience** - you have access to a secure channel now, but would like to use it later, when the channel may not be available
* **Speed, bandwidth** - the secure channel may be slow or of a limited bit rate
* **Cost** - the secure channel may be expensive; e.g. hand-delivered by courier
* **Feasibility** - the security channel may be impractical; e.g. Alice and Bob meet in person before securely communicating

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

Provable security does *not* mean that a cryptography is *proved* secure.
* Proofs typically only reduce to another problem (which could eventually be solved)
* Proofs assume specific adverarial capabilities and attacks (e.g. adaptive CCA)

## Classical ciphers
Classical ciphers usually beong to one of the following two types: substitution or transposition ciphers.

**Substitution cipher** - a cipher for which encryption replaces each plaintext symbol by some ciphertext symbol without changing the order of the plaintext symbols

**Transposition cipher** - a cipher in which the ciphertext is a rearrangement (i.e. permutation) of the plaintext symbols

### Modern Usage
Individually, substitution ciphers and transposition ciphers are generally insecure. However, when alternating them repeatedly, they become secure.

```math
M \to T \to S \to T \to S \to \space ... \space \to T \to S \to C
```

## Substitution Ciphers
Substitution ciphers come in two types:
* Monoalphabetic
* Polyalphabetic

**Monoalphabetic Substitution Cipher** - a substitution cipher that uses a single ciphertext alphabet in the replacement of the plaintext characters

**Polyalphabetic Substitution Cipher** - a substitution cipher in which multiple cipher alphabets are used in the replacement of the plaintext characters

### Monoalphabetic Substitution Ciphers
The simplest example of a monoalphabetic cipher is the **shift cipher**.

#### Example: Shift Cipher
Rather than computinf the shifts, it can be easier to encrypt and decrypt a shift cipher with a *Vigenere tableau*

![Vigenere tableau](cpsc418/img/lec03/02_vigenere.png)

##### Shift Cipher Encryption via Vigenere Tableau
**Encryption**: The key (shift) represents a column. The ciphertext letter is located at the intersection of this column and the row given by the corresponding plaintext letter.
* To encrypt the letter 'i' with a Caesar cipher (key letter D), look up for the row for 'i' and the column for 'D' in the Vigenere tableau. The entry in the tableau gives the ciphertext letter, in this case 'L'.

**Decryption**: Look up a ciphertext letter in the column given by the key. The corresponding plaintext letter is located at the beginning of that row.
* To decrypt 'L' under key 'D', find the entry for L in the column for D. The corresponding row begins with 'i' which is the plaintext letter.

![Vigenere tableau](cpsc418/img/lec03/03_vigenere.png)

#### Security of Monoalphabetic Substitution Ciphers
##### Monoalphabetic Substitution Ciphers in Literature

#### Codes

### Polyalphabetical Substitution Ciphers
A substitution cipher in which several cipher alphabets are used in the replacement of the plaintext characters.

#### Viginere Example
Plaintext: `stay in current position`
Key: `BLACKSTONE`

**Encryption**: done via Vigenere tableau, except now consider multiple columns.
* To encrypt the first letter 's', look up the row for 's' and the collumn for 'B' in the Vigenere tableau. The entry in the tableau gives the ciphertext letter, in this case 'T'
* To encrypt the second letter 't', find the intersection of the row given by plaintext letter 't' with the column given by key letter 'L' to obtain the ciphertext letter 'E'

Ciphertext is often written in groups of 5 letters to obscure spacing.
* If the number of characters is not multiple of 5, we append *nulls* (bodus characters)
* Can apply to any substitution cipher

**Note**: This is a polyalphabetic substitution cipher. The number of cipher alphabets is equal to the number of letters in the key word (10 in this example).

#### Cryptanalysis of the Viginere Cipher
First, determine the number $`n`$ of cipher alphabets (length of the keyword) using methods like the *kappa text* or *Kasiski's factoring method*. Once $`n`$ is known, consider for $`1 \le i \le n`$ the $`i-th`$ subtext considering of the ciphertext letters in following positions:
```math
i, \space i + n, \space i + 2n, \space i + 3n, \space ...
```

* Each of these is simply text encrypted with a shift cipher whose key is the $`i-th`$ letter in the Vigenere keyword
* Cryptanalyze each just like any shift cipher (with frequency analysis)

#### Other Polyalphabetic Substitution Ciphers
* **Beauford cipher** - slight varation of Vigenere
* **Mixed Vigenere** - works with a Vigenere tableau in which the columns are scrambled according to some key word. It's harder to analyze than Vigenere - need to use a technique called [symmetry of position](https://people.ucalgary.ca/~rscheidl/418/handouts/symmetry.pdf) to find out the column permutation, however, still insecure
* **Coherent Running Key** cipher - like a Vigenere cipher, but with a "running" (i.e. very long) key, usually taken from a readily available text. Still fails to frequency analysis due to language redundancy. However, multiple encryption using four different running keys produces a statistically secure cipher

## Transposition Ciphers
A transposition cipher is a rearrangement (permutation) of the plaintext letters.

### Route Cipher
A transposition cipher where the plaintext is arranged in some geometric figure and the ciphertext is obtained by rearranging the plaintext according to some route through the figure.

#### Example: Route Cipher 
Plaintext: `Now is the time for all good men`.

Encryption: arrange the plaintext by rows into a rectangle of $`K`$ columns and extract the ciphertext by the column.

### Columnar Transposition
The message is arranged horizontally in a rectangle. The key is used to generate a permutation of the columns. The ciphertext is read vertically from the permuted columns.

#### Example: Transposition Example
Key: `SCHMID` (relative order of key letter dictates column permutation)

```
key:   S C H M I D
order: 6 1 3 5 4 2
```

Plaintext: `sell all stock on Monday`

Ciphertext: read columnwise in given order.

Decryption: Write ciphertext in columns in the correct order (and shape) of the rectangle (dictated by ciphertext length and key length).

Note that we can't use nulls at the end on the ciphertext.

#### Cryptanalysis of Columnar Transposistion
Vulnerable to a COA:
* Guess the dimensions of the rectangle
* Determine the order of the columns via frequency counts (which will be the same as for English text). Place columns adjacent to each other if they produce common latter pairs (e.g. QX is extremely unlikely, but EN is highly likely).
