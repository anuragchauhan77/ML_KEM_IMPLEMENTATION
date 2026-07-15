 ML-KEM-768 Secure Messaging System

A Post-Quantum Cryptography based secure messaging system implemented using **ML-KEM-768 (Module Lattice-Based Key Encapsulation Mechanism)** from the **Open Quantum Safe (liboqs)** library. The project demonstrates how two communicating parties can securely establish a shared secret and exchange encrypted messages over a local network using **AES-256 encryption**.

This project was developed as part of a **DRDO Internship** to understand the practical implementation of Post-Quantum Cryptography and secure communication.


 Project Overview

Traditional public-key cryptographic algorithms such as RSA and ECC are vulnerable to attacks from future quantum computers. To address this challenge, the National Institute of Standards and Technology (NIST) has standardized **ML-KEM (Kyber)** as a post-quantum key encapsulation mechanism.

This project demonstrates the complete workflow of:

- Establishing a secure connection using ML-KEM-768
- Generating identical shared secrets at both communication ends
- Deriving an AES-256 encryption key from the shared secret
- Encrypting messages before transmission
- Securely decrypting messages at the receiver side
- Sending multiple encrypted messages through localhost socket communication

The implementation provides a practical understanding of how post-quantum secure communication systems operate.


 Objectives

- Understand the fundamentals of Post-Quantum Cryptography.
- Implement ML-KEM-768 using the Open Quantum Safe library.
- Perform secure key exchange between sender and receiver.
- Generate identical shared secrets on both communicating systems.
- Encrypt transmitted messages using AES-256.
- Establish secure local communication using Python Socket Programming.
- Demonstrate quantum-resistant secure messaging.



 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| Open Quantum Safe (liboqs-python) | ML-KEM-768 Implementation |
| PyCryptodome | AES Encryption |
| Python Socket Programming | Local Communication |
| SHA-256 | AES Key Derivation |
| Visual Studio Code | Development Environment |
| Git & GitHub | Version Control |

 Project Structure


ML_KEM_PROJECT
│
├── algorithms.py
├── check_methods.py
├── encryption.py
├── main.py
├── receiver.py
├── sender.py
├── test.py
├── venv/
└── __pycache__/

 File Description

 algorithms.py
Displays all post-quantum Key Encapsulation Mechanisms (KEMs) available in the installed liboqs library.



 check_methods.py
Lists all methods supported by the ML-KEM implementation and helps understand the available API functions.

---

main.py
Demonstrates the implementation of ML-KEM-768 by:

- Generating Public Key
- Generating Secret Key
- Performing Key Encapsulation
- Performing Key Decapsulation
- Verifying identical shared secrets
- Displaying key sizes and ciphertext size



encryption.py
Implements AES-256 encryption and decryption using the shared secret generated through ML-KEM.

Functions included:

- AES Key Derivation
- Message Encryption
- Message Decryption



 receiver.py
Acts as the receiver (server).

Responsibilities:

- Starts local server
- Generates ML-KEM Key Pair
- Sends Public Key
- Receives Ciphertext
- Generates Shared Secret
- Receives Encrypted Messages
- Decrypts Messages
- Displays Plaintext



 sender.py
Acts as the sender (client).

Responsibilities:

- Connects to Receiver
- Receives Public Key
- Performs Key Encapsulation
- Generates Shared Secret
- Encrypts Messages
- Sends Ciphertext
- Sends Multiple Messages Securely



 test.py
Verifies successful installation of the Open Quantum Safe library and displays all supported ML-KEM algorithms.


 Project Workflow


Receiver Starts

        │

        ▼

Generate ML-KEM Key Pair

        │

        ▼

Send Public Key

        │

        ▼

Sender Connects

        │

        ▼

Receive Public Key

        │

        ▼

ML-KEM Encapsulation

        │

        ▼

Generate Shared Secret

        │

        ▼

Send Ciphertext

        │

        ▼

Receiver Decapsulation

        │

        ▼

Generate Identical Shared Secret

        │

        ▼

SHA-256 Key Derivation

        │

        ▼

AES-256 Encryption

        │

        ▼

Encrypted Message Transmission

        │

        ▼

AES-256 Decryption

        │

        ▼

Original Message Displayed




 
