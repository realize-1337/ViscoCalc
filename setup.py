import subprocess

PROJECTNAME = 'ViscoCalc'
VERSION = '1.0'
AUTHOR = 'David Maerker'

# Aktualisiere die Abhängigkeiten mit 'pip freeze'
print("Aktualisiere Abhängigkeiten mit 'pip freeze'...")
with open("requirements.txt", "w") as requirements_file:
    subprocess.check_call(["pip", "freeze"], stdout=requirements_file)

# Führe PyInstaller aus
print("Führe PyInstaller aus...")
cmd = [
    "pyinstaller",
    "--onefile",   # Eine einzelne ausführbare Datei erstellen
    # Hier können Sie weitere PyInstaller-Optionen hinzufügen
    # "--noconsole", 
    # "--windowed",
    "--name", f"{PROJECTNAME}_V{VERSION}",
    # "--icon", "your_icon.ico",
    # "--add-data", "path/to/additional/files:destination",
    # "--exclude-module", "pathlib",
    # "--hidden-import", "module_to_include",
    # "--upx-dir", "path/to/upx",
    # "--additional-hooks-dir", "path/to/hooks",
    # "--clean",
     "--distpath", "",
    "--specpath", "build/spec",
    # "--workpath", "work_directory",
    # "--log-level", "INFO",
    "Calculator.py"
]
try:
    subprocess.check_call(cmd)
except subprocess.CalledProcessError as e:
    raise SystemExit(e)