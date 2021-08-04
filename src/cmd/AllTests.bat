set /P path_project="Path to automation project: "
set dayMonthYear=%Date:~7,2%_%Date:~4,2%_%Date:~10,4%
set datetemp=%Date:~7,2%_%Date:~4,2%_%Date:~10,4%_%time:~0,2%_%time:~3,2%
pytest %path_project% --log-format="%%(message)s" --reruns 3 --color=no --alluredir=C:/AllureReports/%datetemp%/reports/allure-results
allure serve C:/AllureReports/%datetemp%/reports/allure-results