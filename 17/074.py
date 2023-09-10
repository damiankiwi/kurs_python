import hashlib

def haszowanie_md5(slowo):
    hasz_md5 = hashlib.md5(slowo.encode()).hexdigest()
    return hasz_md5

def haszowanie_sha1(slowo):
    hasz_sha1 = hashlib.sha1(slowo.encode()).hexdigest()
    return hasz_sha1

def haszowanie_sha256(slowo):
    hasz_sha256 = hashlib.sha256(slowo.encode()).hexdigest()
    return hasz_sha256

slowo = input("Podaj słowo do zahaszowania: ")

md5 = haszowanie_md5(slowo)
sha1 = haszowanie_sha1(slowo)
sha256 = haszowanie_sha256(slowo)

print(f"MD5: {md5}")
print(f"SHA-1: {sha1}")
print(f"SHA-256: {sha256}")