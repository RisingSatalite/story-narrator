import os

folder_path = 'story'
files = os.listdir(folder_path)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    print(file_path)
