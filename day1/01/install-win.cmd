@ECHO OFF

SETLOCAL
SET CONDA_ENV_NAME=mcneel22
SET CONDA_INSTALL_PATH=%UserProfile%\Miniconda3_Compas

IF not defined CONDA_BAT GOTO configure_conda_bat
GOTO detect_environment

:configure_conda_bat
SET CONDA_BAT=%CONDA_INSTALL_PATH%\condabin\conda.bat

IF NOT EXIST %CONDA_BAT% GOTO install_miniconda
GOTO detect_environment

:install_miniconda
curl -S -s https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o miniconda-installer.exe
IF %ERRORLEVEL% neq 0 GOTO miniconda_download_failed

ECHO Installing miniconda...
CALL miniconda-installer.exe /InstallationType=JustMe /RegisterPython=0 /S /D=%CONDA_INSTALL_PATH%
DEL miniconda-installer.exe
ECHO Installing miniconda...Done!

ECHO To permanently initialize conda for your shell type:
ECHO.
ECHO    %CONDA_INSTALL_PATH%\condabin\conda init

:detect_environment
ECHO Detecting virtual environment...
CALL %CONDA_BAT% run -n %CONDA_ENV_NAME% python --version >nul 2>&1
IF %ERRORLEVEL%==0 GOTO update_environment

:create_environment
ECHO Creating virtual environment...
CALL %CONDA_BAT% env create -n %CONDA_ENV_NAME% -f https://dfab.link/mcneel22.yml
ECHO Creating virtual environment...Done!
GOTO install_for_rhino

:update_environment
ECHO Updating virtual environment...
CALL %CONDA_BAT% env update -n %CONDA_ENV_NAME% -f https://dfab.link/mcneel22.yml
ECHO Updating virtual environment...Done!

:install_for_rhino
ECHO Installing COMPAS for Rhino...
CALL %CONDA_BAT% run -n %CONDA_ENV_NAME% python -m compas_rhino.install -v 7.0
IF %ERRORLEVEL%==0 GOTO install_for_rhino_done

ECHO Could not install for Rhino 7, will try Rhino 6...
:install_for_rhino_6
CALL %CONDA_BAT% run -n %CONDA_ENV_NAME% python -m compas_rhino.install -v 6.0

:install_for_rhino_done
ECHO Installing COMPAS for Rhino...Done!

:clone_repo
SET REPO_LOCATION=%UserProfile%/Documents/mcneel22
IF EXIST %REPO_LOCATION% GOTO pull_repo
CALL %CONDA_BAT% run -n %CONDA_ENV_NAME% git clone https://github.com/compas-Workshops/mcneel22.git %REPO_LOCATION%
GOTO completed

:pull_repo
CALL %CONDA_BAT% run -n %CONDA_ENV_NAME% git -C %REPO_LOCATION% pull

:completed
PAUSE
EXIT /B %errorlevel%

:miniconda_download_failed
ECHO Could not download miniconda. Exiting.
PAUSE
EXIT /B %errorlevel%
