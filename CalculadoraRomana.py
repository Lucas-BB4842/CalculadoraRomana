import os

def rom_para_int(numero):

    simbolos = ( ['M', 1000], ['D', 500], ['C', 100], ['L', 50], ['X', 10], ['V', 5], ['I', 1])
    casos_especiais = (['CM', 900], ['CD', 400], ['XC', 90], ['XL', 40], ['IX', 9], ['IV', 4])
    
    num = numero.upper()
    valor = 0

    while True:

        teste = True

        if len(num) >= 2:
            for ce in casos_especiais:
                if ce[0] == num[:2]: 
                    valor += ce[1]
                    num = num[2:]
                    teste = False
                    break
        
        if len(num) >= 1 and teste == True:
            for s in simbolos:
                if s[0] == num[0]:
                    valor += s[1]
                    num = num[1:]
                    break
        
        if len(num) == 0:
            return valor
            break

sair = 'N'
while sair == 'N':

    os.system('cls')

    print('=' * 22)
    print('  CALCULADORA ROMANA  ')
    print('=' * 22)

    expressao = str(input('Digite a expressão: ')).split()

    numero1 = rom_para_int(expressao[0])
    numero2 = rom_para_int(expressao[2])

    if expressao[1] == '+':
        resultado = numero1 + numero2

    elif expressao[1] == '-':
        resultado = numero1 - numero2

    print(f'{numero1} {expressao[1]} {numero2} = {resultado}')

    sair = str(input('Quer sair? [S/N]')).upper()
