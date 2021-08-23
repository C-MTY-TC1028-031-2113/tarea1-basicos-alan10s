def main():
    #escribe tu código abajo de esta línea
    print('Hola, dame tus calificaciones para saber tu promedio final')   
    cal1=float(input("Ingresa la calificación 1: "))
    cal2=float(input("Ingresa la calificación 2: "))
    cal3=float(input("Ingresa la calificación 3: "))
    cal4=float(input("Ingresa la calificación 4: "))
    promedio= (cal1+cal2+cal3+cal4)/4
    print('Tu promedio es ' + str(promedio))

    

if __name__ == '__main__':
    main()
