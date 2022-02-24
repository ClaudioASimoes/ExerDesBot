# ler ano de nascimento do atleta e classifica-lo
# até 9 : mirim      até 14 ; infantil   até 19: junior
# até 20: senior      acima :master

#####    MEU      #####
from datetime import date

at = date.today().year
ano = int(input('Digite o ano de nascimento: '))
res = int(at - ano)
if res <= 0:
    print("Ano de nascimento inválido!!!")
else:
    if res <= 9:
        print('Atleta da categoria Mirim.')
    elif  9 > res <= 14:
        print('Atleta da categoria Infantil.')
    elif 14 > res <= 19:
        print('Atleta da categoria Junior.')
    elif 19 > res <= 25:
        print('Atleta da categoria Senior.')
    elif res > 25:
        print('Atleta da categoria Master.')


####       CURSO     ######

atual = date.today().year
nasc = int(input('Ano de nascimento : '))
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação : MIRIM')
elif 9 < idade <= 14:
    print('Classificação : INFANTIL')
elif idade <= 19:
    print('Classificação : JUNIOR')
elif idade <= 25:
    print('Classificação : SENIOR')
elif idade > 25:
    print('Classificação : MASTER')c