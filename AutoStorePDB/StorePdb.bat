
:: 
:: ���ܣ�����ǰ·���µ�pdb����������GUID��Ϣ��һ�ݵ�ָ��·��
:: ǰ�᣺��cmd�п�������dumpbin���exe/dll��pdb����ͬ·��������·���ļ��д��ڣ�·���пո���Ҫ��""��
:: ���������P1:�ļ���������׺�� P2:����pdb·��
:: �汾��v1.1
::

:: �� StorePdb.bat a.exe ".\white space\"

@echo on

set "file=%~1"
set "dir=%~2"
set "filepdb=%~dpn1%.pdb"

echo ��ǰ������·����%~dp0

:: ��ȡGUID
for /f "tokens=2 delims=," %%i in ('dumpbin /HEADERS %file% ^| findstr /r /c:"RSDS.*{.*}"') do (set dim=%%~i)
:: �����ļ�
copy %filepdb% "%dir%\"%date:~5,2%%date:~8,2%_%dim:~2,8%.pdb