"""
 Module. AbstractionType. Exercise of Programming 3 and Unity Testing 6.2
 @Motive . Unity Testing
           Code Coverage Evaluation
           PEP8 check with Pylint and Flake8
 @author . Ronald Sandí Quesada
 @Student-ID . A01794620
 @email . A01794620@tec.mx
 @MNA Class . Pruebas de Software y Aseguramiento de la Calidad (TC4017)
 @Professor . PhD Gerardo Padilla Zárate
 @Professor Evaluator and Tutor . PhD Daniel Flores Araiza
 @Period . I Trimester 2026
 @Date: 22 February 2026
"""
import uuid


class UuidHandler():
    """
    Handle class as a factory for
    UUID-4 codes for the whole system.
    It should be the exclusive factory to
    generate and validate IDs
    """
    @staticmethod
    def is_valid_id(uuid_):
        """
        It checks if the provided strig represents a
        valid UUID-4 on its format.
        Args:
            uuid_ (str): proposed UUID.
        Returns:
            bool: Truth if the evaluation matches
                  on the provided UUID.
        """
        try:
            uuid_obj = uuid.UUID(uuid_, version=4)
        except ValueError:
            return False

        return str(uuid_obj) == uuid_

    @staticmethod
    def get_next_id():
        """
        It returns the next UUID-4 available.
        If this factory is followed then the
        previous method should yield positive
        always.
        Args:
            (void): the calculation is internal.
        Returns:
            string: then next UUID-4 available.
        """
        return str(uuid.uuid4())
