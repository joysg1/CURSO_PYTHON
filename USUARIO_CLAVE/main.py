from tkinter import Tk
from modulo_visual import Aplicacion
from modulo_db import Database


def main():
    root = Tk()
    app = Aplicacion(root)
    root.mainloop()

if __name__ == "__main__":
    db = Database('mi_base_de_datos.db')
    db.crear_tabla()
    main()
    db.cerrar_conexion()