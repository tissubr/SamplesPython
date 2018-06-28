seq = [1, 2, 3, 4, 5, 6]
for item in seq: 
    print(item)
#############################################################
for i in range(0, 10):
    print(type(range(0, 10)), i)
#############################################################
i = 0
while i < 5:
    print("i vale {}".format(i))
    i = i + 1
#############################################################
out = []
x = [1,2,3,4]
for item in x:
    out.append(item**2)
print(out)
#############################################################
[item2**2 for item2 in x]
print(x)
#############################################################
def Minha_func(param):
    print(type(param), " -> ", param)
Minha_func(1)
#############################################################
def Minha_func2(param):
    x = param ** 2
    return x
print(Minha_func2(3))
#############################################################
lambda var : var ** 2
#############################################################
seq = [1, 2, 3, 4, 5]
print(list(map(Minha_func2, seq))) 
print(list(map(lambda x:x**2, seq)))
print(list(filter(lambda item:item%2==0, seq)))#retornando somente pares
#############################################################
def contacachorro(string):
    return len(list(filter(lambda x:"cachorro" == x, string.lower().split())))
print(contacachorro("esse cachorro é mais rápido que o outro Cachorro"))