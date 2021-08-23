def main():
    #escribe tu código abajo de esta línea
    print('Hola, bienvenido a la banca movil, vamos a cálcular tu saldo mensual, ingresa los siguientes datos: ')
    mesant= float(input('Dame el saldo del mes anterior: '))
    ingresos= float(input('Dame tus ingresos: '))
    egresos= float(input('Dame tus egresos: '))
    cheques= int(input('Dame el número de cheques expedidos: '))
    calcfinal= (((mesant+ingresos-egresos-(cheques*13)))*0.925)
    print('Tu saldo final de la cuenta este mes es: ' +str(calcfinal))


if __name__ == '__main__':
    main()
