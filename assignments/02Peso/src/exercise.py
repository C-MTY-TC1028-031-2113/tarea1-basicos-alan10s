def main():
    #escribe tu código abajo de esta línea
    print('Hola, soy Alan y seré tu nutriologo, dame tus datos')
    pesoin= float(input('Dame tu peso inicial: '))
    pesofin= float(input('Dame tu objetivo de  peso final: '))
    meses= int(input('Dame la cantidad de meses en que quieres llegar a  ese peso: '))
    cantxmes= (pesoin-pesofin)/meses
    print('La cantidad de Kg que debes bajar por mes es de ' + str(cantxmes))


if __name__ == '__main__':
    main()
