import os
import lsx

for path in lsx.walk('H'):
    root, name, ext = lsx.path_split(path)
    name2 = 'img_%04d%02d%02d_%02d%02d%02d' % lsx.file_mtime(path)
    path2 = os.path.join(root, name2 + ext.lower())
    if name != name2:
        path3 = lsx.path_unique(path2, '_')
        print(path, '->', path3)
        os.rename(path, path3)
