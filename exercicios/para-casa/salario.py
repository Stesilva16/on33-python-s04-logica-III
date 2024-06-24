salario_base = int(input('Insira um salário base: '))
aumento_anual = 1.5
ano_inicial = 1995

    
for ano_inicial in range(1995,2024):
    salario_atual = salario_base * (1 + aumento_anual / 100)
    aumento_anual *= 2
    ano_inicial += 1
    if ano_inicial >= 2024:
        print (f'O salário atualizado do funcionário é de {salario_atual:.2f} em {ano_inicial}')
    

    
