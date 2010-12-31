@echo off
REM - Calls the Doxygen documentation generation with configuration file
if not exist docs mkdir docs
doxygen pyromannumeral.dox
