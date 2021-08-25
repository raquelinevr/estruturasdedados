
from typing import List, Type
from classe_lista import *
# Função escolha tem intuito de escolher a lista
def escolha_lista( escolha ):
        assert escolha <= len(vetores), "Está lista não se encontra, digite um número de 1 a 5"
        return vetores[escolha]
        
    
num_listas = 5 
vetores = {}
for i in range(num_listas):
    vetores[i+1] = Lista()
escolha = 1
while(True):
        escolha_de_vetor = escolha_lista(escolha)
        print('--------------------')
        print(f'lista {escolha} {escolha_lista(escolha)}')
        print('--------------------')
        print('(i) Inserir no Início') # ok 
        print('(f) Inserir no Final') # node nao eh um inteiro
        print('(b) Procurar um valor na lista') # retornando lista vazia
        print('(e) Consultar o conteúdo de um elemento') # 'int' object has no attribute 'get_proximo'
        print("(t) Trocar ordem dos elementos") #
        print('(v) Consultar se a lista está vazia')  
        print('(s) Obter tamanho da lista')  
        print('(r) Remover no início')  
        print('(o) Remover no Final')  
        print('(l) Remover todos os elementos da lista')  
        print('(p) Imprimir lista') 
        print('(m) mudar a lista') 
        print('(x) Sair do programa') 
        print('---------------------')
        try:
            opcoes = ["i", "f", "b", "e", "t", "v", "s", "r", "o", "l", "p", "m", "x" ]
            opcao = input('opcao:')
            opcao.lower()
            
            assert opcao in opcoes, "A opção digitada não está disponível"
            
            if opcao == "p" :
                try:
                    if escolha_de_vetor.tamanho() == 0:
                        print("Sua lista está vazia: ", escolha_de_vetor.estaVazia())
                    else:
                        print(escolha_de_vetor.__str__())
                except ListaException as le:
                    print(le)
            elif opcao == "m":
                try:
                    escolha = int(input("Digite um número entre 1 e 5: ")) 
                    escolha_de_vetor = escolha_lista(escolha)
                
                except ValueError:
                    print(f"O valor digitado não foi um número inteiro")
                
            elif opcao == "l":
                try:
                    escolha_de_vetor.remover_tudo()
                except ListaException as le:
                    print(le)
                    
            elif opcao == "b":
                try:
                    procura = int(input("Digite o elemento que deseja procurar na lista: "))
                    print(escolha_de_vetor.busca(procura))
                except TypeError :
                    print("o Valor digitado não é um inteiro")
                
                except ListaException as le:
                    print(le)

                except ValueError as ve:
                    print(ve)
                
                    
            elif opcao == "s":
                print(f' O seu tamanho é : {escolha_de_vetor.tamanho()}')
            
            elif opcao == "v":
                print(escolha_de_vetor.estaVazia())
            
            elif opcao == "x":
                print("Fim do programa")
                break

            elif opcao == "t":
                try:
                    posicao1 = int(input("Digite a primeira  posição: "))
                    posicao2 = int(input("Digite a segunda posição posição: ")) 
                    escolha_de_vetor.trocar_ordem(posicao1, posicao2)
                    print(f'a nova lista está assim: {escolha_de_vetor.__str__()}')
                except ValueError:
                    print("o valor digitado é uma string")
                except IndexError as ie:
                    print(ie) 
                except ListaException as le:
                    print(le)
                

            elif opcao == "e":
                try:
                    indice_vetor = int(input("Digite a poisção para ser procurado na lista: "))
                    print(f'o elemento encontrado que está nesse índice  é: {escolha_de_vetor.elemento(indice_vetor)}')
                except ValueError:
                    print("o valor digitado não é um inteiro")
                #except AssertionError as ae:
                    #print(ae)
                except ListaException as le:
                    print(le)
            
            elif opcao == "i":
                try:
                    valor_inicio = int(input("Digite o valor que você quer colocar no início: "))
                    escolha_de_vetor.inserir_inicio(valor_inicio)
                
                except ValueError as ve:
                    print(f"O valor digitado não foi um número inteiro")
            
            elif opcao == "f":
                try:
                    valor_final = int(input("Digite o valor que você quer colocar no final: "))
                    escolha_de_vetor.inserir_final(valor_final)
                    #print(escolha_de_vetor.__str__())
                except ValueError as ve:
                    print(f"O valor digitado não foi um número inteiro")
                except ListaException as le:
                    print(le)
            
            elif opcao == "r":
                try:
                    escolha_de_vetor.remover_inicio()
                except ListaException as le:
                    print(le)
                
            
            elif opcao == "o":
                try:
                    print(escolha_de_vetor.remover_final())
                except IndexError as ie:
                    print("Lista vazia")

            
            else:
                pass
        
        except AssertionError as ae:
            print(ae)
        
