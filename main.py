import oqs

# Display the project title

print(" ML-KEM-768 IMPLEMENTATION ")

# Initialize the ML-KEM-768 Key Encapsulation Mechanism
kem = oqs.KeyEncapsulation("ML-KEM-768")

# Generate the public and secret key pair
public_key = kem.generate_keypair()

# Export the generated secret key
secret_key = kem.export_secret_key()

# Encapsulate the public key to generate the ciphertext and sender's shared secret
ciphertext, shared_secret_sender = kem.encap_secret(public_key)

# Decapsulate the ciphertext to generate the receiver's shared secret
shared_secret_receiver = kem.decap_secret(ciphertext)

# Verify whether both sender and receiver generated the same shared secret
print("Shared Secret Match :")

print(shared_secret_sender == shared_secret_receiver)

print()

# Display the size of the generated public key
print("Public Key Size :")

print(len(public_key))

print()

# Display the size of the generated secret key
print("Secret Key Size :")

print(len(secret_key))

print()

# Display the size of the generated ciphertext
print("Ciphertext Size :")

print(len(ciphertext))

print()

# Display the length of the shared secret
print("Shared Secret Length :")

print(len(shared_secret_sender))
