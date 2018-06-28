print("teste")
a = 3 ** 2
print(type(a), " - ", a)
b = "Nome: {one} -> {two}"
c = "Tissu"
print(b.format(one = c, two = "teste"))
lista = [1.0, "teste", [1, 2, 3]]
print(lista[2])
print(lista[2][1]) #posição exata
print(lista[1:]) #inicia ate o fim
print(lista[:1]) #na lista ate a posição apontada
print(lista[0:1]) #começa do 0 até o 1 mas desconsidera o 1
print(b[:3]) #como se fosse copy
dic = {'valor1':1, 'valor2':2}
print(dic['valor2'])
t = (1, 2, 3) #objetos tupla sao listas somente leitura
print(type(t), t[0])
print(1==1)
