:: 
:: ���ܣ��鿴·����exe/dll��GUID��Ϣ
:: ǰ�᣺��cmd�п�������dumpbin����
:: �汾��v1.0
::

@echo off

:: �������ݸ���ʵ����Ҫ�޸�
set "dir=*.*"
set "tmpfile=.tmp"

echo ��ǰ������ȫ·����%~dp0
if exist %tmpfile% del %tmpfile%

for %%i in (%dir%) do (
dumpbin /HEADERS %%i | findstr /r /c:"RSDS.*{.*}" > %tmpfile%
for /f "tokens=2 delims=," %%j in (%tmpfile%) do (
echo %%i%%~j
)
)

del %tmpfile%
set /p prompt=���س��˳�