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


def main():

    via = DoublyLinkedList()

    via.append(Vehiculo("AAA111", "auto" , 3))
    via.append(Vehiculo("BBB222", "moto" , 1))
    via.append(Vehiculo("CCC333", "camion" , 4))
    via.append(Vehiculo("DDD444", "auto" , 2))
    via.append(Vehiculo("EEE555", "moto", 1))
    via.append(Vehiculo("HHH666", "auto" , 2))
    via.append(Vehiculo("KKK777", "moto" , 1))

    print("Via original:\n")
    print(via)

    print("\n")

    paso_preferencial(via)

    print("Via después del paso preferencial:\n")
    print(via)


main()