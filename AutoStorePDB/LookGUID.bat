:: 
:: 功能：查看路径下exe/dll的GUID信息
:: 前提：在cmd中可以运行dumpbin命令
:: 版本：v1.1
::

@echo off

:: 下面内容根据实际需要修改
set "filestyle="exe dll""

echo 当前批处理路径：%~dp0
for /f %%i in ('dir /b ^| findstr %filestyle%') do (
for /f "tokens=2 delims=," %%j in ('dumpbin /HEADERS %%i ^| findstr /r /c:"RSDS.*{.*}"') do (
echo %%i%%j
)
)

set /p prompt=按回车退出