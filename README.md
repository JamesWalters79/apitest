# Running Tests 

**Create allure report for unit-tests (using allure-pytest plugin)**

*pytest -p allure_pytest --alluredir=allure-results*

**Create allure report for BDD tests (using allure-pytest-bdd plugin)**

*pytest -p allure_pytest_bdd --alluredir=allure-bdd-results*

# Allure Test Reporting

**Generate Allure Report with Test Results for BDD tests**

*allure generate allure-bdd-results --clean*

**Open Generated Report**

*allure open*

