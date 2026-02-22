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

This packages holds all the classes and functions
to enable the system user to interacts with the
application.
It uses CLI (command line interface) to send messages
to the system, and it also allows the system to dispatch
back to the commands ordered by the of the end-user.

Handlers. Every entity has a CLI handler.

    * CustomerHandler.
    * HotelHandler.
    * ReservationHandler.

Every handler is articulated by a super handler component
which is the MenuHandler, which holds all the deployed
system functions.

Others classes that helps on CLI process:

* MenuDescriptor: it is a placeholder container to holds
                  all the menu displayed options and labels.
* MenyType: it is an enum with two types definition:
    1. Create: it interfaces to add artifacts into the system.
    2. Display: it is the boostrap to display the artifacts in
       the system, so then they can be susceptible to be either
        be modified or deleted.
"""
