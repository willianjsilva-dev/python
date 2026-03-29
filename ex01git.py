nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2} a média do aluno é {media}')
if 7 > media <= 5:
    print('o ALUNO ESTA EM RECUPERAÇÃO')
elif media <= 5:
    print('O ALUNO ESTA REPROVADO')
elif media >= 7:
    print('O ALUNO ESTA APROVADO')

