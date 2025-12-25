# Este va ser un archivo de ejemplo para ilustrar 
# la gestión de errores de este archivo py pero para aprender git y github.

def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por cero."
    except TypeError:
        return "Error: Los operandos deben ser números."
    else:
        return resultado
# Ejemplo de uso
print(dividir(10, 2))  # Debería imprimir 5.0
print(dividir(10, 0))  # Debería imprimir un mensaje de error por división por cero
print(dividir(10, 'a'))  # Debería imprimir un mensaje de error