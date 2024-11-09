import os

dirp = '/path/to/directory'
if not os.path.isdir(dirp):
    if os.path.exists(dirp):
        print(f"{dirp} is a file")
    else:
        print(f"{dirp} does not exist")
