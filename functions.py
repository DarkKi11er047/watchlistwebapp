FILENAME= "stuff.txt"

def readfile(filename=FILENAME):
    with open(filename, "r") as file:
        lst_w = file.readlines()
        return lst_w


def writefile(list1,filename=FILENAME):
    with open(filename, "w") as file:
        file.writelines(list1)


def showinglist():
    lst = readfile()
    for i, name in enumerate(lst):
        name = name.strip("\n")
        row = f"{i + 1}-{name}"
        print(row)


if __name__ == "__main__":
    print(readfile())