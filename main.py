from get_ascii import get_ascii
from get_binary import get_binary
def get_result(palabra):

    resultado = []
    for caracter in palabra:
        ascii_code = get_ascii(caracter)
        binario = get_binary(ascii_code)
        resultado.append(("El caracter es:", caracter,", El código Ascii es: ", ascii_code,", El binario es:", binario))
    return resultado
