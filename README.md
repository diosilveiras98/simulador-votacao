#Simulador de Votação para Síndico

##Como me usar: 
**1-Inicialização em um terminal python;
**2-As unicas entradas cabiveis são das opções apresentadas em tela[1,2,3,4,5,6,7,8,9,0 e 99]; 
**3-Para encerrar a votação deve-se digitar o código [99]
**4-A tebala de resultados é exibida em tela juntamente com o vencedor

Este projeto é um simulador de votação desenvolvido em **Python**, com foco no treinamento de conceitos fundamentais de programação como:

- Estruturas de decisão
- Estruturas de repetição
- Acumuladores
- Lógica de controle de fluxo
- Entrada e processamento de dados


##Estrutura do sistema

**O software foi estruturado em três fases principais:**

### 1. Inicialização
- Criação dos acumuladores de votos para cada candidato
- Exibição das opções disponíveis para votação

### 2.**Fluxo Principal** 
- Uma estrutura de condições [Se, Senão Se e Senão] envolvida pelo laço de repetição [while] que juntamente com nosso código sentinela [99] e o [break] formão o fluxo desejado para a solução desejada respectivamente; cotabilizando o voto de cada candidato e imprimindo a mensagem que informa o exito de cada voto[Voto computado para X], envolvendo toda a lógica desse trecho em uma repetição e nova entrada de voto até que nosso sentinela[99] seja invocado e coleta dos acomuladores dos votos se encerre através do break.

### 3.**Processamento do Relatório** 
- Impressão do relatório completo com total de votos por candidato
- Estrutura lógica para definição do vencedor
- Tratamento de empate técnico

##Tecnologias Utilizadas:
**Python**
**VsCode**

##lógica de decisão

Para vencer, o candidato tem que ter **mais votos que todos os outros**. Se ocorre um empate entre os candidatos, o código retorna como **Empate Técnico**!

```python

   #**#exemplo**

if candidato_a > candidato_b and candidato_a > candidato_c and candidato_a > candidato_d and candidato_a > candidato_e and candidato_a > candidato_f and candidato_a > candidato_g and candidato_a > candidato_h and candidato_a > candidato_i and candidato_a > anular_voto:

    print(f'|||||| Candidato A Venceu!! ||||||')

else:
    print(f'Houve um EMPATE técnico!')





