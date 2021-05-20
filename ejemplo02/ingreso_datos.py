from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# lectura de los dos archivos
dataclub = open('data/datos_clubs.txt','r')
dataJugadores = open('data/datos_jugadores.txt', 'r')
# ciclo para agregar los clubes
for a in dataclub:
    #Separacion de los atributos de cada fila
    fila = a.rstrip().split(';')
    # Agregar los datos
    c = Club(nombre=fila[0],deporte=fila[1], fundacion=fila[2])
    session.add(c)
# ciclo para agregar los jugadores
for b in dataJugadores:
    #Separacion de los atributos de cada fila
    fila = b.rstrip().split(';')
    # almacenar el club cuando se el jugador pertenezca a este
    aux = session.query(Club).filter_by(nombre = fila[0]).first()
    #Agregar datos
    j = Jugador(nombre=fila[3], dorsal=fila[2], posicion=fila[1],club=aux)
    session.add(j)

dataclub.close()
dataJugadores.close()
session.commit()    




