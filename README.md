# LectorEscritor
Ejercicio declarando 2 lectores y 2 escritores

Un Lector accede al archivo original de texto
Después se hace un lock
Se manda llamar a un escritor
Este hace una modificación al archivo de texto, 
Se hace un lock
Se manda llamar al segundo lector, que a su vez repite el proceso para llamar al segundo escritor

Limitado en este caso hasta 5 turnos
