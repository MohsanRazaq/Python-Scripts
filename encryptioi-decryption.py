import rsa
from cryptography.fernet import Fernet
public_key,private_key=rsa.newkeys(512)

msg='mohsan is best hackeru will see sooN '
enc=rsa.encrypt(msg.encode(),public_key)
dec=rsa.decrypt(enc,private_key)
print(f'The text is : {msg}\nthe Encrypted val is: {enc}\n the Decrption is: {dec}')