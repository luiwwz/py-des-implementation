# DES Implementation in Python

An educational implementation of the symmetric-key block cipher **DES (Data Encryption Standard)** built from scratch in Python without third-party cryptographic libraries.

## Current Features
* Encryption of a single 64-bit data block (an 8-character ASCII string).
* Generation of 16 round subkeys (48 bits each) from an initial 64-bit key (8 characters).
* Complete Feistel network cycle (16 rounds, S-boxes, initial and final permutations).

## Project Structure
* `tables.py` — permutation tables (IP, FP, E, P, PC-1, PC-2), key shift schedule, and S-boxes.
* `des.py` — bit conversion utilities, key generation, and encryption logic.
* `main.py` — entry point for running the encryption.
