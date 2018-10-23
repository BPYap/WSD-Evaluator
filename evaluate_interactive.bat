@echo off

set /p env="Enter path to the directory of virtual environment (Press Enter to ignore): "
IF NOT [%env%] == [] (call %env%\Scripts\activate.bat)

set /p algorithm="Enter name of the algorithm to be evaluated (The .py file must be placed under algorithm/): "
set /p dataset="Enter name of the dataset to be evaluated on (e.g. "semeval2015"): "
call python get_sensekey.py -a %algorithm% -d %dataset%
call java Scorer dataset\%dataset%\%dataset%.gold.key.txt evaluation_result\%dataset%\%algorithm%\%dataset%.predicted.key.txt

pause