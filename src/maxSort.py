lista = list()
while True:
    n = float (input())
    if n == 0:
        break
    lista.append(n)
    
nmax = lista[len(lista)//2+1]
for i in range(len(lista)//2+1, len(lista)):
    if nmax<lista[i]:
        nmax=lista[i]
print(nmax)
