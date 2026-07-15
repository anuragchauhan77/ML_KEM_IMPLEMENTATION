import oqs

print("\n================================")
print(" ML-KEM-768 IMPLEMENTATION ")
print("================================\n")

kem = oqs.KeyEncapsulation("ML-KEM-768")

public_key = kem.generate_keypair()

secret_key = kem.export_secret_key()

ciphertext, shared_secret_sender = kem.encap_secret(public_key)

shared_secret_receiver = kem.decap_secret(ciphertext)

print("Shared Secret Match :")

print(shared_secret_sender == shared_secret_receiver)

print()

print("Public Key Size :")

print(len(public_key))

print()

print("Secret Key Size :")

print(len(secret_key))

print()

print("Ciphertext Size :")

print(len(ciphertext))

print()

print("Shared Secret Length :")

print(len(shared_secret_sender))