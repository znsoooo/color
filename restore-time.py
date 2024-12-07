import re
import lsx

for path in lsx.walk('H'):
    matches = re.findall(r'(?:\D|^)(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})(?:\D|$)', lsx.stem(path))
    if matches:
        lsx.file_utime(path, map(int, matches[0]))
    else:
        print('Not found file time:', path)

lsx.pause()
