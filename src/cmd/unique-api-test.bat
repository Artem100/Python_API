set /P path_project="Path to automation project: "
set /P tests="What api-tests do you want?: "
set datetemp=%date:~10%_%date:~4,2%_%date:~7,2%_%time:~0,2%_%time:~3,2%
pytest %path_project% --log-format="%%(message)s" -k "%tests%" --color=no --alluredir=C:/AllureReports/%datetemp%/reports/allure-results
allure serve C:/AllureReports/%datetemp%/reports/allure-results