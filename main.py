import hashlib
import glob
import itertools

# def md5sum(filename):
#     h  = hashlib.md5()
#     b  = bytearray(128*1024)
#     mv = memoryview(b)
#     with open(filename, 'rb', buffering=0) as f:
#         while n := f.readinto(mv):
#             h.update(mv[:n])
#     return h.hexdigest()


# md5sum('UnityPlayer.dll')
folder = glob.glob("../checkfiles/*.*")
hashes = []

for file in folder:
    with open(file, 'rb') as getmd5:
        data = getmd5.read()
        gethash = hashlib.md5(data).hexdigest()
        # print("f: " + gethash)
        hashes.append(gethash)


for a, b in itertools.combinations(hashes, 2):
    if a == b:
        print(file)
    