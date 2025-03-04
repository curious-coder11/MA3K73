from random import randint

pathLength = 24

count = []
n = 1000 #sample size
for j in range(n):
    path = [1]
    currentStep = path[0]
    for i in range (pathLength):
        number = randint(1,2)
        currentStep+= number
        if currentStep == 25:
            count.append(1)
            break
        elif currentStep > 25:
            count.append(0)
            break
        else:
            path.append(currentStep)

print(count)
