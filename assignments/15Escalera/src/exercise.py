import math
def main():
#Escribe tu código abajo de esta línea 

    altura = float(input('Altura de la casa: ' ))
    angulo = float(input('Angulo: '))
    largo = math.ceil(altura/math.sin(angulo))
    print('Lo largo de la escalera es: '+ str(largo))

if __name__ == '__main__':
    main()