# Python `coverage` Module Commands

## Resources

* <https://pypi.org/project/coverage/>

## Usage

* `coverage run manage.py test` - Run all tests in the project
* `coverage run manage.py test <app_name>` - Run all tests in the app
* `coverage run manage.py test <app_name>.<test_name>` - Run a specific test module
* `coverage run manage.py test <app_name>.<test_name>.<test_class_name>` - Run a specific test class
* `coverage run manage.py test <app_name>.<test_name>.<test_class_name>.<test_method_name>` - Run a specific test method
* `coverage report` - Show coverage report
* `coverage html` - Generate HTML coverage report

## Run Specific Tests

* `coverage run manage.py test vitals.tests.test_admin`
