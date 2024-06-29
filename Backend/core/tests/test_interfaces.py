import unittest
from abc import ABC

from Backend.core.interfaces.interfaces import IUser, IPatient, IExercise


class TestUser(IUser, ABC):
    def get(self, user_id):
        raise Exception("TestUser.get method called")

    def create(self, user_data):
        raise Exception("TestUser.create method called")

    def update(self, user_id, user_data):
        raise Exception("TestUser.update method called")

    def delete(self, user_id):
        raise Exception("TestUser.delete method called")


class TestPatient(IPatient, ABC):
    def get(self, patient_id):
        raise Exception("TestPatient.get method called")

    def create(self, patient):
        raise Exception("TestPatient.create method called")

    def update(self, patient_id, patient):
        raise Exception("TestPatient.update method called")

    def delete(self, patient_id):
        raise Exception("TestPatient.delete method called")

    def login(self, username, password):
        raise Exception("TestPatient.login method called")

    def logout(self):
        raise Exception("TestPatient.logout method called")

    def start_exercise(self, exercise_id):
        raise Exception("TestPatient.start_exercise method called")

    def validate_exercise_data(self, exercise_data):
        raise Exception("TestPatient.validate_exercise_data method called")

    def handle_error(self, error):
        raise Exception("TestPatient.handle_error method called")

    def auto_record_progress(self, exercise_id, progress):
        raise Exception("TestPatient.auto_record_progress method called")

    def view_exercise_history(self):
        raise Exception("TestPatient.view_exercise_history method called")

    def receive_notifications(self):
        raise Exception("TestPatient.receive_notifications method called")

    def view_notifications(self):
        raise Exception("TestPatient.view_notifications method called")

    def view_exercise(self, exercise_id):
        raise Exception("TestPatient.view_exercise method called")

    def view_exercise_list(self):
        raise Exception("TestPatient.view_exercise_list method called")

    def view_exercise_progress(self, exercise_id):
        raise Exception("TestPatient.view_exercise_progress method called")


class TestExercise(IExercise, ABC):
    def get(self, exercise_id):
        raise Exception("TestExercise.get method called")

    def create(self, exercise):
        raise Exception("TestExercise.create method called")

    def update(self, exercise_id, exercise):
        raise Exception("TestExercise.update method called")

    def delete(self, exercise_id):
        raise Exception("TestExercise.delete method called")


class TestInterfaces(unittest.TestCase):
    def setUp(self):
        self.user = TestUser()
        self.patient = TestPatient()
        self.exercise = TestExercise()

    def test_user_interface(self):
        with self.assertRaises(Exception) as context:
            self.user.get(1)
        self.assertTrue("TestUser.get method called" in str(context.exception))

    def test_patient_interface(self):
        with self.assertRaises(Exception) as context:
            self.patient.get(1)
        self.assertTrue("TestPatient.get method called" in str(context.exception))

    def test_exercise_interface(self):
        with self.assertRaises(Exception) as context:
            self.exercise.get(1)
        self.assertTrue("TestExercise.get method called" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
