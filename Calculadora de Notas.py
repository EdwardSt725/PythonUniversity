notas = []
opc = int

def ingre_datos():
    global notas
    materia = str(input('Ingrese la materia: '))
    nota = float
    porcent = int
    avg = []
    cant= int(input('Ingrese la cantidad de notas que va a calcular: '))
    
    for i in range(1,cant+1):
        porcent = int(input('A cuanto equivale la nota %i: ' %i))
        avg.append(porcent)
        nota = float(input('Ingresa la nota: '))
        porcent = porcent*0.01
        notas.append(nota*porcent)
    print(notas)
    avg = int(sum(avg))
    print('Ha cursado el %i'%avg,'% ', 'de la materia')
    print('Su nota de %s hasta el momento va en: '%materia,sum(notas))
    
def menu():
    global opc
    print('-'*5,'PROGRAMA NOTAS','-'*5)
    print('[1]Calcular Materia\n[2]Salir')
    opc = int(input('Ingrese la opción que desea: '))

def main():
    global opc
    while opc != 2:
        menu()
        if opc == 1:
            ingre_datos()
        elif opc == 2:
            print('Gracias, adiós.')
        elif opc <= 0 or opc >= 3:
            print('No ha digitado una opción válida...')

main()