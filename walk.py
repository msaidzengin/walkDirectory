import os
from glob import glob
from collections import Counter

path = os.getcwd()

result = []
for entry in os.walk(path):
    directory = entry[0]
    for match in glob(os.path.join(directory, "*")):
        result.append(match)

with open("allfiles.txt", "a", encoding="utf-8") as output:
    for file_path in result:
        output.write(file_path + "\n")

names = []
for file_path in result:
    names.append(file_path.split("\\")[-1])

counts = Counter(names)
sorted_counts = {
    name: count
    for name, count in sorted(counts.items(), key=lambda item: item[1])
}

with open("counter.txt", "a", encoding="utf-8") as output:
    for name, count in sorted_counts.items():
        output.write(name + " - " + str(count) + "\n")
