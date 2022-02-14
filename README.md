# cuadrados
Resuelvo un problema que involucra cuadrados.
Determinar cuando un número se puede escirbir como la suma de dos cuadrados.
Usé varios resultados de congruencias.
Defino una función llamada sq:
De aquí el primer paso es ver que el residuo del número m con el 4 es igual a 3, si esto pasa entonces m no puede ser una suma de dos cuadrados. Ya que todo cuadrado es congruente con 0,1 módulo 4 y la suma de dos cuadrados será congruente con 0,1 y 2 mod 4.  

Ahora Si no pasa lo anterior, entonces la función ve primero si es un cuadrado, si es un cuadrado entonces en efecto es la suma de dos cuadrados (0 y el mismo).

Si no sucede lo anterior, entonces procede a iterar sobre los números 1 a la parte entera de raíz de m. Entonces compara las igualdad de m-i**2 == a la parte entera de m-i**2, de donde i está en el conjunto {1,2,...[m**0.5]}, si coincide entonces m se puede escribir como la suma de dos cuadrados.
