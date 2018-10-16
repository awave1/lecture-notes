# Hash Functions

## Hash Functions - Data integrity

Take a string and give a fixed sized output. Needs to be easy to compute

### Cryptographic Requirements

- Pre-image Resistance (PR): Given a hash $`x`$, it is computationally infeasable to find an $`M`$ where $`H(M) = x`$
- Second pre-image resistance (weak collision resistance): Given some M, it is comp. infeasable to find M_2 where H(M1) = H(M2)
- Collision Resistance(strong collision resistance): It is hard to find M1M2 where H(M1) = H(M2)
-

## Iterated hash function
