import os

path = '.'

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    file_size = os.path.getsize(file_path)
    print("Path: {}, File: {}, Size {} bytes".format(file_path, file, file_size))




