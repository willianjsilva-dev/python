from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa''')
    opcao = int (input('Qual a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1}+{n2} = {soma}')
    elif opcao == 2:
        multiplicar = n1 * n2
        print(f'O resultado entre {n1}x{n2} = {multiplicar}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
    else:
     print('\033[31mOpção invalida. Tente novamente.\033[m')
    print('-=' * 20)
    sleep(1.5)
print('\033[33m Fim do programa! Volte sempre!\033[m')
