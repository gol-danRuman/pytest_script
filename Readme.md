python generate_test_file.py eai/
- to generate test case file for every python module

pytest --cov-report html --cov=eai eai/
- to generate html coverage report

pytest --cov-report xml --cov=eai eai/
- to generate xml coverage report

pytest --cov-report annotate --cov=eai eai/
- to generate annotate coverage report

pytest --cov-report term-missing --cov=eai eai/
- to view coverage report with term missing

