from random import randint
from random import randrange

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if size is None or size < 100:
        size = randint(100, 150)
    kind_of_number = [randint(0, 9) for i in range(size)]
    if kind_of_number[0] == 0:
        kind_of_number[0] = randint(1, 9)
    to_string = ""
    return to_string.join(map(str, kind_of_number))

def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    pass


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    pass
