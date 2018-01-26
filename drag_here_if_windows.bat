@echo off
if exist C:\Python27\python.exe (
	start C:\Python27\python.exe showjar.py %1%
) else if exist C:\Python36\python.exe (
	start C:\Python36\python.exe showjar.py %1%
) else (
	start python showjar.py %1%
)