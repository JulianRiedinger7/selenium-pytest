# Automation Selenium + Pytest
![agile-travel](https://github.com/JulianRiedinger7/selenium-pytest/assets/90704238/24676eeb-4fa5-4977-8e14-0ac153da9975)

## Technologies

- Selenium Webdriver
- Webdriver manager
- Python
- Pytest
- Allure-reports

## How to run the tests and see the reports

- Clone the repository
````shell
    git clone https://github.com/JulianRiedinger7/selenium-pytest.git
````
- Set up the environment
````shell
    python -m venv venv
    source venv/bin/activate # On Windows use: venv\Scripts\activate
````
- Install Dependencies
````shell
    pip install -r requirements.txt
````
- Run the tests
````shell
    pytest --browser=chrome --alluredir=allure-reports
    # (Browser can be chrome, edge or firefox)
````
- Serve the report
````shell
    allure serve allure-reports
````