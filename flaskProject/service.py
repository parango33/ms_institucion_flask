from models import InstitucionModel


class InstitucionService:
    def __init__(self):
        self.model = InstitucionModel()

    def create_institucion(self, params):
        '''
        Crear institucion
        '''
        self.model.create(params["Nombre"], params["Nit"])

    def select_institucion(self, pNombre):
        '''
        Trae una insitucion por su nombre
        '''
        self.model.select(pNombre)

    def select_all_instituciones(self):
        '''
        Trae todas las instituciones
        '''
        self.model.select_all()

