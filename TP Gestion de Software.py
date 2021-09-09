#Se desea conocer el aumento de salario de todos los vendedores de un local comercial, para lo cual deberá preguntar al operador el sueldo que se venía persibiendo, teiendo en cuenta que el aumento es del 25%. 
#Se desea conocer cuánto ganará cada uno.
#Además será necesario mostrar lo que la empresa deberá pagar a todos los vendedores en concepto de salario y con cuántos vendedores cuenta.

contVendedor = 0
acumuladorDia = 0

v = int (input ("Ingesar 1 para registrar un vendedor o 0 para terminar \n"))
ant = float(input("Ingrese el sueldo que se venia persibiendo \n"))
    aumento = ant*0.25
    au2 = ant+aumento
    acumuladorDia = acumuladorDia + au2
    contVendedor = contVendedor + 1
    print ("El operario venia ganando" ,ant,"y pasara a ganar" ,au2)
    
