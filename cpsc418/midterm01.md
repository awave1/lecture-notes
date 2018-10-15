# Midterm 1 - Study Guide

## Overview of cryptography

### Services provided by cryptography

### Notions of cryptographic primitive and cryptographic protocol

### Definitions and ingridients of cryptosystem

### Notions of active and passive attacks and the corresponding goals of the attacker

### Types of attacks

- COA
- KPA
- CCA
- Adaptive versions of attacks, described above

### Notions of security of a cryptosystem

- Unconditional
- Provable
- Computational

### Kerckhoff's principle

## Classical cryptography

### Classical ciphers

- Monoalphabetic substitution
  - Casesar
  - Shift
  - One-time pad
- Polyalphabetical substitution
  - Vigenere
- Transposition

### Security of classical ciphers (vulnerability to KPAs or even COAs)

## Perfect secrecy and entropy

### Definition of perfect secrecy

### Bayes' Theorem

### Equivalent characterization of perfect secrecy

$`p(C|M) = p(C)`$ for all $`M, C`$ with $`p(M), p(C) > 0`$.

Note: should be able to work with formulas for $`p(C|M)`$ and $`p(C)`$.

### Perfect secrecy, and what it implies

### One-time pad, strengths and weaknesess of OTP, security of OTP

### Entropy: meaning of formula; min/max entropy

Entropy is **maximal** exactly for equiprobable outcames and **minimal** exactly when one outcome always occurs (should know maximal value $`\log_2(n)`$ and minimal value $`0`$.

## Modern symmetric cryptography

### Concepts of confusion and diffusion

- Confusion: obtained through substitutions
- Diffusion: obtained through transpositions/permutations

### Basic specification of DES

- Format of plaintexts, ciphertexts, and keys
- Number of rounds
- A product cipher with a **Fiestel network architecture**

### Basic specifications and high-level design of AES

- Format of plaintexts, ciphertexts, and keys
- Notion of a state
- The fact that is is a product cipher, consisting of three layers
  - linear mixing
  - non liniar substitutions
  - key XORing

### Attacks on block ciphers

- Exhaustive search
- Notion and resource requirements of time-memory trade-off
- Meet-In-The-Middle attack on double encryption and its run requirement
- Diffrential and linear cryptoanalysis

## Discrete Math Topics

### Congruences & Integer modular arithmetic

### Modular arithemtic on polynomials with binary coefficients

### Proof techniques
