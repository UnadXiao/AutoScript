:: 
:: ���ܣ��鿴·����exe/dll��GUID��Ϣ
:: ǰ�᣺��cmd�п�������dumpbin����
:: �汾��v1.1
::

@echo off

:: �������ݸ���ʵ����Ҫ�޸�
set "filestyle="exe dll""

echo ��ǰ������·����%~dp0
for /f %%i in ('dir /b ^| findstr %filestyle%') do (
for /f "tokens=2 delims=," %%j in ('dumpbin /HEADERS %%i ^| findstr /r /c:"RSDS.*{.*}"') do (
echo %%i%%j
)
)

set /p prompt=���س��˳�