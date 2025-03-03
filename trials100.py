from random import randint

pathLength = 24

count = 0
n = 100 #sample size
for j in range(n):
    path = [1]
    currentStep = path[0]
    for i in range (pathLength):
        number = randint(1,2)
        currentStep+= number
        if currentStep == 25:
            count+= 1
            break
        else:
            path.append(currentStep)
    
print(count)
print(count/n)
