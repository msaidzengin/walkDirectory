import os
from glob import glob

path = os.getcwd()

result = []
for entry in os.walk(path):
    directory = entry[0]
    for match in glob(os.path.join(directory, "*.txt")):
        result.append(match)

with open("allfiles.txt", "a", encoding="utf-8") as output:
    for file_path in result:
        print(file_path)
        output.write(file_path + "\n")
