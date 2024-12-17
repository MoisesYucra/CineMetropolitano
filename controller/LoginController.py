class UsuarioController:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def login(self, correo, password):
        usuario = self.usuario_repository.get_usuario_by_email(correo)
        if usuario and usuario["password"] == password:  
            return usuario
        return None

    def registrar_usuario(self, nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol):
        self.usuario_repository.insert_usuario(nombre, apellido, tipo_doc, numero_doc, telefono, correo, genero, id_rol)
