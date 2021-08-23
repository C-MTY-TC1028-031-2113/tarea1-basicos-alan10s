def main():
    #escribe tu código abajo de esta línea
    #Lee los datos
    print('Hola, bienvenido a la clase de matematicas, para cálcular la pendiente dame los siguientes datos')
    x1= float(input('Dame x1: '))
    y1= float(input('Dame y1: '))
    x2= float(input('Dame x2: '))
    y2= float(input('Dame y2: '))
    pendiente= (y2 - y1) / (x2 - x1)
    print('La pendiente de tu recta es '+str(pendiente))




if __name__ == '__main__':
    main()
