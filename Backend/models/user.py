from Backend.core.interfaces.interfaces import IUser

class User(IUser):
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password

    def get(self, user_id):
        # Implémentation pour récupérer un utilisateur par son ID
        pass

    def create(self, user):
        # Implémentation pour créer un nouvel utilisateur
        pass

    def update(self, user_id, user):
        # Implémentation pour mettre à jour un utilisateur par son ID
        pass

    def delete(self, user_id):
        # Implémentation pour supprimer un utilisateur par son ID
        pass