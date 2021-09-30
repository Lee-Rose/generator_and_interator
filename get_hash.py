import hashlib

def compute_MD5_hash(string, encoding='utf-8'):
    md5_hash = hashlib.md5()
    md5_hash.update(string.encode(encoding))
    return md5_hash.hexdigest()

with open('dzen.txt') as f:
    for line in f:
        print(compute_MD5_hash(line))