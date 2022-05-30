sizes = input().split()
num1 = int(sizes[0])
num2 = int(sizes[1])
def domino_piling(a, b):
    return (a*b)//2
print(domino_piling(num1,num2))