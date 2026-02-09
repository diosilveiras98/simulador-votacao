
#1.Inicialização dos contadores de votos(Acumuladores)

candidato_a = 0
candidato_b = 0
candidato_c = 0
candidato_d = 0
candidato_e = 0
candidato_f = 0
candidato_g = 0
candidato_h = 0
candidato_i = 0
anular_voto = 0

#<---Inicio do programa(saída em tela)--->
print('############# Votação Sindico do Prédio #############')
print('Opções:Candidato A = 1 | Cantidato B = 2 | Canditado C = 3 | Canditado D = 4 | Candida E = 5 \n | Candidato F = 6 | Candidato G = 7 | Candidato H = 8 | Candidato I = 9 | ANULAR VOTO = 0')
print()


#2.Fluxo Principal de captura de votos
#<--Neste trecho o loop fica ativo até que nossa (SENTINELA) seja invocada-->
voto_candidato = 0

while voto_candidato != 99:
    
    voto_candidato = int(input('Digite seu voto:'))

#<---Processamento de entrada--->
#Contabilizador de voto por candidato utilizando uma estrutura de condição Se, Senão Se e Senão
    
    if voto_candidato == 1:
        candidato_a = candidato_a + 1
        print(f'Voto computado para A')
        
    elif voto_candidato == 2:
        candidato_b = candidato_b + 1
        print(f'Voto computado para B')
        
    elif voto_candidato == 3:
        candidato_c = candidato_c + 1
        print(f'Voto computado para C')

    elif voto_candidato == 4:
        candidato_d = candidato_d + 1
        print(f'Voto computado para D')

    elif voto_candidato == 5:
        candidato_e = candidato_e + 1
        print(f'Voto computado para E')

    elif voto_candidato == 6:
        candidato_f = candidato_f + 1
        print(f'Voto computado para F')

    elif voto_candidato == 7:
        candidato_g = candidato_g + 1
        print(f'Voto computado para G')

    elif voto_candidato == 8:
        candidato_h = candidato_h + 1
        print(f'Voto computado para candidato H')

    elif voto_candidato == 0:
        anular_voto = anular_voto + 1
        print(f'Voto computado para votos nulos')
        
    
    elif voto_candidato == 9:
        candidato_i = candidato_i + 1
        print(f'Voto computado para candidato I')

       #Sentinela, esse código é responsável por finalizar a votação através do (break) a instrução é que seja realizado pelo cordenador/auditor da votação 
    elif voto_candidato == 99:
        break  # Sai do loop apenas se for 99
    else:
        print("Opção inválida! Digite um número da lista.")

#3.Relatório de Resultdados e indicação do vencedor
#Neste trecho é impresso o ultimo valor atualizado de cada variavel(candidato) após a finalização da votação(99) 

print(f'##################################################')
print(f'#####Total de votos Candidato A {candidato_a}#####')
print(f'#####Total de votos Canditado B {candidato_b}#####')
print(f'#####Total de votos Candidato C {candidato_c}#####')
print(f'#####Total de votos Candidato D {candidato_d}#####')
print(f'#####Total de votos Candidato E {candidato_e}#####')
print(f'#####Total de votos Candidato F {candidato_f}#####')
print(f'#####Total de votos Candidato G {candidato_g}#####')
print(f'#####Total de votos Candidato H {candidato_h}#####')
print(f'#####Total de votos Candidato I {candidato_i}#####')
print(f'#####Total de votos Nulos {anular_voto}      #####')
print(f'##################################################')


#<---Indicação do Vencedor--->
#Utiliza-se novamente uma estrutura condicional para determinar o vencedor

if candidato_a > candidato_b and candidato_a > candidato_c and candidato_a > candidato_d and candidato_a > candidato_e and candidato_a > candidato_f and candidato_a > candidato_g and candidato_a > candidato_h and candidato_a > candidato_i and candidato_a > anular_voto:
    print(f'|||||| Candidato A Venceu!! ||||||')


elif candidato_b > candidato_a and candidato_b > candidato_c and candidato_b > candidato_d and candidato_b > candidato_e and candidato_b > candidato_f and candidato_b > candidato_g and candidato_b > candidato_h and candidato_b > candidato_i and candidato_b > anular_voto:
    print(f'|||||| Candidato B Venceu!! ||||||')

elif candidato_c > candidato_a and candidato_c > candidato_b and candidato_c > candidato_d and candidato_c > candidato_e and candidato_c > candidato_f and candidato_c > candidato_g and candidato_c > candidato_h and candidato_c > candidato_i and candidato_c > anular_voto:
    print(f'|||||| Candidato c Venceu!! ||||||')

elif candidato_d > candidato_a and candidato_d > candidato_b and candidato_d > candidato_c and candidato_d > candidato_e and candidato_d > candidato_f and candidato_d > candidato_g and candidato_d > candidato_h and candidato_d > candidato_i and candidato_d > anular_voto:
    print(f'||||| !!Candidato D Venceu!! |||||')

elif candidato_e > candidato_a and candidato_e > candidato_b and candidato_e > candidato_c and candidato_e > candidato_d and candidato_e > candidato_f and candidato_e > candidato_g and candidato_e > candidato_h and candidato_e > candidato_i and candidato_e > anular_voto:
    print(f'||||| !!Candidato E Venceu!! |||||')

elif candidato_f > candidato_a and candidato_f > candidato_b and candidato_f > candidato_c and candidato_f > candidato_d and candidato_f > candidato_e and candidato_f > candidato_g and candidato_f > candidato_h and candidato_f > candidato_i and candidato_f > anular_voto:
    print(f'||||| !!Candidato F Venceu!! |||||')

elif candidato_g > candidato_a and candidato_g > candidato_b and candidato_g > candidato_c and candidato_g > candidato_d and candidato_g > candidato_e and candidato_g > candidato_f and candidato_g > candidato_h and candidato_g > candidato_i and candidato_g > anular_voto:
    print(f'||||| !!Candidato G Venceu!! |||||')

elif candidato_h > candidato_a and candidato_h > candidato_b and candidato_h > candidato_c and candidato_h > candidato_d and candidato_h > candidato_e and candidato_h > candidato_f and candidato_h > candidato_g and candidato_h > candidato_i and candidato_h > anular_voto:
    print(f'||||| !!Candidato H Venceu!! |||||')

elif candidato_i > candidato_a and candidato_i > candidato_b and candidato_i > candidato_c and candidato_i > candidato_d and candidato_i > candidato_e and candidato_i > candidato_f and candidato_i > candidato_g and candidato_i > candidato_h and candidato_i > anular_voto:
    print(f'||||| !!Candidato I Venceu!! |||||')

elif anular_voto > candidato_a and anular_voto > candidato_b and anular_voto > candidato_c and anular_voto > candidato_d and anular_voto > candidato_e and anular_voto > candidato_f and anular_voto > candidato_g and anular_voto > candidato_h and anular_voto > candidato_i:
    print(f'||||| !!Votos Nulos foram a maioria!! |||||')

else:
    print(f'Houve um EMPATE técnico!')

print(f'Votação encerrada!') 



