from abc import ABC, abstractmethod


class IUser(ABC):
    @abstractmethod
    def get(self, user_id):
        pass

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def update(self, user_id, user):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass


class IPatient(ABC):
    @abstractmethod
    def get(self, patient_id):
        pass

    @abstractmethod
    def create(self, patient):
        pass

    @abstractmethod
    def update(self, patient_id, patient):
        pass

    @abstractmethod
    def delete(self, patient_id):
        pass

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def start_exercise(self, exercise_id):
        pass

    @abstractmethod
    def validate_exercise_data(self, exercise_data):
        pass

    @abstractmethod
    def handle_error(self, error):
        pass

    @abstractmethod
    def auto_record_progress(self, exercise_id, progress):
        pass

    @abstractmethod
    def view_exercise_history(self):
        pass

    @abstractmethod
    def receive_notifications(self):
        pass

    @abstractmethod
    def view_notifications(self):
        pass

    @abstractmethod
    def view_exercise(self, exercise_id):
        pass

    @abstractmethod
    def view_exercise_list(self):
        pass

    @abstractmethod
    def view_exercise_progress(self, exercise_id):
        pass


class IExercise(ABC):
    @abstractmethod
    def get(self, exercise_id):
        pass

    @abstractmethod
    def create(self, exercise):
        pass

    @abstractmethod
    def update(self, exercise_id, exercise):
        pass

    @abstractmethod
    def delete(self, exercise_id):
        pass
