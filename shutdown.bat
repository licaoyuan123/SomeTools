


echo Auther: Loveice
rem Description: 指定时间自动关机
title 指定时间自动关机
set /p shutdown_time = 输入关机时间，如23:00
at %shutdown_time% Shutdown -s
pause

