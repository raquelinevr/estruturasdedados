# Implementação de uma Fila Encadeada

import copy
class NoFila:
    def __init__(self, valor = None):
        if valor is not None:
            self.__valor = valor #se passar o valor, vai receber e colocar dentro do objeto
        else:
            self.__valor = None #se não passar nenhum valor, vai setar o valor pra nada

        self.__proximoNo = None #valor que vai manter a referencia, incicialmente None

    def get_valor(self):
        return self.__valor

    def set_valor(self, valor):
        self.__valor = valor

    def get_proximo_no(self):
        return self.__proximoNo

    def set_proximo_no(self,no):
        self.__proximoNo = no

class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def get_tamanho_fila(self):
        return self.__tamanho

    def incrementar_tamanho(self):
        self.__tamanho =+1

    def decrementar_tamanho(self):
        self.__tamanho = -1

    def set_inicio(self,no):
        self.__inicio = no

    def get_inicio(self):
        return self.__inicio

    def set_fim(self, no):
        self.__fim = no

    def get_fim(self):
        return self.__fim

    def enfileirar(self, valor):
        if self.get_tamanho_fila() == 0:
            novo_no = NoFila(valor) #criando um novo no pra fila com o valor que vai ser passado no teste (main) com, executar a classe e retornar um novo nó.
            novo_no.set_proximo_no(None)
            self.set_inicio(novo_no) #se a fila ta vazia, esse nó vire o inicio da vazia
            self.set_fim(novo_no) 
            self.incrementar_tamanho()

        else:
            novo_no = NoFila(valor)
            novo_no.set_proximo_no(None) #o novo no que está entrando seja nulo, aponte para o final da fila

            self.get_fim().set_proximo_no(novo_no) #pega o inicio da fila e coloca o novo nó na fila *

            self.set_fim(novo_no) #o fim vai está apontando para o novo nó

            self.incrementar_tamanho()

    def desenfileirar(self):
        if self.get_tamanho_fila() > 0:
            proxs_nos = copy.deepcopy(self.get_inicio().get_proximo_no()) #pegando o prox no da fila, e guarda a referencia
            no_removido = self.get_inicio()
            self.set_inicio(proxs_nos)

            return no_removido

    def imprime_fila(self):
            # if self.get_tamanho_fila() == 0:
            #     raise FilaException('Fila vazia!')
        if self.get_tamanho_fila() > 0:
            proximo_no = []
            pos = 1 #posicao inicial eh 1
            no_atual = self.get_inicio() #pegando o primeiro no da fila pra começar a impressão

            while proximo_no is not None: 
                proximo_no = no_atual.get_proximo_no()
                print('Pos: ', pos, 'val: ', no_atual.get_valor())
                no_atual = proximo_no
                pos +=1
                
               
