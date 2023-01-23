import os

path = input("Path/filename of CSV >")

f = open(path, "r")
path = f.name
# print(name)
if not path.endswith(".csv"):
    print("Only .csv files are supported")
    exit(1)
fileString = f.read()
fileParsed = [i.split(",") for i in fileString.split("\n")]
# print(fileParsed)
f.close()
# now to get filename and the iterator names
# name = fileParsed[0][0]
iterators = fileParsed[0]
# print(name)
# print(iterators)

outputData = "["

for i in fileParsed[1:]:
    # put key here:
    outputData += '{'
    for j in range(len(iterators)):
        outputData += '"' + iterators[j] + '":"' + i[j] + '",'
    outputData = outputData[:-1] + "},"
outputData = outputData[:-1] + "]"

outputPath = path[:-3] + "json"
# print(outputPath)
output = open(outputPath, "w")
output.write(outputData)
output.close()
print("wrote data from " + path + " to " + outputPath)