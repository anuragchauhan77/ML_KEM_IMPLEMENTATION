from Crypto.Cipher import AES
import hashlib


def derive_key(shared_secret):

    return hashlib.sha256(
        shared_secret
    ).digest()


def encrypt(message, shared_secret):

    key = derive_key(shared_secret)

    cipher = AES.new(

        key,

        AES.MODE_EAX

    )

    ciphertext, tag = cipher.encrypt_and_digest(

        message.encode()

    )

    return cipher.nonce, ciphertext


def decrypt(

        nonce,

        ciphertext,

        shared_secret

):

    key = derive_key(shared_secret)

    cipher = AES.new(

        key,

        AES.MODE_EAX,

        nonce=nonce

    )

    plaintext = cipher.decrypt(

        ciphertext

    )

    return plaintext.decode()