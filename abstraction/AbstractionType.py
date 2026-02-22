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


class AbstractionType(Enum):
    """
    AbstractionType:
    This is an enumeration class that helps to iterate though
    the essential subject classes: Customer, Hotel and Reservation.
    These three abstractions are the core of the whole system.
    """
    CUSTOMER = 0
    HOTEL = 1
    RESERVATION = 2
