import copy
class NoPilha(object): #implementação do nó
    def __init__(self, valor):  #quando criar o nó ele vai ser inicializado com um valor

        self.__valor = valor 
        self.__proximo = None #quando se instanciar o nó, vai receber um valor none e inicialmente apontar para um vazio.

    def set_proximo(self, no):

        self.__proximo = no #o nó por padrão vai guardar o valor e vai apontar o próx nó da pilha. método que define o prox no da fila.

    def get_proximo(self): #não recebe argumentos pq só retorna o próximo nó

        return self.__proximo

    def get_valor(self):

        return self.__valor

class PilhaEncadeada(object):

    def __init__(self):
        self.__topo = None #pilha inicialmente vazia, atributo topo apontando pro nó
    
    def empilhar(self, no): #p/ adc um novo nó na pilha
        if self.__topo is None:
            self.__topo = no #verificar se a pilha ta vazia, se estiver pode-se dizer que o nó do topo eh o nó atual
         #uma forma de saber se o nó é o fundo da pilha, o prox item que ele vai tá atrelado é nada
        else:
            topo_anterior = copy.deepcopy(self.__topo) 
            self.__topo = no
            self.__topo.set_proximo(topo_anterior)
    
    def desempilhar(self):
        if self.__topo is None:
            print('Pilha Vazia')
        else:
            proximo_no = copy.deepcopy(self.__topo.get_proximo())

            topo_atual = self.__topo

            self.__topo = proximo_no

            return topo_atual
    
    def imprime_pilha(self):
        if self.__topo is None:
            print('Pilha está vazia')
        else:
            proximo_no= []
            tam = 0

            no_atual = self.__topo

           
            while proximo_no is not None: #verificando se o prox nó nao está vazio
                proximo_no = no_atual.get_proximo() #prox nó eh o no atual 
                print('Pos ', tam, 'val', no_atual.get_valor())
                no_atual = proximo_no  
                tam += 1

