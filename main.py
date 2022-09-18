import hashlib
import glob





hashes = []
names = []
def gethash(folder):
    for file in folder:
        with open(file, 'rb') as getmd5:
            data = getmd5.read()
            gethash = hashlib.md5(data).hexdigest()
            hashes.append(gethash)
            names.append(file)

def copies():
    for i in range(len(hashes)):
        for j in range(i + 1, len(hashes)):
            if hashes[i] == hashes[j]:
                 print(names[i]," ",names[j])



