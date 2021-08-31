from pilhaEncadeada import *

p = PilhaEncadeada()

no1 = NoPilha(10)
no2 = NoPilha(8)
no3 = NoPilha(50)
no4 = NoPilha(3)


p.empilhar(no1)
p.empilhar(no2)
p.empilhar(no3) 
p.empilhar(no4) 

p.imprime_pilha() #alocando na ordem que a posição anterior tava

p.desempilhar()
# p.desempilhar()
# p.desempilhar()
# p.desempilhar() = 'Pilha está vazia' 

print('-----------')

p.imprime_pilha()


#O último a entrar eh o primeiro a sair 






