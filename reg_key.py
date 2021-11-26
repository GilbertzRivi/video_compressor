import os, sys, winreg

python_exe = sys.executable

key_path = r"Directory\\Background\\shell\\VideoCompressor"

key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)

winreg.SetValue(key, '', winreg.REG_SZ, '&Compress Videos')

key1 = winreg.CreateKeyEx(key, r"command")
winreg.SetValue(key1, '', winreg.REG_SZ, python_exe + f' "'YOUR_PATH_TO_THIS_FILE'\\vidcomp_rc.py"',)
