@echo off

set SCRIPT_PATH=%~dp0
set BLENDER_EXE_PATH=C:\Program Files\Blender Foundation\Blender 3.2\blender.exe

"%BLENDER_EXE_PATH%" -b -P "%SCRIPT_PATH%fbxtowtf.py" %1


pause
REM This batch file expects the .fbx file to be passed as an argument when it is run. 
REM It then runs Blender in background mode (-b) and specifies a Python script (-P) to run. 
REM You will need to create a script.py file that contains the necessary code to import the .fbx file, convert it to the .wtf format, and save the resulting file.
