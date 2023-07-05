import os, sys, winreg

python_exe = sys.executable

key_path = r"Directory\\Background\\shell\\VideoCompressor8M"

key = winreg.CreateKeyEx(winreg.HKEY_CLASSES_ROOT, key_path)

winreg.SetValue(key, '', winreg.REG_SZ, '&Compress Videos 8MB')

key1 = winreg.CreateKeyEx(key, r"command")
winreg.SetValue(key1, '', winreg.REG_SZ, python_exe + f' "C:\\PATH\\vidcomp_rc_dc.py"',)
