@echo off
Title Personal Clock
@mode con cols=40 lines=12
color 03
: main
cls
echo.
echo Time: %time%
echo.
echo Date: %date%
echo.
ping -n 2 0.0.0.0>null
goto main
