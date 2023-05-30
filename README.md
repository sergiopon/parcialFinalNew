# parcialFinalNew
# Evaluación Final

### def get_binary(ascii_code):
    
    Convierte un código ASCII en su representación binaria.

    Parameters:
        ascii_code (int): El código ASCII a convertir.

    Returns:
        str: La representación binaria del código ASCII.

    Example:
        >> get_binary(65)
        '1000001'
    """
    binario = ""  # Initialize an empty string to store the binary representation
    while ascii_code > 0:  # Continue the loop until ascii_code becomes 0
        residuo = ascii_code % 2  # Calculate the remainder when dividing ascii_code by 2 (least significant bit)
        binario = str(residuo) + binario  # Concatenate the remainder (converted to a string) to the left of the existing binario string
        ascii_code = ascii_code // 2  # Update ascii_code by performing an integer division by 2 (shift bits to the right)
    return binario  # Return the binary representation string
### def  get_ascii(caracter):
 Obtiene el código ASCII correspondiente a un carácter. 
 Parameters: caracter (str): El carácter para el cual se desea obtener el código ASCII. Returns: int: El código ASCII correspondiente al carácter.
  Example: >> get_ascii('A') 65 
  return  ord(caracter)
### def get_result(palabra):
   
    Obtiene el resultado de procesar cada caracter de una palabra.

    Parameters:
        palabra (str): La palabra a procesar.

    Returns:
        list: Una lista de tuplas que contienen información sobre cada caracter procesado.

    Example:
        >> get_result("Hello")
        [('El caracter es:', 'H', ', El código Ascii es: ', 72, ', El binario es:', '1001000'),
         ('El caracter es:', 'e', ', El código Ascii es: ', 101, ', El binario es:', '1100101'),
         ('El caracter es:', 'l', ', El código Ascii es: ', 108, ', El binario es:', '1101100'),
         ('El caracter es:', 'l', ', El código Ascii es: ', 108, ', El binario es:', '1101100'),
         ('El caracter es:', 'o', ', El código Ascii es: ', 111, ', El binario es:', '1101111')]
    """
    resultado = []  # Initialize an empty list to store the processed character information
    for caracter in palabra:  # Iterate over each character in the word
        ascii_code = get_ascii(caracter)  # Get the ASCII code for the character
        binario = get_binary(ascii_code)  # Get the binary representation of the ASCII code
        # Construct a tuple with the processed character information and append it to the resultado list
        resultado.append(("El caracter es:", caracter, ", El código Ascii es: ", ascii_code, ", El binario es:", binario))
    return resultado  # Return the list of tuples containing information about each processed character
    

# Integrantes del grupo

-Sebastian Izquierdo Saavedra (sebasizq)
-Sergio Ponce (sergiopon)
-Emily Bonilla(emilyb0)
-Eli mallama (EliMallama)


## Iniciar sesion en git Bash
sebas@DESKTOP-7N9GBQ8 MINGW64 ~
$ git config --global user.name "sebasizq"

sebas@DESKTOP-7N9GBQ8 MINGW64 ~
$ git config --global user.email "sebastiansaavedra_2005@hotmail.com"

## Clonar repositorio

$ git clone https://github.com/sebasizq/TercerParcial.git
Cloning into 'TercerParcial'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.

## Cargar Archivos
sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git add archivo.py
warning: in the working copy of 'archivo.py', LF will be replaced by CRLF the next time Git touches it

sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   archivo.py


sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git commit -m "cambio 1"
[main d001fd9] cambio 1
 1 file changed, 2 insertions(+)
 create mode 100644 archivo.py

sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 4 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 303 bytes | 303.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/sebasizq/TercerParcial.git
   c5bc5de..d001fd9  main -> main



## Crear rama 

sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git branch
* main

sebas@DESKTOP-7N9GBQ8 MINGW64 ~/Desktop/TercerParcial (main)
$ git branch RamaNueva


