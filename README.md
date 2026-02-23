# Exercise of Programming 3 and Unity Testing 6.2

| **MNA Class**                       | Pruebas de Software y Aseguramiento de la Calidad (TC4017) |
|-------------------------------------|------------------------------------------------------------|
| **Author**                          | Ronald Sandí Quesada                                       |
| **Student-ID**                      | A01794620                                                  |
| **E-mail**                          | A01794620@tec.mx                                           |
| **Professors:**                     |                                                            |
| &nbsp;&nbsp;**Professor**           | PhD. Gerardo Padilla Zárate                                |
| &nbsp;&nbsp;**Evaluator and Tutor** | PhD. Daniel Flores Araiza                                  |
| **Period**                          | I Trimester 2026                                           |
| **Date**                            | 22/02/20226                                                 |

## Introduction.

This document exhibits the dynamic of coding and applying: 
* Static analysis for quality assurance using Pylint and Flake8
* Running the tool Coverage to check the running code portion coverage.
* In the process of creating a reservation system.
* Adding Unity Testing

The process of building a valid deliverable is described in the next main steps:

1.	Understanding the main problem and its specific requirements.
2.	Installation of the support libraries: Pylint, Flake8 and Converage.
3.	Coding the solution.
4.	Initial testing for preparing the environment.
5.	Testing using Pylint static analysis tool, under PEP-8 standards. 
6.  Fixing inconsistencies and bugs detected by Pylint. 
7.  Testing using Flake8 analysis tool, under PEP-8 standards.
8.  Fixing inconsistencies and bugs detected by Flake8.
9.  Assessing the solution by using a battery of Unity tests as per system functions.

## Product deliverable.

The following deliverable is the main part of the final solution.

Program for the Programming Individual Exercise:
Reservation System using Unity Testing (Exersice 6.2)

---
* **Program #1. Reservation system:
  * The motive of the program is to simulate an essential reservation system.
  * It includes Customers, Hotels and Reservations.
  * compile the sales totals using the information from both files.
---

## Structure of the Project.

The GitHub repository has the following structure.

**Table 1.** Project structure in GitHub repository.

| Folder in A01794620_A6_2 repository | Details                                                                                                                                                                                                                                                                            |   |   |   |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---|---|---|
| abstractions                        | This package holds the essential entities of the system: 1. Customer. 2. Hotel. 3. Reservation.                                                                                                                                                                                    |   |   |   |
| cli                                 | This packages holds all the classes and functions to enable the system user to interacts with the application. It uses CLI (command line interface) to send messages to the system, and it also allows the system to dispatch back to the commands ordered by the of the end-user. |   |   |   |
| datahandling                        | This package holds only one handy class, the most relevant to file persistence. JSON handler package.                                                                                                                                                                              |   |   |   |
| dataset                             | This where all the artifacts are stored in JSON files. Every main subject has a folder in.                                                                                                                                                                                         |   |   |   |
| setting                             | This is global system settings, which are default and essential for system to start (bootstrapping).                                                                                                                                                                               |   |   |   |
| tests                               | This is where all the unit testing are, following stardanrds one folder mirrored per every folder simulating unit testing.                                                                                                                                                         |   |   |   |

## Quality Assurance using Pylint and Flake 8.
 
Majority of the issues found in both tools combined are :

* Lines to long.
* The lack of docstrings for documentation.
* Lack of double spaces in the beginning of classes.
* In some cases/funcions were needed to tolerate the following exceptions codes, because of the nature of the code returned: (too-many-branches), (too-many-statements), (too-many-nested-blocks) and (too-many-locals); using the codes R0912, R0915, R1702 and R0914.

## Classes Links.

**Table 2.** Classes Links.

| Class  | Code | Motive |
|--------|------|--------|
|        | [Go](https://github.com/A01794620/A01794620_A5_2/)      |        |
|        |      |        |
|        |      |        |
|        |      |        |


## Unit Test Cases:

## Positive Test Cases.

## Negative -Intended- Test Cases.

## Methodological references.

The following material helped on validation inside classes:

* The Library Phone-Numbers in Dale (2026) for number verification.
* Console-Menu in Sphinx (2018) fantastic libray, it was the base for the CLI of the actual work.
* The commits of the project had been performed using the techniques described in Buchea(2026) and Conventional Commits (2026).
* The amazing Coverage tool from Sphinx (2026) used to check the code coverage.

## System Images:

## Coverage Images:

## Unity Testing Images:

## Pylint Images:

## Flake8 Images:



## APA References:
* Conventional Commits (2026). _Conventional Commits_. Recovered on February 12, 2026 form https://www.conventionalcommits.org/en/v1.0.0/
* Buchea, J. (2026). _Semantic Commit Messages_. Recovered on February 12, 2026 from https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716
* Dale, D (2026). Project Description PhoneNumbers Python Library. Recovered on February 18, 2026 from https://pypi.org/project/phonenumbers
* Sphinx (2018). Welcome to console-menu’s documentation! Recovered on February 18, 2026 from https://console-menu.readthedocs.io/en/latest/index.html
* Sphinx (2026). Coverage.py. Recovered on February 18, 2026 from https://coverage.readthedocs.io/en/7.13.4/#