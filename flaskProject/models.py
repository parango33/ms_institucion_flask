# 1.import sqlite
import sqlite3


class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('institucion.db') #cambiar nombre
        self.create_institucion_table()

    def create_institucion_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Institucion" (
          id INTEGER PRIMARY KEY,
          Nombre TEXT,
          Nit TEXT
        );
        """

        self.conn.execute(query)


class InstitucionModel:
    TABLENAME = "Institucion"

    def __init__(self):
        self.conn = sqlite3.connect('institucion.db')

    def create(self, pNombre, pNit):
        '''
        Crea una institucion
        '''
        query = f'insert into Institucion ' \
                f'(Nombre, Nit) ' \
                f'values ("{pNombre}","{pNit}")'

        result = self.conn.execute(query)
        return result

    def select(self,pNombre):
        '''
        Trae una institucion
        '''
        query = f'select * from Institucion' \
                f'where Nombre like {pNombre}'

        result = self.conn.execute(query)
        return result

    def select_all(self):
        '''
        Trae todas las instituciones
        '''
        query = f'select * from Institucion'
        result = self.conn.execute(query)
        return result
