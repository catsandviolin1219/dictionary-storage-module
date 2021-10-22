## Only works with string data (for now...)
import json

## Writes a string to a text file, only for internal purposes.
def writeString(text, fileName="dict", overwriteFile=False):
    if (overwriteFile == False):
        file = open(fileName + ".txt", "a")
    else:
        file = open(fileName + ".txt", "w")
    file.write(text)
    file.close()

## Reads a string from a text file, only for internal purposes.
def readLine(line, fileName="dict"):
    file = open(fileName + ".txt", "r")
    lines = file.readlines()
    read = lines[line].rstrip("\n")
    file.close()
    return read

## Converts a dictionary to a string, with double-quotes.
def dictToStr(dict):
    newStr = "{"
    for i in dict:
        x = '"{}": "{}", '
        newStr = newStr + x.format(i, dict[i])
    newStr = newStr[0:len(newStr)-2] + "}\n"
    return newStr

## Converts a string to a dictionary, with double-quotes.
def strToDict(str):
    newDict = json.loads(str)
    return newDict

## Writes a dictionary to a text file.
def writeDict(dict, fileName="dict"):
    writeString(dictToStr(dict), fileName, False)

## Reads a dictionary from a text file.
def readDict(line, fileName="dict"):
    return strToDict(readLine(line, fileName))

## Finds the first index of a dictionary from a text file.
def indexDict(dict, fileName="dict"):
    file = open(fileName + ".txt", "r")
    index = 0
    for x in file:
        if (strToDict(x) == dict):
            return index
        else:
            index += 1
    raise Exception("Dictionary " + str(dict) + " not found.")

## Deletes the dictionary at the index from a text file.
def deleteDictIndex(i, fileName="dict"):
    with open(fileName + ".txt", "r") as file:
        lines = file.readlines()
    with open(fileName + ".txt", "w") as file:
        for x in range(0, len(lines)):
            if x != i:
                file.write(lines[x])

## Deletes the given dictionary from a text file.
def deleteDict(dict, fileName="dict"):
    deleteDictIndex(indexDict(dict, fileName), fileName)

## Gets all the dictionaries from a text file.
def getAll(fileName="dict"):
    file = open(fileName + ".txt", "r")
    lines = file.readlines()
    dicts = []
    for i in lines:
        dicts.append(strToDict(i))
    file.close()
    return dicts