import copy
class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Node:
    def __init__(self, dado):
        self._carga = dado
        self._proximo = -1
        
    def get_proximo(self):
        return self._proximo

    def set_proximo(self, valor):
        self._proximo = valor

    def get_carga(self):
        return self._carga

    def set_carga(self, nova_carga):
        self._carga = nova_carga
       
    
    def __str__(self):
        return f'[{self._carga} | {self._proximo}] '



class Lista:
   def __init__(self):
      self._vetor = []
      self._head = None
   def rem_no(self, posicao):
        del self._vetor[posicao]

   def estaVazia(self):
       return True if self.tamanho() == 0 else False
   
   def elemento(self, elemento):
        if self.tamanho() == 0:
                raise ListaException(f'Lista vazia')
        try:
            assert elemento >= 0 and elemento <= self.tamanho() 
            cursor = self._head
            contador = 1
            while (cursor != -1 and contador < elemento):
                contador += 1
                cursor = self._vetor[cursor].get_proximo()
            return self._vetor[cursor].get_carga()
        except AssertionError:
           raise AssertionError(f'Está Posição não está na lista')
        

           
   def tamanho(self):
        return len(self._vetor)
        
   def busca(self, valor):
        if(self.estaVazia()):
           raise ListaException(f'A lista está vazia')
        cursor = self._head
        contador = 1
        while (cursor != -1 and contador <= self.tamanho()):
                if self._vetor[cursor].get_carga() == valor:
                    return contador
                contador += 1
                cursor = self._vetor[cursor].get_proximo()
        raise ListaException(f'Este valor não está na')

            
        
   
   def inserir_inicio(self, valor ):
        novo = Node(valor)
        if self.tamanho() == 0:
            self._head = self.tamanho()-1

        novo.set_proximo(self._head) 
        self._head = self.tamanho()
        self._vetor.append(novo) 
       

   def inserir_final(self, valor ):
        novo = Node(valor)
        if self.tamanho() == 0:
            self.inserir_inicio(valor)

        else:
            novo = Node(valor)
            posicao_insercao = self.tamanho()
            i = copy.deepcopy(self._head)
            while True:
                if (self._vetor[i].get_proximo() == -1):
                    self._vetor[i].set_proximo(posicao_insercao)
                    self._vetor.append(novo)
                    break
                else:
                    i = copy.deepcopy(self._vetor[i].get_proximo())

   def trocar_ordem(self, posicao_elem_1, posicao_elem_2):
        try:
            if self.tamanho() == 0:
                raise ListaException(f'Lista está vazia')
            if self.tamanho() >= 2:
                if posicao_elem_1 != posicao_elem_2:
                    elemento1 = self._vetor[posicao_elem_1-1]
                    elemento2 = self._vetor[posicao_elem_2-1]
                    auxiliar = elemento1.get_proximo()
                    elemento1.set_proximo(elemento2.get_proximo())
                    elemento2.set_proximo(auxiliar)
                    self._vetor[posicao_elem_2-1] = elemento1 
                    self._vetor[posicao_elem_1-1] = elemento2
                    if elemento1 == self._head:
                        self._head = elemento2
                    elif elemento2 == self._head:
                        self._head = elemento1

        except IndexError:
            raise IndexError(f'Posição inválida que foi passada não está dentro da lista')
        
   
    
   def remover_final(self):
        if self.tamanho() == 0:
           raise ListaException(f'Lista está vazia')
        

                
        
        

            
   def remover_inicio(self):
        if self.tamanho() == 0:
           raise ListaException(f'Lista está vazia')
        

    
   
   def remover_tudo(self):
            if self.tamanho() == 0:
                raise ListaException(f'Lista já está  vazia')
            self._head = None
            self._vetor.clear()
            
            
    
   def __str__(self):
        s = ''
        cursor = self._head
        if self.tamanho() == 0:
            s += '[]'
        else:
            while (cursor != -1):
                s += f'[{self._vetor[cursor].get_carga()} | {self._vetor[cursor].get_proximo()}] '
                cursor = self._vetor[cursor].get_proximo()
        return s

                
