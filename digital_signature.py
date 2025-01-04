from rsa import encrypt, decrypt

def sign(private_key, document):
    print("Signing document:", document)
    return encrypt(private_key, document)

def verify(public_key, document, signature):
    decrypted_signature = decrypt(public_key, signature)
    print("Verifying signature. Decrypted:", decrypted_signature)
    return decrypted_signature == document

