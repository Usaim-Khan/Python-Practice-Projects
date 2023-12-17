# CALCULATE SIZE OF FOLDERS AND FILE
import os

# file size
# print(os.path.getsize('C:\\Users\\Asif Iqbal\\PycharmProjects\\UsaimPython\\Modules\\DateTime Module.py'))

# folder size
folder_path = 'C:\\Users\\Asif Iqbal\\PycharmProjects\\UsaimPython\\practices'
print(os.path.getsize(folder_path))

# folder size 2
size = 0
path = 'C:\\Users\\Asif Iqbal\\PycharmProjects\\UsaimPython\\practices'
file_names = os.listdir(path)

for file in file_names:
    full_path = os.path.join(path,file)

    size = size + os.path.getsize(full_path)

print(size)

# 2nd method is more accurate