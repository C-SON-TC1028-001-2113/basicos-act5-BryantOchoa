import math
def main():
    #escribe tu código abajo de esta línea
    area = float(input('Area a pintar en metros:  '))
    rendimiento = float(input("Rendimiento (m2/l)"))
    Litros = math.ceil(area/rendimiento)

    print('Litros a comprar: '+str (Litros))


if __name__ == '__main__':
    main()
