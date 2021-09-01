from filaEncadeada import *

fila = FilaEncadeada()


no = NoFila(10)

fila.enfileirar(10)
fila.enfileirar(5)
fila.enfileirar(150)
fila.imprime_fila()

fila.desenfileirar()
print('---------------')

fila.imprime_fila()
