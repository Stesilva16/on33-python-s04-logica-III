tabuada = int(input('Tabuada de: '))
inicio = int(input('Começada pelo nº: '))
fim = int(input('Terminada pelo nº: '))

try:
    while inicio-1 < fim:
        resultado = tabuada * inicio
        print(tabuada, 'x', inicio, '=', resultado) 
        inicio += 1
        
        
except:
    if fim > inicio:
        print('Digite o início maior que o fim!')

    