import hashlib

def get_hash(path,encoding='utf-8'):

    '''a generator that takes a file path.
    Returns the md5 hash of each line in the file on each iteration.'''

    md5_hash = hashlib.md5()
    with open(path) as f:
        while True:
            txt_line = f.readline()
            if not txt_line:
                break
            md5_hash.update(txt_line.encode(encoding))
            yield md5_hash.hexdigest()


format_text = get_hash('dzen.txt')

for item in format_text:
    print(item)


