import time

def fibonacci(idx):
    seq = [0,1]
    for i in range(idx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]

def Fibonacci(idx):
    if idx <= 1:
        return idx
    else:
        return Fibonacci(idx - 1) + Fibonacci(idx - 2)

print("Recursion")
rec = time.time()
print(Fibonacci(30))
print("Speed :" + str(time.time()-rec))

print("Iteration")
it = time.time()
print(fibonacci(30))
print("Speed :" + str(time.time()-it))