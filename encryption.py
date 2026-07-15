from Crypto.Cipher import AES
import hashlib


def derive_key(shared_secret):

    # Derive a 256-bit AES key from the ML-KEM shared secret
    return hashlib.sha256(
        shared_secret
    ).digest()


def encrypt(message, shared_secret):

    # Generate AES key using the shared secret
    key = derive_key(shared_secret)

    # Create an AES cipher object in EAX mode
    cipher = AES.new(

        key,

        AES.MODE_EAX

    )

    # Encrypt the plaintext message
    ciphertext, tag = cipher.encrypt_and_digest(

        message.encode()

    )

    # Return the nonce and ciphertext to the sender
    return cipher.nonce, ciphertext


def decrypt(

        nonce,

        ciphertext,

        shared_secret

):

    # Generate the same AES key using the shared secret
    key = derive_key(shared_secret)

    # Recreate the AES cipher using the received nonce
    cipher = AES.new(

        key,

        AES.MODE_EAX,

        nonce=nonce

    )

    # Decrypt the received ciphertext
    plaintext = cipher.decrypt(

        ciphertext

    )

    # Convert decrypted bytes into readable text
    return plaintext.decode()
