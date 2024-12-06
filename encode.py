import lsx

for path in lsx.walk('H'):
    data = lsx.readb(path)
    if not data.startswith(b'REV'):
        mtime = lsx.file_mtime(path)
        lsx.write(path, b'REV' + bytes(reversed(data)))
        lsx.file_utime(path, mtime)
