# Prodigy InfoTech Internship Tasks

## Task 1: Caesar Cipher Encryption and Decryption

- **Directory:** `PRODIGY_CS_01`
- **Description:** This directory contains a Python program for encrypting and decrypting text using the Caesar Cipher algorithm.


## Usage Instructions

1. **Encryption:**
   - Run the `Cipher_Program.py` program.
   - Enter the message you want to encrypt.
   - Enter the shift value (an integer) for encryption.
   - The program will output the encrypted message.

2. **Decryption:**
   - Run the `Cipher_Program.py` program.
   - Enter the encrypted message.
   - Enter the the shift value used for encryption to decrypt the message.
   - The program will output the decrypted message.

---

## Caesar Cipher Algorithm Overview

The Caesar Cipher is a simple substitution cipher technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on.

- **Encryption:** \( E(x) = (x + n) \mod 26 \)
- **Decryption:** \( D(x) = (x - n) \mod 26 \)

---

## Example

- **Message:** "HELLO WORLD"
- **Shift:** 3
- **Encrypted Message:** "KHOOR ZRUOG"
- **Decrypted Message:** "HELLO WORLD" (using a shift of 3 for decryption)

