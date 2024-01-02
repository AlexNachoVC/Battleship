import random                                                                                              # Se importa la librería random

tablero = [["O" for _ in range(10)] for _ in range(10)]                                                    # Se define un list comprehension, que anida dos for loops con rango 10 para poder crear el tablero. La logíca es que tablero inicializa una lista vacía en la lista exterior, en la cual funciona el primer for loop en el cual se crea la lista interior vacia (correspondiente a las filas), en la cual funciona el segundo for loop, que colocara una "O" por cada "columna" dentro del rango (10), hasta que se "llene cada fila", al llenarse una fila, esta fila se añade a la lista vacía correspondiente al tablero, y se itera hasta llenarse una "matriz" de 10*10. Se utilizo esta estructura, por comodidad y espacio
numBarcos = 5                                                                                              # Se define el numero de barcos en una variable hardcodeada

def colocarBarcos(tablero, numBarcos):                                                                     # Se define la función colocarBarcos, que toma como argumentos, las dos variables previamente definidas
    barcosColocados = set()                                                                                # Se crea un set vacio que servira para guardar las ubicaciones creadas en el loop de la función
    while len(barcosColocados) < numBarcos:                                                                # Se define un while loop que funcionara mientras la cantidad de barcosColocados (Que empieza en 0), sea menor que numBarcos (Que esta hardcodeado)
        filaBarco = random.randint(0, len(tablero) - 1)                                                    # Se define la variable filaBarco, a la que se le asignara un valor aleatorio (utilizando el metodo randint, de la libreria random) entre 0 y el numero final del tamaño del tablero (usando len(tablero)-1, porque empieza en 0 el conteo)
        columnaBarco = random.randint(0, len(tablero[0]) - 1)                                              # Se define la variable columnaBarco, a la que se le asignara un valor aleatorio (utilizando el metodo randint, de la libreria random) entre 0 y el numero final del tamaño del tablero (usando len(tablero)-1, porque empieza en 0 el conteo)
        nuevaPosicion = (filaBarco, columnaBarco)                                                          # Se define la variable nuevaPosicion, a la que se le asignaran en un tuple, los datos obtenidos de filaBarco y columnaBarco
        if nuevaPosicion not in barcosColocados:                                                           # Usando condicionales, se checa si el tuple asignado en la variable nuevaPosicion ya existe en el set barcosColocados
            barcosColocados.add(nuevaPosicion)                                                             # Si no existe en el set, se le añade el tuple de la variable nuevaPosicion al set barcosColocados
    return barcosColocados                                                                                 # Al completar una iteracion, se regresa el set barcosColocados, con los cambios dados

barcosColocados = colocarBarcos(tablero, numBarcos)                                                        # Se define, fuera de la funcion, el set barcosColocados. Que llamara a la funcion colocarBarcos, para asignarle valores
# print(barcosColocados) # TEST

def mostrarTablero(tablero):                                                                               # Se define la funcion mostrarTablero, que tomara como argumento la list comprehension "tablero"
    print("  " + " ".join(str(i) for i in range(len(tablero[0]))))                                         # Se imprimen los numeros de las columnas. El primer " " se utiliza para alinear las columnas, después del "+", se genera un string que representa el número de cada columna. El "range(len(tablero[0]))" genera una secuencia de numeros del 0 al número de columnas en "tablero" (utilizando la funcion len()), "str(i) for i in range" convierte cada numero de la secuencia en una string, " " ".join(...)" une cada uno de los strings de numeros generados, pero con un espacio entre ellos.
    for i, fila in enumerate(tablero):                                                                     # Se utiliza un for loop que iterara por cada fila en el tablero. La función "enumerate" se usa para guardar el valor del indice (i) de la fila actual en el loop
        print(i, " ".join(fila))                                                                           # Se imprime el numero de filas. "i" representa el indice de la fila actual, y se imprime antes del contenido de la fila. " " ".join(fila)" une los elementos del contenido de "fila" en con el número de esta, separados por un espacio

def obtenerInputUsuario(tablero):                                                                          # Se define la función obtenerInputUsuario, que toma como argumento "tablero"
    try:                                                                                                   # Se utiliza un bloque try, para poder limitar el tipo de dato que el usuario puede ingresar como input
        filaInput = int(input("Elige una fila: "))                                                         # Se le solicita al usuario un numero correspondiente a la fila de su elección. El input se convierte a entero, y  se asigna en la variable filaInput
        columnaInput = int(input("Elige una columna: "))                                                   # Se le solicita al usuario un numero correspondiente a la columna de su elección. El input se convierte a entero, y se asigna en la variable columnaInput
        return filaInput, columnaInput                                                                     # Si el usuario ingreso correctamente dos enteros validos, se regresan las variables con sus inputs en una tupla
    except ValueError:                                                                                     # Se utiliza un bloque except, para poder manejar un input de tipo de dato incorrecto (Por ejemplo, si no fue posible convertir el input a entero; se "levanta" un ValueError)
        print("Input inválido. Por favor, ingresa números válidos.")                                       # Se le imprime un mensaje de notificación de error al usuario, en caso de presentarse un ValueError. Y se le pide ingresar un input valido
        return obtenerInputUsuario(tablero)                                                                # Después de mostrar el mensaje, la función se vuelve a llamar a si misma, y se reinicia el proceso. Esto seguira pasando hasta que el input sea valido

def checkInput(filaInput, columnaInput, barcosColocados):                                                  # Se define la función checkInput, que toma como argumentos filaInput, columnaInput y barcosColocados
    if (filaInput, columnaInput) in barcosColocados:                                                       # Utilizando condicionales, se checa si una tupla de inputs del usuario coincide con una de las tuplas almacenadas en el set barcosColocados
        barcosColocados.remove((filaInput, columnaInput))                                                  # Si coincide una tupla, se quita la tupla coincidente del set barcosColocados, para que cuando vuelva a haber un input, no se pueda "volver a tirar" ese barco
        tablero[filaInput][columnaInput] = "/"                                                             # Si coincide una tupla, se cambia la "O" de la posición atinada por un "/" para mostrar que en esa posición se tiro un barco
        return "¡Hundiste un barco! \n"                                                                    # Si coinicde una tupla, se regresa el mensaje de hundiste un barco
    else:                                                                                                  # Si no coincide una tupla, se entra a otra serie de condicionales, para confirmar que caso se presento
        if (0 <= filaInput < len(tablero)) and (0 <= columnaInput < len(tablero[0])):                      # Si el input de la fila y el de la columna entran dentro los limites definidos del tablero, pero no correspondia a ninguna ubicación de barco, se ingresa a los siguientes condicionales, para checar que caso se cumple
            if tablero[filaInput][columnaInput] == "X" or tablero[filaInput][columnaInput] =="/":          # Si el input estaba dentro de los limites, pero en la ubicación elegida se encuentra una "X" o una "/" en lugar de una "O", se le notifica al usuario que ya había dicho esa ubicación
                return "Ya habias dicho esa ubicación. \n"
            else:                                                                                          # Si el input estaba dentro de los limites, pero la ubicación no estaba en el set barcosColocados, y no era una ubicación ya seleccionada, se cambia la "O" de esa posición por una "X", y se muestra un mensaje de que no se le atino a ningún barco
                tablero[filaInput][columnaInput] = "X"
                return "No le atinaste a ningún barco. \n"
        else:                                                                                              # Mensaje de error, si la ubicación del input excedia los limites definidos del tablero
            return "Uy. Esa ubicación ni siquiera existe. \n"


def juego():                                                                                               # Se define la función juego
    print("     ¡Bienvenid@!     \n")                                                                       # Se imprime una bienvenida e instrucciones
    print("----Instrucciones----\n")
    print("""1. Inicio del juego:
   • El programa posicionara aleatoriamente al menos 5 barcos sencillos en un tablero de 10x10.
   • Cada barco ocupará una celda en el tablero (una casilla de 1x1).
2.  Tu turno:
   • Tienes un total de 10 intentos para adivinar la ubicación de los barcos.
   • El tablero estará etiquetado con coordenadas, por ejemplo, desde (0,0) hasta (9,9), para que puedas especificar tus adivinanzas.
3.  Realizar una adivinanza:
   • En tu turno, elige una celda del tablero (por ejemplo, "(1,9)") donde creas que podría estar ubicado un barco e introdúcela.
   • La computadora te dirá si tu adivinanza fue "acertada" (toca un barco) o "fallada" (no toca ningún barco).
4.  Objetivo:
   • El objetivo es adivinar la ubicación de todos los barcos con la menor cantidad de intentos posibles.
5.  Continúa adivinando:
   • Continúa adivinando las ubicaciones de los barcos en el tablero hasta que adivines todas las ubicaciones de los barcos o agotes tus 10 intentos.
   • Si repites una ubicación previamente dicha, se te quitara un intento.
6.  Ganar o perder:
   • Ganarás el juego si adivinas exitosamente las ubicaciones de todos los barcos antes de agotar tus 10 intentos.
   • Perderás si usas todos tus intentos sin adivinar todas las ubicaciones de los barcos. \n\n """)

    print(" ¡Juguemos Battleship! \n")


    mostrarTablero(tablero)                                                                                # Al inicio del juego, y después de las instrucciones, se muestra el tablero

    for turno in range(10):                                                                                # Se utiliza un for loop, que en su interior," dara el juego" por cada turno que el usuario tenga (en este caso, siguiendo las instrucciones, 10)
        print(f"\nTurno {turno + 1}")                                                                      # Se le muestra al usuario el turno en el que va, utilizando un fstring, que muestra la iteración+1 (esto porque la primera iteración es 0, y queremos que el usuario vea el turno 1 primero)
        filaInput, columnaInput = obtenerInputUsuario(tablero)                                             # Se asigna el valor de las variables filaInput, y columnaInput, llamnando a la funcion obtenerInputUsuario (explicada previamente)
        resultado = checkInput(filaInput, columnaInput, barcosColocados)                                   # Se checa el resultado del input, llamando a la función checkInput (explicada previamente), y se asigna en la variable resultado
        print(resultado)                                                                                   # Se le muestra al usuario su resultado, que es un mensaje preestablecido por la función checkInput
        mostrarTablero(tablero)                                                                            # Se vuelve a mostrar el tablero (llamando a la función mostrarTablero), pero ahora modificado en base al input del usuario

        if not barcosColocados:                                                                            # Si ya no quedan tuplas en el set barcosColocados, significa que se hundieron todos los barcos, por lo que se le muestra un mensaje al usuario, y se rompe la función, para terminar el juego
            print("Hundiste todos los barcos. ¡Ganaste!")
            break

    if barcosColocados:                                                                                    # Si todavía quedan tuplas en el set barcosColocados, significa que no se hundieron todos los barcos
        print("\nGame over. No hundiste todos los barcos.")                                                # Por lo que se le muestra al usuario un mensaje de Game Over
        print("Ubicaciones de los barcos no hundidos:")                                                    # Al igual que se le muestra un mensaje que dice las ubicaciones de los barcos no hundidos
        for fila, columna in barcosColocados:                                                              # La ubicación se mostrara usando un for loop, que itere por cada fila y columna de las tuplas restantes, y se mostrara cada iteración en un formato preestablecido
            print(f"Fila: {fila}, Columna: {columna}")


juego()                                                                                                    # Se llama a la función juego(), y empieza todo.
