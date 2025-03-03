from random import randint

pathLength = 10
path = [1]
currentStep = path[0]
for i in range (pathLength):
    number = randint(1,2)
    currentStep+= number
    path.append(currentStep)

print(path)
