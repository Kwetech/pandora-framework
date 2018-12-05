import hashlib

def encrypt(hash_type, text):
    if hash_type == "md5":
        hash_text = hashlib.md5(text.encode("utf-8")).hexdigest()
    elif hash_type == "sha1":
        hash_text = hashlib.sha1(text.encode("utf-8")).hexdigest()
    elif hash_type == "sha224":    
        hash_text = hashlib.sha224(text.encode("utf-8")).hexdigest()
    elif hash_type == "sha256":
        hash_text = hashlib.sha256(text.encode("utf-8")).hexdigest()
    elif hash_type == "sha384":
        hash_text = hashlib.sha384(text.encode("utf-8")).hexdigest()
    elif hash_type == "sha512":
        hash_text = hashlib.sha512(text.encode("utf-8")).hexdigest()

    else:
        hash_text = "\33[91m[-]\33[00m" + "hash type not found"

    print("=>  " + hash_text)
    