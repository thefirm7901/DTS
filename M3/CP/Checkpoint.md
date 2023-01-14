# Checkpoint - Módulo 3

Cómo responder: <br>
* Cuando se pida una respuesta numérica, redondear al segundo decimal. <br>
   Ejemplo: 1.3421 -> 1.34;<br>
            1.8888 -> 1.89;<br>
            3 -> 3.00.<br>

* Recuerda resolver los problemas de manera secuencial y pensar las consultas por partes. Además te resultará útil pensar di debes reutilizar la lógica de consulta de otro ejercicio.<br>

## Responder Verdadero ó Falso

### 1) Un índice SQL mejora la eficiencia y rapidéz en la búsqueda de información.<br>

### 2) En la detección de Outliers, el método del Rango Intercuartil se basa en la utilización de la mediana.<br>

### 3) Las tablas Maestros registran las operaciones ocurridas, todo tipo de transacciones donde intervienen las diferentes entidades del modelo.<br>

## Elegir la opción correcta en base a la observación del siguiente DER:

<img src="DER.jpg"  height="400">

### 4) ¿Cuál de las siguientes es una tabla de hecho?
1. canal_venta<br>
2. calendario<br>
3. tipo_producto<br>
4. venta<br>

### 5) El DER mostrado en la imagen:
1. Es un Modelo Estrella, porque tiene una única tabla de hechos.<br>
2. Es un Modelo Copo de Nieve, porque de la tabla venta se desprenden el resto de tablas.<br>
3. Niguna de las anteriores.<br>

## Resuelve los siguientes ejercicios:

### En tu motor de base de datos MySQL, ejecutá las instrucciones del script 'Checkpoint_Create_Insert.sql' (Si no trabajas con MySQL es posible que tengas que realizar algunos ajustes en el script. También están provistas las tablas en formato csv dentro de la carpeta 'tablas_cp').

### 6) La ganancia neta por sucursal es las ventas menos los gastos (Ganancia = Venta - Gasto) ¿Cuál es la sucursal con mayor ganancia neta en 2019? 
1. Alberdi<br>
2. Flores<br>
3. Corrientes<br>

### 7) La ganancia neta por producto es las ventas menos las compras (Ganancia = Venta - Compra) ¿Cuál es el tipo de producto con mayor ganancia neta en 2019?
1. Informática<br>
2. Impresión<br>
3. Grabacion<br>

### 8) Del total de clientes que realizaron compras en 2019 ¿Qué porcentaje lo hizo en al menos dos sucursales? (expresado en porcentaje y con dos decimales, por ejemplo 11.11)

### 9) Del total de clientes que realizaron compras en 2020 ¿Qué porcentaje no había realizado compras en 2019? (expresado en porcentaje y con dos decimales, por ejemplo 11.11)

### 10) Del total de clientes que realizaron compras en 2019 ¿Qué porcentaje lo hizo también en 2020? (expresado en porcentaje y con dos decimales, por ejemplo 11.11)

### 11) ¿Qué cantidad de clientes realizó compras sólo por el canal Presencial entre 2019 y 2020?

### 12) ¿Cuál es la sucursal que más Venta (Precio * Cantidad) hizo en 2019 a clientes que viven fuera de su provincia?
1. Flores<br>
2. Rosario1<br>
3. Córdoba Centro<br>

### 13) ¿Cuál fué el mes del año 2020, de mayor decrecimiento (o menor crecimiento) con respecto al mismo mes del año 2019 si se toman en cuenta a nivel general Ventas (Precio * Cantidad) - Compras (Precio * Cantidad) - Gastos? 
#### Responder el Número del Mes:

### 14) El negocio suele requerir con gran frecuencia consultas a nivel trimestral tanto sobre las ventas, como las compras y los gastos, entonces:
1. Con los índices creados existentes, sólo sobre las claves primarias y foráneas, sería suficiente para cubrir cualquier necesidad de consulta.<br>
2. Sería aduecuado colocar un índice sobre el campo trimestre de la tabla calendario aunque este no sea una clave foránea.<br>
3. No se puede crear índices sobre campos que no son clave.<br>


### Cada una de las sucursales de la provincia de Córdoba, disponibilizaron un excel donde registraron el porcentaje de comisión que se le otorgó a cada uno de los empleados sobre la venta que realizaron. Es necesario incluir esas tablas (Comisiones Córdoba Centro.xlsx, Comisiones Córdoba Quiróz.xlsx y Comisiones Córdoba Cerro de las Rosas.xlsx) en el modelo y contestar las siguientes preguntas:

### 15) ¿Cuál es el código de empleado del empleado que mayor comisión obtuvo en diciembre del año 2020?

### 16) ¿Cuál es la sucursal que más comisión pagó en el año 2020?
1. Córdoba Centro.<br>
2. Córdoba Quiroz.<br>
3. Cerro De Las Rosas.<br>

