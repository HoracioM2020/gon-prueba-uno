ipi = {
    "Dtomin": 556.02, 
    "Indif": 85528, 
    "Basemax": 14839.02, 
    "Porcentaje-min": 18, 
    "Porcentaje-max": 32
}
print(ipi)
print(ipi["Basemax"])

def main():
    a = int(input("su ingreso anual: "))
    print()
    b = impuesto(a)
    print("El impuesto es de ") 
    c = round(b,0)
    print(c)

def impuesto(a):
    if a <= ipi["Indif"]:
        resultado_final  = (ipi["Porcentaje-min"] / 100) * a - ipi["Dtomin"]
    if a < 0:
        resultado_final = 0
        print("Usted es un afortunado")
    elif a > ipi["Indif"]:
        resultado_final  = ipi["Basemax"] + (a - ipi["Indif"] * ipi["Porcentaje-max"]) / 100

    return resultado_final
