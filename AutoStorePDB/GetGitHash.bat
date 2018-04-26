
:: 
:: ���ܣ���ȡgit�����ύ��hashֵ��8λ������д���ļ���
:: ǰ�᣺��cmd�п�������git���·���пո���Ҫ��""��
:: ���������P1:�ļ���������׺�� P2:����·�� P3: ������Ϣ
:: �汾��v1.0
::

:: �� GetGitHash.bat a.h .\ Debug

@echo off

:: �����޸���������ļ���
set "file=%~1"
set "dir=%~2"
set "attach=%3"
set "tmpfile=.tmp"
set "date_str=%date:~5,2%%date:~8,2%"

echo ��ǰ������·����%~dp0
if exist %tmpfile% del %tmpfile%

:: ��ȡhash
for /f "delims=" %%i in ('git rev-parse HEAD') do (set githash=%%i)

::�����ļ������ݲ�ͬ������
echo #ifndef VERSION_H > %tmpfile%
echo #define VERSION_H >> %tmpfile%
echo= >> %tmpfile%
set sp="
echo #define COMMIT_HASH %sp%CH%githash:~,8%-%attach%%sp% >> %tmpfile%
echo= >> %tmpfile%
echo #endif // VERSION_H >> %tmpfile%

copy %tmpfile% "%dir%\"%file%
del %tmpfile%