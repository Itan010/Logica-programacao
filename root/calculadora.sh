#!/bin/bash

# Função para adição
adicionar() {
    echo "Resultado: $(($1 + $2))"
}

# Função para subtração
subtrair() {
    echo "Resultado: $(($1 - $2))"
}

# Função para multiplicação
multiplicar() {
    echo "Resultado: $(($1 * $2))"
}

# Função para divisão
dividir() {
    if [ $2 -eq 0 ]; then
        echo "Erro: Divisão por zero."
    else
        echo "Resultado: $(($1 / $2))"
    fi
}

echo "Selecione a operação:"
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"
read -p "Escolha uma opção (1/2/3/4): " opcao

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

case $opcao in
    1) adicionar $num1 $num2 ;;
    2) subtrair $num1 $num2 ;;
    3) multiplicar $num1 $num2 ;;
    4) dividir $num1 $num2 ;;
    *) echo "Opção inválida" ;;
esac
