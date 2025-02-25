# Logica-programacao
## Primeiro Projeto 
### Calculadora em Python

Este é um simples script de calculadora em Python que permite ao usuário realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão. O script é interativo e solicita que o usuário escolha uma operação e insira dois números para realizar o cálculo.

**Funcionalidades**

O script oferece as seguintes operações:

  1 **Adição:** Soma dois números.

  2 **Subtração:** Subtrai o segundo número do primeiro.

  3 **Multiplicação:** Multiplica dois números.

  4 **Divisão:** Divide o primeiro número pelo segundo (com tratamento para divisão por zero).

**Como funciona**

O script utiliza uma estrutura match-case (disponível a partir do Python 3.10) para determinar qual operação será executada com base na escolha do usuário. As operações são realizadas usando funções simples que retornam o resultado da operação selecionada.

**Como usar**
**1 Executar o script:**

Certifique-se de ter o Python instalado.

Execute o script no terminal:

python calculadora.py

**2 Interagir com a calculadora:**

O script solicitará que você escolha uma operação (1 para adição, 2 para subtração, 3 para multiplicação, 4 para divisão).

Em seguida, insira dois números para realizar a operação.

O resultado será exibido no terminal.

**Exemplo de uso**

    $ python calculadora.py
    Selecione a operação:
    1. Adição
    2. Subtração
    3. Multiplicação
    4. Divisão
    Escolha uma opção (1/2/3/4): 1
    Digite o primeiro número: 10
    Digite o segundo número: 5
    Resultado: 15

**Código**

     Aqui está o código principal do script:

     def adicionar(a, b):
         return a + b

     def subtrair(a, b):
         return a - b

     def multiplicar(a, b):
         return a * b

     def dividir(a, b):
         if b == 0:
             return "Erro: Divisão por zero."
         return a / b

     print("Selecione a operação:")
     print("1. Adição")
     print("2. Subtração")
     print("3. Multiplicação")
     print("4. Divisão")

     opcao = input("Escolha uma opção (1/2/3/4): ")

     num1 = float(input("Digite o primeiro número: "))
     num2 = float(input("Digite o segundo número: "))

     match opcao:
         case '1':
             print(f"Resultado: {adicionar(num1, num2)}")
         case '2':
             print(f"Resultado: {subtrair(num1, num2)}")
         case '3':
             print(f"Resultado: {multiplicar(num1, num2)}")
         case '4':
             print(f"Resultado: {dividir(num1, num2)}")
         case _:
             print("Opção inválida.")

**Requisitos**

Python 3.10 ou superior (para usar a estrutura  `match-case`).

Nenhuma dependência externa é necessária.

**Contribuição**

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Basta abrir uma *issue* ou enviar um *pull request*


