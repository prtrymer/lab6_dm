def task1():
    f1 = "p∨q"
    f2 = "p→r"
    f3 = "q→s"
    g = "¬r∨¬s"
    print(resolrule(knf(f1) + knf(f2) + knf(f3) + knf(g)))


def task2():
    print(unification("W={Q(a,y), Q(x,f(b))}"))

def knf(f):
    a = ""
    if f[1] == "→":
        a = f.replace("→", "∨")
        a = "¬" + a
    else:
        a = f
    return a


def resolrule(f):
    a = ["p", "q", "r", "s"]
    b = ["¬p", "¬q", "¬r", "¬s"]
    for i in range(len(a)):
        if a[i] and b[i] in f:
            f = f.replace(a[i], '')
        if a[i] in f:
            return "Method of resolutions can't be done"
        else:
            return "Method of resolutions can be done"


def unification(disjunct):
    predicatsRaw = disjunct.split('W={')
    predicats = predicatsRaw[1].replace('}', '').split(", ")
    predicat1 = predicats[0]
    predicat2 = predicats[1]

    result = ""
    predicat1Cursor = 0
    predicat2Cursor = 0
    replacement = []
    while predicat1Cursor < len(predicat1) or predicat2Cursor < len(predicat2):
        if not predicat1[predicat1Cursor] == predicat2[predicat2Cursor]:
            #якщо зміна в першому предиканті
            if predicat1[predicat1Cursor] == 'x' or predicat1[predicat1Cursor] == 'y':
                predicat2Element = returnElement(predicat2Cursor, predicat2)
                replacement.append(predicat1[predicat1Cursor] + "/" + predicat2Element)
                predicat1 = predicat1.replace(predicat1[predicat1Cursor], predicat2Element)
                result += predicat2Element
                predicat2Cursor += len(predicat2Element)
                predicat1Cursor += len(predicat2Element)
            #якщо змінна в другому предиканті
            elif predicat2[predicat2Cursor] == 'x' or predicat2[predicat2Cursor] == 'y' or predicat2[predicat2Cursor] == 'z':
                predicat1Element = returnElement(predicat1Cursor, predicat1)
                replacement.append(predicat2[predicat2Cursor] + "/" + predicat1Element)
                predicat2 = predicat2.replace(predicat2[predicat1Cursor], predicat1Element)
                result += predicat1Element
                predicat1Cursor += len(predicat1Element)
                predicat2Cursor += len(predicat1Element)
            #якщо в першому предиканті функція
            elif predicat1[predicat1Cursor] == 'f' or predicat1[predicat1Cursor] == 'g':
                predicat1Function = returnElement(predicat1Cursor, predicat1)
                result += predicat1Function
                replacement.append(predicat2[predicat2Cursor] + "/" + predicat1Function)
                predicat1Cursor += len(predicat1Function)
                predicat2Cursor += 1
            #якщо в другому предиканті функція
            elif predicat2[predicat2Cursor] == 'f' or predicat2[predicat2Cursor] == 'g':
                predicat2Function = returnElement(predicat2Cursor, predicat2)
                result += predicat2Function
                replacement.append(predicat1[predicat1Cursor] + "/" + predicat2Function)
                predicat2Cursor += len(predicat2Function)
                predicat1Cursor += 1
        else:
            result += predicat1[predicat1Cursor]
            predicat1Cursor += 1
            predicat2Cursor += 1
    return "W={" + result + "}" + ", " + replacementToString(replacement)


#вертає елемент предиканта, перший символ якого лежить в ячейке комірка i
def returnElement(i, predicat):
    for j in range(i, len(predicat)):
        nextCommaPosition = predicat.find(',', i)
        return predicat[i:nextCommaPosition]

def replacementToString(replacement):
    replacementString = "δ={"
    for i in range(len(replacement)):
        if not i == len(replacement) - 1:
            replacementString += replacement[i] + ','
        else:
            replacementString += replacement[i]
    replacementString += '}'
    return replacementString


print("Task 1:")
task1()
print("Task 2:")
task2()
