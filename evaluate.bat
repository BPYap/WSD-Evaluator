@echo off
set algorithm=%1
set dataset=%2
call python get_sensekey.py -a %algorithm% -d %dataset%
call java Scorer dataset\%dataset%\%dataset%.gold.key.txt evaluation_result\%dataset%\%algorithm%\%dataset%.predicted.key.txt

pause