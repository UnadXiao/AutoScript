
:: 
:: ���ܣ�����ǰ·���µ�pdb����������GUID��Ϣ��һ�ݵ�ָ��·��
:: ǰ�᣺��cmd�п�������dumpbin���exe/dll��pdb����ͬ·��������·���ļ��д��ڣ�·���пո���Ҫ��""��
:: ���������P1:�ļ���������׺�� P2:����pdb·��
:: �汾��v1.1
::

:: �� StorePdb.bat a.exe .\white space\

@echo on

set "file=%~1"
set "dir=%~2"
set "filepdb=%~dpn1%.pdb"
set "tmpfile=.tmp"

echo ��ǰ������·����%~dp0
if exist %tmpfile% del %tmpfile%

:: ��ȡGUID
dumpbin /HEADERS %file% | findstr /r /c:"RSDS.*{.*}" > %tmpfile%
for /f "tokens=2 delims=," %%i in (%tmpfile%) do (set dim=%%~i)
:: �����ļ�
copy %filepdb% "%dir%\"%date:~5,2%%date:~8,2%_%dim:~2,8%.pdb
del %tmpfile%