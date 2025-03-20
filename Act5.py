class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        #Si aun no se han agregado valores inicializa la cabeza
        if self.head is None:
            self.head = Node(value)
        else:
            #Comienza a guardar valores a partir del ultimo nodo
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)
        self.length += 1

    #Compara en cada nodo de la lista y si lo encuentra retorna el nodo
    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return current
            current = current.next
        return None

    #Metodo exclusivo para las tareas (busca basado en la descripcion de la tarea)
    def search_by_description(self, description):
        current = self.head
        while current is not None:
            if current.value.description == description:
                return current.value
            current = current.next
        return None


    def remove(self, value):
        current=self.head
        if current.value is None: #Si aun no hay elemento en la lista no hace nada
            return
        if current.value==value: #Si la cabeza es el elemento a eliminar, pasa a ser el siguiente elemento
            self.head=current.next
            self.length -= 1
            return
        while current.next is not None: #itera la lista hasta encontrar el valor a eliminar
            if current.next.value == value:
                current.next = current.next.next #reasigna el nodo
                self.length -= 1
                return
            current = current.next

    def remove_by_description(self, description):
        current = self.head

        if current is None:
            print("Sin elementos en la lista")
            return

        if current.value.description == description:
            self.head = current.next
            self.length -= 1
            return

        while current.next is not None:
            if current.next.value.description == description:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    #funcion to String para imprimir los elementos dentro de la lista
    def __str__(self):
        Llist= ""
        if self.head is None:
            Llist = "Sin elementos"
        else:
            current = self.head
            while current:
                Llist+= str(current.value) + ","
                current = current.next

        return Llist

class Tarea:
    def __init__(self,description,estado,prioridad):
        self.description=description
        self.estado=estado #False para tareas sin terminar
        self.prioridad=prioridad

    def __str__(self):
        return ("\nTarea:{ \n"+
                "descripcion: "+self.description+",\n"+
                "estado: "+str(self.estado)+",\n"+
                "prioridad: "+str(self.prioridad)+"\n}")

    def completar_Tarea(self):
        self.estado = True


linkedList = LinkedList()
tarea1=Tarea("Tarea 1",False,1)
tarea2=Tarea("Tarea 2",False,2)
tarea3=Tarea("Tarea 3",False,3)
linkedList.append(tarea1)
linkedList.append(tarea2)
linkedList.append(tarea3)

linkedList.remove_by_description("Tarea 3")

linkedList.search_by_description("Tarea 2").completar_Tarea()

print(linkedList)






