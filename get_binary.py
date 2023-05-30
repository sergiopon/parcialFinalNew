def get_binary(ascii_code):

    binario = ""
    while ascii_code > 0:
        residuo = ascii_code % 2
        binario = str(residuo) + binario
        ascii_code = ascii_code // 2
    return binario