from get_ascii import get_ascii
from get_binary import get_binary
def get_result(palabra):
    """
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
    resultado = []
    for caracter in palabra:
        ascii_code = get_ascii(caracter)
        binario = get_binary(ascii_code)
        resultado.append(("El caracter es:", caracter,", El código Ascii es: ", ascii_code,", El binario es:", binario))
    return resultado
