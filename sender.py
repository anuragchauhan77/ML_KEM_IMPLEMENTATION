import socket

import oqs

from encryption import encrypt


# Create a socket for the sender (client)
client = socket.socket()

# Connect to the receiver running on localhost at port 5000
client.connect(

        ("localhost",5000)

)

# Receive the public key from the receiver
public_key = client.recv(4096)

# Initialize the ML-KEM-768 algorithm
kem = oqs.KeyEncapsulation(

        "ML-KEM-768"

)

# Perform key encapsulation to generate the ciphertext and shared secret
ciphertext, shared_secret = kem.encap_secret(

        public_key

)

# Send the generated ciphertext to the receiver
client.send(

        ciphertext

)

print()

print("Sender Shared Secret")

print()

# Display the shared secret in hexadecimal format
print(

        shared_secret.hex()

)

print()

# Continuously send encrypted messages until the user exits
while True:

    # Accept message input from the user
    message = input(

        "Enter Message : "

    )

    # Encrypt the message using the shared secret
    nonce, encrypted_message = encrypt(

            message,

            shared_secret

    )

    # Send the nonce required for decryption
    client.send(

            nonce

    )

    # Send the encrypted message to the receiver
    client.send(

            encrypted_message

    )

    # End the communication session if the user enters "exit"
    if message.lower() == "exit":

        print()

        print("Session Ended")

        break

print()

# Close the client socket connection
client.close()
