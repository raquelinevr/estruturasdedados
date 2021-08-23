from typing import List


class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)




class ListaSequencial:

    def __init__(self):
        self.__dados = []

    def vazia(self):
        return len(self.__dados) == 0


    #def cheia(self):
       #pass 

    def tamanho(self):
        return (len(self.__dados))

    def busca(self, dado):
        ''''
        for i in range(self.__dados):
            if self.__dados[i] == dado:
                return i+1
            return None
        '''
        try:

            return self.__dados.index(dado) + 1
        except ValueError:
            raise ListaException(f'O valor {dado} não se encontra na lista')
        except:
            raise 



    def elemento(self, posicao):

        try:
            assert posicao > 0
            return self.__dados[posicao -1]
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except IndexError:
            raise ListaException('A posição informada para consulta é inválida')
        except:
            raise


    def inserir(self, posicao, dado):
        try:
            assert posicao > 0
            self.__dados.insert(posicao-1, dado)
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except IndexError:
            raise ListaException('A posição informada para consulta é inválida')
        except:
            raise


    def remover(self, posicao):
        try:
            assert posicao > 0
            if (self.vazia()):
                raise ListaException('Lista vazia. Não é possivel remover elementos. ')
            valor = self.__dados[posicao-1]
            del self.__dados[posicao-1]
            return valor 
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except IndexError:
            raise ListaException('A posição informada para consulta é inválida')
        except:
            raise


    def __str__(self):
        return self.__dados.__str__()

    def imprimir(self):
        print(self.__str__())

    def modificar(self, posicao, novoValor):
        try:
            assert posicao > 0
            if ( self.vazia()):
                raise ListaException('Lista vazia. Não é possivel remover elementos. ')
            self.__dados[posicao-1] = novoValor
            return True
        except TypeError:
            raise ListaException('O argumento posição deve ser um valor do tipo inteiro')
        except AssertionError:
            raise ListaException('Posição negativa não é válida para a lista')
        except IndexError:
            raise ListaException('A posição informada para consulta é inválida')
        except:
            raise



if (__name__ == '__main__'):
    print('Rodando o programa principal a partir da classe ListaSequencial')
    l1 = ListaSequencial()
 
    if (l1.vazia()):
        print('Lista está vazia')

    print('Tamanho: ', l1.tamanho())

    for i in range(10):
        l1.inserir(1,i*10)
    print(l1)

    valor = l1.remover(2)
    print(valor)
    print(l1)

    print()
    l1.imprimir()
    l1.modificar(5,44)
    l1.imprimir()

    #l1.inserir(-10,99)
    print(l1)

    try:
        #print(l1.busca(55))
        #print(l1.elemento(5))
        #l1.inserir(5,111)
        #l1.remover(1)
        l1.modificar(100,999)
        print(l1)
    except ListaException as li:
        print(li)