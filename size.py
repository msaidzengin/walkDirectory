import os
from glob import glob

path = os.getcwd()

result = []
for entry in os.walk(path):
    directory = entry[0]
    for match in glob(os.path.join(directory, "*")):
        result.append(match)

sizes = {}
for file_path in result:
    try:
        sizes[file_path] = os.path.getsize(file_path)
    except:
        sizes[file_path] = 0

sorted_sizes = {
    file_path: size
    for file_path, size in sorted(sizes.items(), key=lambda item: item[1])
}

with open("sizes.txt", "a", encoding="utf-8") as output:
    for file_path, size in sorted_sizes.items():
        output.write(str(size) + " - " + file_path + "\n")
