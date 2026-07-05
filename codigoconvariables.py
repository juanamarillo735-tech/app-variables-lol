import pulp

# Inicializar modelo
modelo_complejo = pulp.LpProblem("Maximizacion_Cloud_Avanzado", pulp.LpMaximize)

# Variables de decisión (Enteras)
x1 = pulp.LpVariable("VM_Basica", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("VM_Pro", lowBound=5, cat='Integer') # Aquí ya incluimos la restricción de ventas >= 5
x3 = pulp.LpVariable("VM_Enterprise", lowBound=0, cat='Integer')

# Función Objetivo
modelo_complejo += 20 * x1 + 50 * x2 + 120 * x3, "Ingreso_Total"

# Restricciones
modelo_complejo += 2 * x1 + 4 * x2 + 8 * x3 <= 120, "Limite_CPU"
modelo_complejo += 4 * x1 + 16 * x2 + 32 * x3 <= 320, "Limite_RAM"
modelo_complejo += 50 * x1 + 100 * x2 + 250 * x3 <= 1000, "Limite_SSD"

# Resolver
modelo_complejo.solve()

# Resultados
print("--- MODELO COMPLEJIZADO ---")
print(f"Estado: {pulp.LpStatus[modelo_complejo.status]}")
print(f"VM Básicas: {x1.varValue}")
print(f"VM Pro: {x2.varValue}")
print(f"VM Enterprise: {x3.varValue}")
print(f"Ingreso mensual máximo: ${pulp.value(modelo_complejo.objective)} USD")