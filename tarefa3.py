listaCaractere = ["mesa", "cadeira", "cadeira"]
listaInteiro = [1, 5, 7, 9, 3, 5]
listaBooleano = [True, False, False]

listaInteiro.sort()
listaCaractere = [("mesa", 3), ("cadeira", 2), ("cadeira", 3)]

def chave(membro):
    return membro[1]
    
listaCaractere.sort(key=chave)

print (listaCaractere)
print (listaInteiro)
print (listaBooleano)

listaCaractere.append("copo")
listaInteiro.insert(8, 1)
listaInteiro.remove(5)
print(listaBooleano.pop(0))
print (listaCaractere)
del listaCaractere[2]
print (listaCaractere)
print (listaInteiro)
print (listaBooleano)

listaInteiro.append(0)
print("Lista depois do append: ", listaInteiro)
print("Elemento removido: ", listaInteiro.pop())
print("Lista depois do pop: ", listaInteiro)
