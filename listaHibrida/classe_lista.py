#busca, inserir final, remover início e remover final

class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Node:
    def __init__(self, dado = int):
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
      self._tamanho = 0
   
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
                for i in range(self.tamanho()):
                    novo_no = self._vetor[i]
                    if novo_no.get_proximo() == cursor.get_proximo()-1:
                        cursor = novo_no
                contador += 1
            return cursor
        except AssertionError:
           raise AssertionError(f'Está Posição não está na lista')
        '''try:
           if self.tamanho() == 0:
               raise ListaException(f'Lista vazia')
           assert elemento >= 0 and elemento <= self.tamanho() 
           return self._vetor[elemento]
       except AssertionError:
           raise AssertionError(f'Está Posição não está na lista')'''

           
   def tamanho(self):
        return self._tamanho
        
   def busca(self, valor):
        if(self.estaVazia()):
           raise ListaException(f'A lista está vazia')
        cursor = self._head
        contador = self._tamanho
        while (contador != -1):
            if cursor == valor:
                return contador
            contador -= 1
            cursor = cursor.get_proximo()
        raise ListaException(f'Este valor não está na lista')
            
        
   
   def inserir_inicio(self, valor ):
        novo = Node(valor)
        novo.set_proximo(self.tamanho()-1)
        self._head = novo
        self._vetor.append(novo)
        self._tamanho += 1          
       

   def inserir_final(self, valor ):
    novo = Node(valor)
    if(self.estaVazia()):
        raise ListaException(f'A lista está vazia')
    novo.set_proximo(self._head)
    self._head = novo        

   def trocar_ordem(self, posicao_elem_1, posicao_elem_2):
        try:
            if self.tamanho() == 0:
                raise ListaException(f'Lista está vaziaaa')
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
            self._tamanho = 0
            
    
   def __str__(self):
        cursor = self._head
        s = ''
        if self.estaVazia():
            s = "[]"
            return s
        else:
            contador = 0
            while contador < self.tamanho():
                s += f' ({cursor.get_carga()}| {cursor.get_proximo()})'
                for i in range(self.tamanho()):
                    novo_no = self._vetor[i]
                    if novo_no.get_proximo() == cursor.get_proximo()-1:
                        cursor = novo_no
                contador += 1
        return f' [ {s} ]'

                
               

    
            
