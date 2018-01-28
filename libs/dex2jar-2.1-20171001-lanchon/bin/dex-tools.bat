@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  dex-tools startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

@rem Add default JVM options here. You can also use JAVA_OPTS and DEX_TOOLS_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS=

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%..

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windowz variants

if not "%OS%" == "Windows_NT" goto win9xME_args
if "%@eval[2+2]" == "4" goto 4NT_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*
goto execute

:4NT_args
@rem Get arguments from the 4NT Shell from JP Software
set CMD_LINE_ARGS=%$

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\lib\dex-tools-2.1-20171001-lanchon.jar;%APP_HOME%\lib\dex-translator-2.1-20171001-lanchon.jar;%APP_HOME%\lib\d2j-smali-2.1-20171001-lanchon.jar;%APP_HOME%\lib\d2j-jasmin-2.1-20171001-lanchon.jar;%APP_HOME%\lib\dex-writer-2.1-20171001-lanchon.jar;%APP_HOME%\lib\d2j-base-cmd-2.1-20171001-lanchon.jar;%APP_HOME%\lib\dx-23.0.0.jar;%APP_HOME%\lib\dex-reader-2.1-20171001-lanchon.jar;%APP_HOME%\lib\dex-ir-2.1-20171001-lanchon.jar;%APP_HOME%\lib\asm-debug-all-5.0.3.jar;%APP_HOME%\lib\antlr4-4.5.jar;%APP_HOME%\lib\antlr4-runtime-4.5.jar;%APP_HOME%\lib\antlr-3.5.2.jar;%APP_HOME%\lib\antlr-runtime-3.5.2.jar;%APP_HOME%\lib\dex-reader-api-2.1-20171001-lanchon.jar;%APP_HOME%\lib\ST4-4.0.8.jar;%APP_HOME%\lib\org.abego.treelayout.core-1.0.1.jar

@rem Execute dex-tools
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %DEX_TOOLS_OPTS%  -classpath "%CLASSPATH%" com.googlecode.dex2jar.tools.BaseCmd %CMD_LINE_ARGS%

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable DEX_TOOLS_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%DEX_TOOLS_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega
