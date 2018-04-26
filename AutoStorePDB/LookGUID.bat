:: 
:: 功能：查看路径下exe/dll的GUID信息
:: 前提：在cmd中可以运行dumpbin命令
:: 版本：v1.0
::

@echo off

:: 下面内容根据实际需要修改
set "dir=*.*"
set "tmpfile=.tmp"

echo 当前批处理全路径：%~dp0
if exist %tmpfile% del %tmpfile%

for %%i in (%dir%) do (
dumpbin /HEADERS %%i | findstr /r /c:"RSDS.*{.*}" > %tmpfile%
for /f "tokens=2 delims=," %%j in (%tmpfile%) do (
echo %%i%%~j
)
)

del %tmpfile%
set /p prompt=按回车退出