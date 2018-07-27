# %%
a = 1
b = 2
c = a + b
c
# %%
for i in range(1, 8):
    print (i)
# %%
def digiSum(n, sum):
    if (n > 0):
        sum += n % 10
        n = n // 10
        return digiSum(n, sum)
    else:
        return sum
digiSum(9725, 0)
# %%
13 % 10
13 // 10 % 10
13 // 10
1 // 10
# %%
def rootSum(n):
    if (n > 0 && n < 10):
        return n
    else:
        
