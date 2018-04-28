
:: 
:: 功能：将当前路径下的pdb拷贝（附加GUID信息）一份到指定路径
:: 前提：在cmd中可以运行dumpbin命令；exe/dll和pdb在相同路径，并且路径文件夹存在；路径有空格需要加""。
:: 输入参数：P1:文件名（带后缀） P2:保存pdb路径
:: 版本：v1.1
::

:: 例 StorePdb.bat a.exe ".\white space\"

@echo on

set "file=%~1"
set "dir=%~2"
set "filepdb=%~dpn1%.pdb"

echo 当前批处理路径：%~dp0

:: 获取GUID
for /f "tokens=2 delims=," %%i in ('dumpbin /HEADERS %file% ^| findstr /r /c:"RSDS.*{.*}"') do (set dim=%%~i)
:: 生成文件
copy %filepdb% "%dir%\"%date:~5,2%%date:~8,2%_%dim:~2,8%.pdb