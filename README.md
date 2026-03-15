
# Simulador de Tránsito Urbano

Implementación de un simulador de tránsito utilizando estructuras de datos enlazadas en Python.

## Estructuras utilizadas

- Lista doblemente enlazada para representar la vía principal.
- Colas enlazadas para simular el funcionamiento del semáforo y la revisión de vehículos.

No se utilizan listas, tuplas, diccionarios ni estructuras auxiliares como lo exige la práctica.

## Vehículo

Cada vehículo contiene:

- placa
- tipo (auto, moto, camion)
- prioridad (1 a 5)
- estado de revisión

## Funcionalidades

### 1. Insertar vehículos
Los vehículos se insertan al final de la vía representada por una lista doblemente enlazada.

### 2. Paso preferencial
Todas las motos con prioridad 1 se mueven al inicio de la vía manteniendo su orden relativo.

### 3. Eliminación de camiones
Se eliminan todos los camiones con prioridad mayor a 3.

### 4. Simulación de accidente
Dados dos vehículos por placa, se eliminan todos los vehículos que estén entre ellos en la vía.

### 5. Inversión de la vía
Si existen más autos que motos, la vía se invierte completamente.

### 6. Reorganización por prioridad
Los vehículos se reorganizan de prioridad 1 a 5 conservando su orden original dentro de cada prioridad.

### 7. Simulación de semáforo

El sistema simula el paso de vehículos mediante dos colas:

- colaSemaforo
- colaRevision

Reglas implementadas:

- Paso de vehículos cada 30 segundos
- Desvío a revisión de camiones con prioridad mayor a 3
- Paso preferencial para motos con prioridad 1
- Control de máximo dos vehículos consecutivos del mismo tipo
- Reprocesamiento de vehículos revisados
- Eliminación de vehículos que pasan el semáforo de la vía principal

La simulación termina cuando:

- pasan 6 vehículos, o
- no quedan vehículos en las colas.

