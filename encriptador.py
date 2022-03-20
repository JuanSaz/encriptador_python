#Tarea: Conseguir encriptar y desencriptar un archivo de texto (.txt)
def CreateFile():                           #Solo usado al principio para crear el .txt
    archivo = open("text.txt","a")         #Crea el archivo, verificando si existe o no
    archivo.close()
    print("File was created")

def ReadFile():
    archivo = open("text.txt", "r")
    content = archivo.read()
    archivo.close()
    return content                          #Si yo hago return, el valor que obtenga del contenido 
                                            #será el resultado si yo llamo a esta función
def WriteWelcomeText(text):                     #Usado solo para escribir el texto principal
    archivo = open("text.txt", "w")
    archivo.write(text)
    print("Welcome Message is inside the text file.")
    

def EncryptFile(content):                   #Cada vez que se llama a esta funcion, se encripta el texto entero
    encryptedMessage = ""
    for letters in content:
        encriptedArray = [letters + "x"]    #Creo un Array con los elementos ya "encriptados"
        for word in encriptedArray:
            encryptedMessage += word
    print("Message was successfully encripted.")
    archivo = open("text.txt", "a")
    archivo.write("\n")
    archivo.write(encryptedMessage)
    print("Text has been successfully re-written as " + encryptedMessage)

welcomeMessage = input("Ingrese el texto a encriptar: ")
CreateFile()
WriteWelcomeText(welcomeMessage)
EncryptFile(ReadFile())                     #Le mando el valor del texto a la funcion encriptadora
