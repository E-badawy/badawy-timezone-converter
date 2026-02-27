#!/usr/bin/env python
"""
Build script to create standalone exe with PyInstaller
Bundles Flask app + frontend files
"""
import os
import PyInstaller.__main__
from pathlib import Path

# Get paths
backend_dir = Path(__file__).parent / 'backend'
frontend_dir = Path(__file__).parent / 'frontend'
build_dir = Path(__file__).parent / 'dist'

print(f"Backend: {backend_dir}")
print(f"Frontend: {frontend_dir}")
print(f"Build dir: {build_dir}")

# PyInstaller arguments
args = [
    str(backend_dir / 'app.py'),  # Main script
    '--name=BadawyTimezoneConverter',  # App name
    '--onefile',  # Single exe file
    '--icon=NONE',  # No icon (optional)
    f'--distpath={build_dir}',  # Output directory
    f'--add-data={frontend_dir}/../frontend:frontend',  # Bundle frontend folder
    '--hidden-import=pytz',  # Hidden imports
    '--hidden-import=flask_cors',
    '--collect-all=flask',
    '--collect-all=pytz',
]

print("\nBuilding executable...")
print(f"Command: pyinstaller {' '.join(args)}\n")

# Run PyInstaller
PyInstaller.__main__.run(args)

print("\nBuild complete!")
print(f"Exe location: {build_dir / 'BadawyTimezoneConverter.exe'}")
