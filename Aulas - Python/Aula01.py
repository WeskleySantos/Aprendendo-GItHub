# Aula 1 - Fundamentos Básicos Variáveis e Operadores Aritiméticos

#Variáveis: Tipos Primitivos -> Inteiro(int), Real(float, Double), Str(String), Bollean(bool)
#Seguindo a sequência são: numeros inteiros, numeros com pontos flutuantes ex(10,08),[...]
#[...] Qualquer coisa escrita, Valores lógicos (Verdadeiro, Falso)

#Definindo variáveis

numeroInteiro = 10
numeroReal = 10.00     #Usa-se ponto no lugar da virgula.
texto = '10.00 reais'  #Usa se aspas para indicar que é uma String ou seja somente Texto.
valorLogico = True

#para se mostrar o valor de uma varável usa-se o comando print()
#Tudo que está entre aspas são apenas textos para facilitar o entendimento do que se mostra na tela;
#Usa se também a virgula para concatenar, ou seja separar o texto de outras informações.
print('Valor da variável é ', numeroReal)


#Caso você não saiba o tipo certo da variável, pode se usar o comando type() EX:

print('o Tipo dessa variave é ', type(numeroInteiro))  #print() -> comando usado para aparecer uma mensagem na tela
print('o Tipo dessa variave é ', type(numeroReal))     #Todos comandos com parênteses() são chamados de funções
print('o Tipo dessa variave é ', type(texto))          #E dentro dos parênteses são os Atributos
print('o Tipo dessa variave é ', type(valorLogico))

#type() serve para mostrar qual é o tipo da varivel, que está dentro do parênteses!

#input() -> esse comando serve para receber valores externos.
#ou seja por teclado, touch, outros aparelhos etc..
#Exemplo se eu quiser que o usuário digite o nome

nome = input('Digite seu nome: ')

#Por padrão tudo que se digita no input é String. Se eu quiser receber um valor numérico [...]
#será preciso converter EX: se eu quiser que um usuário digite a idade!

idade = int(input('Digite a idade '))

#A função INPUT está dentro da função INT separado pelos parênteses()
#int() esse comando ira convertar o que estiver entre parênteses para um valor Interio
#Lembrando sempre de abrir e feixar os parênteses