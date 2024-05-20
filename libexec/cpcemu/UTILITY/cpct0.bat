@echo off




cls
echo CPCT0.BAT
echo อออออออ
echo Read CPC diskettes (DATA FORMAT, WITH VERIFY, SIDE 0 AND 1)

echo.
if %1.==. goto syntax

rem cls

echo Insert CPC data disk in drive B and press return.
pause > nul

echo Side A ...

cpctrans B: cpcpd%1a.dsk /f 0 /s 0 -v
if errorlovel 1 goto end

echo Side B ...

cpctrans B: cpcpd%1b.dsk /f 0 /s 1 -v

if errorlevel 1 goto end

goto end
rem goto copy

:syntax
echo Syntax:	cpct0 disknumber
echo Example: 	cpct0 01
goto end


:end
echo.
