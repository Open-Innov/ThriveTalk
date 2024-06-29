class UserException(Exception):
    """Base exception for user related errors"""
    pass


class UserNotFoundException(UserException):
    """Raised when a user is not found"""
    pass


class InvalidUserException(UserException):
    """Raised when a user is invalid"""
    pass


class PatientException(Exception):
    """Base exception for patient related errors"""
    pass


class PatientNotFoundException(PatientException):
    """Raised when a patient is not found"""
    pass


class InvalidPatientException(PatientException):
    """Raised when a patient is invalid"""
    pass


class ExerciseException(Exception):
    """Base exception for exercise related errors"""
    pass


class ExerciseNotFoundException(ExerciseException):
    """Raised when an exercise is not found"""
    pass


class InvalidExerciseException(ExerciseException):
    """Raised when an exercise is invalid"""
    pass
