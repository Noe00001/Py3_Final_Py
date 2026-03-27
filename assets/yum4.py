# Ejercicio 4: 
# Analiza el siguiente “código existente” y realiza un -> refactor <-, tener en cuenta los 
# problemas que se plantean al final.

# Código original (difícil de mantener)

# 1 def calc(a, b, op):
# 2     if op == "s":
# 3         return a + b
# 4     elif op == "r":
# 5         return a - b
# 6     elif op == "m":
# 7         return a * b
# 8     elif op == "d":
# 9         if b == 0:
# 10             return "error"
# 11         return a / b
# 12     else:
# 13         return None

# Problemas:
# • Retorna "error" (string) o números → mezcla de tipos (confuso)
# • op con letras “mágicas”
# • No deja claro qué errores existen
# • Difícil testear los errores bien

#Solución:
#• No "error"
#• Op con palabras entendibles

#Reto: Agregar Errores con excepciones (comportamiento consistente)

#op =  input("Ingrese operación (suma, resta, multi, divi): ")
#a = int(input("Ingrese primer número: "))
#b = int(input("Ingrese segundo número: "))

#def calc(a, b, op):
    
    # match op:
    #     case "suma":
    #         return a + b
    #     case "resta":
    #         return a - b
    #     case "multi":
    #         return a * b
    #     case "divi":
    #         if b == 0:
    #             return "error"
    #         return a / b
    #     case _:
    #         return None
    
#    ops = {
#       "suma": lambda x, y: x + y,
#      "resta": lambda x, y: x - y,
#     "multi": lambda x, y: x * y,
#    "divi": lambda x, y: "error" if y == 0 else x / y        
#}

#func = ops.get(op)
#return func(a, b) if func else None

#result = calc(a, b, op)
# print("El resultado de", op, "es:", result)

#Organizadooooooo

def calc(a, b, op):
    ops = {
    "suma"  : lambda x, y: x + y,
    "resta" : lambda x, y: x - y,
    "multi" : lambda x, y: x * y,
    "divi"  : lambda x, y: x / y,  
    }

    if op not in ops:
            raise ValueError(
        f"Operación '{op}' no válida. "
        "Usa: suma, resta, multi, divi"
    )

    if op == "divi" and b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero")

    return ops[op](a, b)


#REFACTORIZADA .W.
def calc(a, b, op):
    ops = {
        "suma"  : lambda x, y: x + y,
        "resta" : lambda x, y: x - y,
        "multi" : lambda x, y: x * y,
        "divi"  : lambda x, y: x / y,   # sin "error" mezclado
    }

    if op not in ops:
        raise ValueError(
            f"Operación '{op}' no válida. Usa: suma, resta, multi, divi"
        )

    if op == "divi" and b == 0:
        raise ZeroDivisionError("No se puede dividir entre cero.")

    return ops[op](a, b)


# Principal primera .w.
try:
    op = input("Ingrese operación (suma, resta, multi, divi): ").strip().lower()
    a  = int(input("Ingrese primer número: "))
    b  = int(input("Ingrese segundo número: "))

    resultado = calc(a, b, op)
    print(f"El resultado de {op} es: {resultado}")

except ValueError as e:
    print(f"Error de valor: {e}")

except ZeroDivisionError as e:
    print(f"Error matemático: {e}")

except Exception as e:
    print(f"Error no previsto: {e}")