from estructuras import*

def paso_preferencial(via):

    nodo = via.head

    while nodo:
        siguiente = nodo.next
        vehiculo = nodo.value

        if vehiculo.tipo == "moto" and vehiculo.prioridad == 1 and nodo != via.head:
            
            if nodo.prev:
                nodo.prev.next = nodo.next

            if nodo.next:
                nodo.next.prev = nodo.prev
            else:
                via.tail = nodo.prev

            nodo.prev = None
            nodo.next = via.head
            via.head.prev = nodo
            via.head = nodo
        
        nodo = siguiente

def eliminar_camiones(via):

    nodo = via.head

    while nodo:
        
        siguiente = nodo.next
        vehiculo = nodo.value

        if vehiculo.tipo == "camion" and vehiculo.prioridad > 3:

            if nodo == via.head:
                via.head = nodo.next
                if via.head:
                    via.head.prev = None
                else:
                    via.tail = None

            elif nodo == via.tail:
                via.tail = nodo.prev
                via.tail.next = None
            
            else:
                nodo.prev.next = nodo.next
                nodo.next.prev = nodo.prev

        nodo = siguiente

def accidente(via):
    ...

def invertir_via(via):

    autos = 0
    motos = 0

    nodo = via.head
    while nodo:
        if nodo.value.tipo == "auto":
            autos += 1
        elif nodo.value.tipo == "moto":
            motos += 1
        nodo = nodo.next 
    
    if autos <= motos:
        return
    
    nodo = via.head
    while nodo:
        siguiente = nodo.next

        nodo.next = nodo.prev
        nodo.prev = siguiente

        nodo = siguiente
    
    via.head, via.tail = via.tail, via.head
        


    

def main():

    via = DoublyLinkedList()

    via.append(Vehiculo("AAA111", "auto" , 3))
    via.append(Vehiculo("BBB222", "moto" , 1))
    via.append(Vehiculo("CCC333", "camion" , 4))
    via.append(Vehiculo("DDD444", "auto" , 2))
    via.append(Vehiculo("EEE555", "moto", 1))
    via.append(Vehiculo("OOO999", "camion" , 4))
    via.append(Vehiculo("HHH666", "auto" , 2))
    via.append(Vehiculo("KKK777", "moto" , 1))
    via.append(Vehiculo("RRR888", "camion" , 4))
    via.append(Vehiculo("XXX000", "auto", 2))

    print("Via original:\n")
    print(via)

    print("\n")

    paso_preferencial(via)

    print("Via después del paso preferencial:\n")
    print(via)

    print("\n")
    
    eliminar_camiones(via)

    print("Via después de eliminar camiones:\n")
    print(via)

    print("\n")

    invertir_via(via)

    print("Via después de invertir:\n")
    print(via)


main()