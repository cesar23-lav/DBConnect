import pyodbc
from prettytable import PrettyTable

SERVER = 'localhost'
DATABASE = 'DBEscuela'
DRIVER = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;'

def conectar():
    """
    Establece y retorna la conexión a la base de datos.
    """
    try:
        conexion = pyodbc.connect(connection_string)
        return conexion
    except Exception as event:
        print(f"Error al conectar a la base de datos: {event}")
        return None

def listar_alumnos():
    """
    Obtiene y muestra todos los registros de la tabla Alumno
    """
    miTabla = PrettyTable(["ID", "NOMBRES", "APELLIDOS", "CODIGO PERSONAL"])
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            consulta = "SELECT id_alumno, nombres, apellidos, codigo_personal FROM Alumno"
            cursor.execute(consulta)

            alumnos = cursor.fetchall()

            print(f"\nLista de Alumnos en {DATABASE}\n")
            if not alumnos:
                print("No hay alumnos registrados.")
            else:
                for alumno in alumnos:
                    miTabla.add_row([alumno.id_alumno, alumno.nombres, alumno.apellidos, alumno.codigo_personal])
                print(miTabla)
                print("")
        except Exception as event:
            print(f"Error al listar los usuarios: {event}")
        finally:
            conexion.close()

if __name__ == "__main__":
    listar_alumnos()