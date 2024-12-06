import lsx

for path in lsx.walk('H'):
    data = lsx.readb(path)
    if data.startswith(b'REV'):
        mtime = lsx.file_mtime(path)
        lsx.write(path, bytes(reversed(data[3:])))
        lsx.file_utime(path, mtime)
