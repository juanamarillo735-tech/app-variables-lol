
import pulp

# 1. Inicializar el modelo indicando que queremos MAXIMIZAR los ingresos
modelo = pulp.LpProblem("Maximizacion_Ingresos_Cloud", pulp.LpMaximize)

# 2. Definir las variables de decisión
# cat='Integer' indica que no podemos vender fracciones de máquinas virtuales (deben ser enteras)
x1 = pulp.LpVariable("VM_Basica", lowBound=0, cat='Integer')
x2 = pulp.LpVariable("VM_Pro", lowBound=0, cat='Integer') 
x3 = pulp.LpVariable("VM_Enterprise", lowBound=0, cat='Integer')

# 3. Definir la Función Objetivo (Ingresos generados por cada tipo de VM)
# $20 por la Básica, $50 por la Pro, $120 por la Enterprise
modelo += 20 * x1 + 50 * x2 + 120 * x3, "Ingreso_Total_Mensual"

# 4. Definir las Restricciones
# Restricción 1: Límite de núcleos de CPU (Máximo 120)
modelo += 2 * x1 + 4 * x2 + 8 * x3 <= 120, "Limite_CPU"

# Restricción 2: Límite de memoria RAM en GB (Máximo 320)
modelo += 4 * x1 + 16 * x2 + 32 * x3 <= 320, "Limite_RAM"

# Restricción 3: Límite de almacenamiento SSD en GB (Máximo 1000)
modelo += 50 * x1 + 100 * x2 + 250 * x3 <= 1000, "Limite_SSD"

# Restricción 4: Contrato de ventas (Mínimo 5 VM Pro configuradas)
modelo += x2 >= 5, "Minimo_Ventas_Pro"

# 5. Resolver el modelo matemático
modelo.solve()

# 6. Imprimir los resultados por pantalla
print("-" * 30)
print("RESULTADOS DE LA OPTIMIZACIÓN")
print("-" * 30)
print(f"Estado de la solución: {pulp.LpStatus[modelo.status]}")
print(f"Cantidad de VM Básicas a instanciar (x1): {int(x1.varValue)}")
print(f"Cantidad de VM Pro a instanciar (x2): {int(x2.varValue)}")
print(f"Cantidad de VM Enterprise a instanciar (x3): {int(x3.varValue)}")
print("-" * 30)
print(f"INGRESO MENSUAL MÁXIMO: ${int(pulp.value(modelo.objective))} USD")
print("-" * 30)
