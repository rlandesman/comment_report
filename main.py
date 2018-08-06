import io

isComment = False
x = 0

with open('python_sample.py') as input:
    for line in input:
        isComment == False
        for char in line:
            if char == "#":
                isComment = True
            else:
                pass
        if (isComment == True):
            x = x + 1
print(x)
