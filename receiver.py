import socket

import oqs

from encryption import decrypt


server = socket.socket()

server.bind(

        ("localhost",5000)

)

server.listen(1)

print()

print("Receiver Started")

print()

print("Waiting for Sender...")

print()

conn, addr = server.accept()

print("Sender Connected")

print()


kem = oqs.KeyEncapsulation(

        "ML-KEM-768"

)

public_key = kem.generate_keypair()

conn.send(public_key)

ciphertext = conn.recv(4096)

shared_secret = kem.decap_secret(

        ciphertext

)

print("Receiver Shared Secret")

print()

print(

    shared_secret.hex()

)

print()

while True:

    nonce = conn.recv(16)

    if not nonce:

        break

    encrypted_message = conn.recv(4096)

    message = decrypt(

        nonce,

        encrypted_message,

        shared_secret

    )

    if message.lower() == "exit":

        print()

        print("Sender ended session")

        break

    print()

    print("Message Received")

    print()

    print(message)

    print()

conn.close()

server.close()