def Punto3(Valor):
    Total = []
    Total.append(Valor)
    
    if Valor > 500:
        Total.append(10)
    elif Valor >= 100:
        Total.append(5)
    else:
        Total.append(0)
        
    Total.append(Total[0] - (Total[0] * (Total[1] / 100)))
    
    return Total

Resultado = Punto3(int(input('Valor venta:')))
print(f"Valor: {Resultado[0]}\nDescuento: {Resultado[1]}%\nValor a Pagar: {Resultado[2]}")