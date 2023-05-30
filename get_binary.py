def get_binary(ascii_code):
    """
    Convierte un código ASCII en su representación binaria.

    Parameters:
        ascii_code (int): El código ASCII a convertir.

    Returns:
        str: La representación binaria del código ASCII.

    Example:
        >> get_binary(65)
        '1000001'
    """
    binario = ""
    while ascii_code > 0:
        residuo = ascii_code % 2
        binario = str(residuo) + binario
        ascii_code = ascii_code // 2
    return binario
