import os
import lsx

files = {}
for path in lsx.walk('H'):
    hash = os.path.getsize(path), lsx.md5(path)
    files.setdefault(hash, []).append(path)

print('Repeat files:')
for paths in files.values():
    if len(paths) > 1:
        print('-' * 12)
        print('\n'.join(paths))
print('-' * 12)

print()
input('Delete later files (press enter): ')
print('-' * 12)
for paths in files.values():
    for path in paths[1:]:
        os.remove(path)
        print(path)
print('-' * 12)
print('Delete files success!')
