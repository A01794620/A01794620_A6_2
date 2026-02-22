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
from enum import Enum


class MenuType(Enum):
    """
    MenyType:
    It is an enum with two types definition:
        1. Create: it interfaces to add artifacts into the system.
        2. Display: it is the boostrap to display the artifacts in
           the system, so then they can be susceptible to be either
           be modified or deleted.
    """
    CREATE = 0
    DISPLAY = 1
