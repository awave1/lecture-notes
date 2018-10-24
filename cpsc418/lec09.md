## Birthday attack on digital signatures

Birthday attack on signature schemes with hash functions:

- Attacker generates $`2^{m/2}`$ variations of a valid message (easy to do by adding/removing white space, replacing synonyms)
- Attacker generates $`2^{m/2}`$ variations of a desired fraudulent message
- The two sets of messages are compared to find a pair with the same hash
- Attacker has the victim sign the hash of the valid message - the signature will also be valid for the fraudulent message

## Cryptoanalytic Attacks

Hash functions are composed of rounds that iteratively use a compression function f.

Iterated hash functions can be set up in such a way that if f is collision resistant, so is H (hash function)

An attack approach is to exploi the structure of the hash function (similar to block ciphers):
- analytically attack the rounds of a hash function
- focus on collisions in function f
- many hash functions have succumbed to this type of attack.

## Message Authentication Codes

A small, fixed sized, **key dependent** block that is applied to a message to check data integrity - aka keyed hash function or tag.

A single parameter family $`\{C_k\}_{k \in K}`$ of many-to-one functions

```math
C_k: M \to \{0, 1\}^n (n \in \N)
```

satisfying:

- Ease of computation when the key $`k`$ is known: For any $`m \in M`$ and $`k \in K`$, $`C_k(m)`$ is easy to compute
- Computation resistance: for any key $`k \in K`$, given zero or more message/MAC pairs $`(m_i, C_k(m))`$, it is computationally infeasible t ocompute any new message/MAC pair $`(m C_k(m))`$, $`m \new m_i`$ for all $`i`$, without knowledge of $`k`$.

Note: **Computational resistance (MACs)** and **collision resistance (hash functions)** are different. 

### Data integrity using MACs

Computational resistance implies data integrity (without secrecy):

- sender and receiver share a secret key $`k`$
- sender computes $`MAC = C_k(m)`$ and sends $`(m, MAC)`$ (**unencrypted**)
- Receiver computes computes $`MAC' = C_k(m)`$ and checks $`MAC' = MAC`$. If they match and $`C_k`$ is computation resistant, the integrity of $`m`$

MACs also provicde limited sender authentication in a similar manner to encryption. Note: non-repudiation of data origin is *not* provided.

### MAC vs Encryption

MAC does not provide secrecy, it's not necessarily reversible, many messages have the same MAC. Encryption provides secrecy, reversivle via decryption, and injective.
