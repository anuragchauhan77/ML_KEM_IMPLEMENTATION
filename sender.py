import socket

import oqs

from encryption import encrypt


client = socket.socket()

client.connect(

        ("localhost",5000)

)

public_key = client.recv(4096)

kem = oqs.KeyEncapsulation(

        "ML-KEM-768"

)

ciphertext, shared_secret = kem.encap_secret(

        public_key

)

client.send(

        ciphertext

)

print()

print("Sender Shared Secret")

print()

print(

        shared_secret.hex()

)

print()

while True:

    message = input(

        "Enter Message : "

    )

    nonce, encrypted_message = encrypt(

            message,

            shared_secret

    )

    client.send(

            nonce

    )

    client.send(

            encrypted_message

    )

    if message.lower() == "exit":

        print()

        print("Session Ended")

        break

print()

client.close()