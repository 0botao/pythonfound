'''Módulo 1: Estrutura Sequencial

Imagine que você está dando instruções passo a passo para alguém realizar uma tarefa. Na programação, a estrutura sequencial funciona da mesma forma: cada linha de código é executada em
ordem, uma após a outra.

Conceitos Básicos

Variáveis: Pense nelas como caixas que armazenam valores. Podemos dar nomes a essas caixas (como idade, nome, preco) e guardar diferentes tipos de informação nelas.

Tipos de Dados:

Números: Inteiros (ex: 10, -5) e decimais (ex: 3.14, -0.5).

Strings: Sequências de caracteres entre aspas (ex: "Olá", "Python é legal!").

Booleanos: Representam valores verdadeiro (True) ou falso (False).

Operadores:

Aritméticos: + (soma), - (subtração), * (multiplicação), / (divisão), % (resto da divisão), ** (potência).

Lógicos: and (e), or (ou), not (não).

Entrada e Saída


input(): Permite que o usuário digite informações no programa.

print(): Exibe mensagens ou resultados na tela.

'''

# numero1 = float(input("Digite o primeiro número: "))  # Lê o primeiro número e converte para decimal
# numero2 = float(input("Digite o segundo número: "))   # Lê o segundo número e converte para decimal
# soma = numero1 + numero2                              # Calcula a soma
# print("A soma dos números é:", soma)                  # Exibe o resultado 

''' Crie um programa que peça o nome e a idade do usuário e exiba uma mensagem de boas-vindas personalizada. '''

nome = input(' digite o seu nome ')
idade = int(input(' digite a sua idade ')) 

print(f' seja bem vido {nome}')
