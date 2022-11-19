#diccionario1={"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","Ñ":"--.--","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","Á":".--.-","É":"..-..","Ó":"---.","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-","(":"-.--.","+":".-.-.","¿":"..-.-",",":"--..--",")":"-.--.-","-":"-....-","¡":"--...-","?":"..--..","&":".-...","_":"..--.-","'":".----.",":":"---...","!":"-.-.--",";":"-.-.-.","$":"...-..-","/":"-..-.","=":"-...-"," ":"/","@":".--.-.","a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","ñ":"--.--","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","á":".--.-","é":"..-..","ó":"---."}
diccionario={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","ñ":"--.--","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--..","á":".--.-","é":"..-..","ó":"---.","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.",".":".-.-.-","(":"-.--.","+":".-.-.","¿":"..-.-",",":"--..--",")":"-.--.-","-":"-....-","¡":"--...-","?":"..--..","&":".-...","_":"..--.-","'":".----.",":":"---...","!":"-.-.--",";":"-.-.-.","$":"...-..-","/":"-..-.","=":"-...-","":"/","@":".--.-."}



def menu():
    print("Este programa realizará una traducción del alfabeto tradicional a codigo morse, o viceversa")
    print("1. Traducir de alfabeto tradicional a morse")
    print("2. Traducir de morse a alfabeto tradicional")
    print("3. Salir")
    opcion=input(("Escriba la opcion deseada: "))
    return opcion



def abc_to_morse():
    frase=(input("A continuación escriba la frase deseada: "))
    frase=frase.lower()
    print(frase)
    lista_letras=list(str(frase))
    lista_traducida=[]
    print(lista_letras)
    for i in range (len(lista_letras)):
        letra=lista_letras[i]
        lista_traducida.append(diccionario[letra])
    lista_traducida=" ".join(lista_traducida)
    print("="*100)
    print("La traducción es: %s" %lista_traducida)
    print("="*100)



def morse_to_abc():
    morse=(input("A continuación escriba el codigo morse: "))
    lista_morse=morse.split()
    lista_traducida=[]
    for i in range (len(lista_morse)):
        for keyword, value in diccionario.items():
            if value==lista_morse[i]:
                lista_traducida.append(keyword)
    lista_traducida="".join(lista_traducida)
    print("="*100)
    print("La traducción es: %s " %lista_traducida)
    print("="*100)



def main():
    opcion1=menu()
    while not (opcion1 in "3"):
        if opcion1 in "1":
            abc_to_morse()
        
        if opcion1 in "2":
            morse_to_abc()


        opcion1=menu()

main()
