# Running Tests 

**Create allure report for unit-tests (using allure-pytest plugin)**

*pytest -p allure_pytest --alluredir=allure-results*

**Create allure report for BDD tests (using allure-pytest-bdd plugin)**

*pytest -p allure_pytest_bdd --alluredir=allure-bdd-results*

**Create allure report for BDD tests using specific tags (using allure-pytest-bdd plugin)**

***tagged with bdd only***

*pytest -m "bdd" -p allure_pytest_bdd --alluredir=allure-bdd-results*

***tagged with bdd and neo_core only***

*pytest -m "bdd and neo_core" -p allure_pytest_bdd --alluredir=allure-bdd-results*

***tagged with bdd and not neo_core***

*pytest -m "bdd and not neo_core" -p allure_pytest_bdd --alluredir=allure-bdd-results*

# Allure Test Reporting

**Generate Allure Report with Test Results for BDD tests**

*allure generate allure-bdd-results --clean*

**Open Generated Report**

*allure open*

