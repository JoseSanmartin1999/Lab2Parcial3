#retorna el costo minimo en un vector si hay varios estados objetivos
def BusquedaLab(objetivo,inicio):
    # costo mínimo hasta el estado del objetivo desde el inicio
    global grafos,costo    
    respuesta=[]
    # crear una cola de prioridad
    cola = []
    # establecer el vector de respuesta al valor máximo
    for i in range(len(objetivo)):
        respuesta.append(10**8) 
    # insertar el índice inicial
    cola.append([0,inicio])
    # mapa para almacenar el nodo visitado
    visitado = {}
    # contar
    cuenta = 0
    #Mientras la cola no este vacia 
    while(len(cola)>0):
        # obtener el elemento superior de la cola
        cola=sorted(cola)
        p=cola[-1]
        #pop de elemento 
        del cola[-1]
        # obtener el valor original
        p[0]*=-1
        # Chequear si el elemento es parte de la lista objetivo
        if (p[1] in objetivo):
            index=objetivo.index(p[1])
            # si se alcanza una nueva meta
            if(respuesta[index]== 10**8):
                cuenta += 1
            # si el costo es menor
            if (respuesta[index] > p[0]):
                respuesta[index] = p[0]
            #eliminar el elemento
            del cola[-1]
            cola = sorted(cola)
            if (cuenta == len(objetivo)):
                return respuesta        
    # verificar los nodos no visitados que están adyacentes al nodo actual
        if (p[1] not in visitado):
            for i in range(len(grafos[p[1]])):
                # valor se multiplica por -1 para que la menor prioridad está en la parte superior				
                cola.append( [(p[0] + costo[(p[1], grafos[p[1]][i])])* -1, grafos[p[1]][i]])
            # mark as visited
        visitado[p[1]] = 1
    return respuesta

# main funcion
if __name__ == '__main__':

    #Creamos el grafo
    grafos,costo = [[] for i in range(10)],{}

    # grafos es una lista de listas. Cada elemento de la lista externa corresponde a un nodo y la 
    # respectiva lista interna contiene los nodos vecinos    
    # costo es un diccionario
    # Agregamos una variable que nos represente una parada o vertice      
    urb_CIEEPI=0
    # Agregamos una variable que nos represente una parada o vertice      
    parada_buses_6_junio=1
    # Agregamos una variable que nos represente una parada o vertice      
    puente_8=2
    # Agregamos una variable que nos represente una parada o vertice      
    admintracion_valle_de_los_chillos=3
    # Agregamos una variable que nos represente una parada o vertice      
    san_jose=4
    # Agregamos una variable que nos represente una parada o vertice      
    parque_kingman=5
    # Agregamos una variable que nos represente una parada o vertice      
    mega_kiwi=6
    # Agregamos una variable que nos represente una parada o vertice      
    triangulo=7
    # Agregamos una variable que nos represente una parada o vertice      
    san_luis=8
    # Agregamos una variable que nos represente una parada o vertice 
    espe=9
    #Añadir Borde
    #Esta es la accion de moverse desde mi punto Urb CIEEPi hacia Parada de Buses 6 De Junio
    grafos[urb_CIEEPI].append(parada_buses_6_junio)
    #Esta es la accion de moverse desde mi punto Urb CIEEPi hacia Adminstracion Valle de los Chillos 
    grafos[urb_CIEEPI].append(admintracion_valle_de_los_chillos)   
    #Esta es la accion de moverse desde mi punto Para de Buses 6 de Junio hacia Puente 8
    grafos[parada_buses_6_junio].append(puente_8)
    #Esta es la accion de moverse desde mi punto Puente 8 hacia ESPE
    grafos[puente_8].append(espe)
    #Esta es la accion de moverse desde mi punto Administracion Valle de los Chillos  hacia San Jose 
    grafos[admintracion_valle_de_los_chillos].append(san_jose)
    #Esta es la accion de moverse desde mi punto Administracion Valle de los Chillso hacia Parque Kingman 
    grafos[admintracion_valle_de_los_chillos].append(parque_kingman)
    #Esta es la accion de moverse desde mi punto San JOSEhacia Parque Kingman 
    grafos[san_jose].append(parque_kingman)
    #Esta es la accion de moverse desde mi punto Parque Kingman hacia Mega Kiwi 
    grafos[parque_kingman].append(mega_kiwi)
    #Esta es la accion de moverse desde mi punto San Jose hacia Triangulo
    grafos[san_jose].append(triangulo)
    #Esta es la accion de moverse desde mi punto Mega Kiwi hacia San Luis
    grafos[mega_kiwi].append(san_luis)
    #Esta es la accion de moverse desde mi punto Triangulo hacia San Luis
    grafos[triangulo].append(san_luis)
    #Esta es la accion de moverse desde mi punto San Luis hacia ESPE
    grafos[san_luis].append(espe)
   

    # añade el costo de moverse de un vertice a otro
    costo[(urb_CIEEPI, parada_buses_6_junio)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(urb_CIEEPI, admintracion_valle_de_los_chillos)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(parada_buses_6_junio, puente_8)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(puente_8, espe)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(admintracion_valle_de_los_chillos, san_jose)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(admintracion_valle_de_los_chillos, parque_kingman)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(san_jose, parque_kingman)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(parque_kingman, mega_kiwi)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(san_jose, triangulo)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(mega_kiwi, san_luis)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(triangulo, san_luis)] = 1
    # añade el costo de moverse de un vertice a otro
    costo[(san_luis, espe)] = 1
   
    
    

    # Estado Objetivo
    objetivo = []
    objetivo1 = []
    objetivo2 = []

    # Establecer el objetivo puede exisitr varios estados objetivos 
    
    objetivo.append(9)
    objetivo1.append(8)
    objetivo2.append(6)

    # obtener la respuesta
    respuesta = BusquedaLab(objetivo, 0)
    respuesta1=BusquedaLab(objetivo1,0)
    respuesta2=BusquedaLab(objetivo2,0)

    # print the answer
def principal():
    opcion=input("Ingrese la opcion que quiera consultar: \n1.- Para la ruta 1 \n2.- Para la ruta 2 \n3.-Para la ruta 3 \n 0.- Para salir \nOpcion: ")
    while opcion != "0":
        if opcion =="1":
            print("La ruta 1 es: [Urb CIEEPI-Parada de Buses 6 de Junio-Puente 8- ESPE]")
            print("El costo minimo para llegar de CIIEPI a ESPE es = ",respuesta[0])
        elif opcion =="2":
            print("La ruta 2 es: [Urb CIEEPI-Adminstriacion Valle- San Jose -Triangulo-San Luis- ESPE]")
            print("El costo minimo para llegar de CIIEPI a ESPE es = ",respuesta1[0]+1)
        elif opcion =="3":
            print("La ruta 3 es: [Urb CIEEPI-Adminstriacion Valle-San Jose-Parque Kingman-Mega Kiwi-San Luis- ESPE]")
            print("El costo minimo para llegar de CIIEPI a ESPE es = ",respuesta2[0]+3)
        else:
            print("opcion no valida")
        
        return principal()
            
principal()