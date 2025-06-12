

def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def taylor_exponencial(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        resultado += (x ** n) / factorial(n)
    return resultado

def taylor_seno(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        signo = (-1) ** n
        resultado += signo * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return resultado

def taylor_coseno(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        signo = (-1) ** n
        resultado += signo * (x ** (2 * n)) / factorial(2 * n)
    return resultado

def taylor_arcsen(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        numerador = factorial(2 * n)
        denominador = (4 ** n) * (factorial(n) ** 2) * (2 * n + 1)
        resultado += (numerador / denominador) * (x ** (2 * n + 1))
    return resultado

def taylor_arccos(x, terminos=10):
    return (3.141592653589793 / 2) - taylor_arcsen(x, terminos)

def taylor_seno_hiperbolico(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        resultado += (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return resultado

def taylor_coseno_hiperbolico(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        resultado += (x ** (2 * n)) / factorial(2 * n)
    return resultado