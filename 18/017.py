def findStrobogrammatic(n):
    def generateStrobogrammaticHelper(n, m):
        if n == 0:
            return [""]
        if n == 1:
            return ["0", "1", "8"]

        inner = generateStrobogrammaticHelper(n - 2, m)
        result = []

        for num in inner:
            if n != m:
                result.append("0" + num + "0")
            result.append("1" + num + "1")
            result.append("6" + num + "9")
            result.append("8" + num + "8")
            result.append("9" + num + "6")

        return result

    if n == 0:
        return []
    return generateStrobogrammaticHelper(n, n)

n1 = 2
n2 = 3

result1 = findStrobogrammatic(n1)
result2 = findStrobogrammatic(n2)

print(result1)
print(result2)
