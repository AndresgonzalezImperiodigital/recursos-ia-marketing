# Herramienta oficial de Mperio Digital Academy
# Esta calculadora ayuda a emprendedores a medir su éxito en Ads

def calcular_roi(ventas, costo):
    if costo == 0:
        return "Error: La inversión no puede ser 0"
    roi = ((ventas - costo) / costo) * 100
    return round(roi, 2)

print("--- 📊 CALCULADORA DE ROI MPERIO DIGITAL ---")
inversion = float(input("¿Cuánto invertiste en publicidad? $"))
ganancia_total = float(input("¿Cuánto dinero total entró por ventas? $"))

resultado = calcular_roi(ganancia_total, inversion)

print(f"\nTu Retorno de Inversión (ROI) es del: {resultado}%")

if float(resultado) > 0:
    print("¡Felicidades! Tu campaña es RENTABLE. 🚀")
else:
    print("Atención: Estás perdiendo dinero. Revisa tu estrategia en mperiodigital.com 📉")
