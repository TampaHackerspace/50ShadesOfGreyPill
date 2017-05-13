import hashlib
import sys

filea = str(sys.argv[1])
fileb = str(sys.argv[2])

digests = []
for filename in [filea, fileb]:
    hasher = hashlib.md5()
    with open(filename, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
        a = hasher.hexdigest()
        digests.append(a)
        print(a)

print(digests[0] == digests[1])