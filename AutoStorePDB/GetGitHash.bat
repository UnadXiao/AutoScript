
:: 
:: 功能：获取git最新提交的hash值（8位），并写入文件。
:: 前提：在cmd中可以运行git命令；路径有空格需要加""。
:: 输入参数：P1:文件名（带后缀） P2:保存路径 P3: 附加信息
:: 版本：v1.0
::

:: 例 GetGitHash.bat a.h .\ Debug

@echo off

:: 可以修改下面这个文件名
set "file=%~1"
set "dir=%~2"
set "attach=%3"
set "tmpfile=.tmp"
set "date_str=%date:~5,2%%date:~8,2%"

echo 当前批处理路径：%~dp0
if exist %tmpfile% del %tmpfile%

:: 获取hash
for /f "delims=" %%i in ('git rev-parse HEAD') do (set githash=%%i)

::生成文件，根据不同需求定制
echo #ifndef VERSION_H > %tmpfile%
echo #define VERSION_H >> %tmpfile%
echo= >> %tmpfile%
set sp="
echo #define COMMIT_HASH %sp%CH%githash:~,8%-%attach%%sp% >> %tmpfile%
echo= >> %tmpfile%
echo #endif // VERSION_H >> %tmpfile%

copy %tmpfile% "%dir%\"%file%
del %tmpfile%