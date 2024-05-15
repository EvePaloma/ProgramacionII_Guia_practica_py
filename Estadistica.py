'''
def moda():
    frecuencia = {}
    for elemento in moda:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1


    valor_moda = None
    frecuencia_moda = 0
    for valor, freq in frecuencia.items():
        if freq > frecuencia_moda:
            valor_moda = valor
            frecuencia_moda = freq   

    return valor_moda                 
'''

