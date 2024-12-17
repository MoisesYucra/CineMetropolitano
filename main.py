from util.ConexionBaseDatos import ConexionBaseDatos
from repositorios.CarteleraRepository import CarteleraRepository
from repositorios.ClienteRepository import ClienteRepository
from repositorios.PeliculaRepository import PeliculaRepository
from repositorios.VentaRepository import VentaRepository
from controller.CarteleraController import CarteleraController
from controller.ClienteController import ClienteController
from controller.PeliculaController import PeliculaController
from controller.VentaController import VentaController

def main():
    try:
        # Establecer la conexión a la base de datos
        conexion = ConexionBaseDatos().get_conexion()

        # Inicializar los repositorios
        cartelera_repo = CarteleraRepository(conexion)
        cliente_repo = ClienteRepository(conexion)
        pelicula_repo = PeliculaRepository(conexion)
        venta_repo = VentaRepository(conexion)

        # Inicializar los controladores
        cartelera_controller = CarteleraController(cartelera_repo)
        cliente_controller = ClienteController(cliente_repo)
        pelicula_controller = PeliculaController(pelicula_repo)
        venta_controller = VentaController(venta_repo)

        # Agregar y listar carteleras
        print("Agregando cartelera:")
        cartelera_controller.agregar_cartelera('12:00:00', '14:00:00', '2024-12-16', 1)  # Asegúrate que el formato de hora sea correcto
        cartelera_controller.listar_carteleras()

        # Agregar y listar clientes
        print("\nAgregando cliente:")
        cliente_controller.agregar_cliente('Juan', 'Perez', 'DNI', '12345678', '987654321', 'juan.perez@example.com', 'M', 1)
        cliente_controller.listar_clientes()

        # Agregar y listar películas
        print("\nAgregando película:")
        pelicula_controller.agregar_pelicula('Avatar', 120, 'Acción', 'A')
        pelicula_controller.listar_peliculas()

        # Agregar y listar ventas
        print("\nAgregando venta:")
        venta_controller.agregar_venta('2024-12-16', 5, 'Efectivo', 'Completada', 1)
        venta_controller.listar_ventas()

    except Exception as e:
        print(f"Se produjo un error: {e}")
    finally:
        if conexion.is_connected():
            conexion.close()

if __name__ == "__main__":
    main()
