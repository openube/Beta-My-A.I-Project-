import cx_Freeze
import  sys
import matplotlib
import os
base=None
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'
if sys.platform =="win32":
    base= "Win32GUI"
    
executables=[ cx_Freeze.Executable("Ai_interfce.py", base=base,icon="ai_6mX_icon.ico")]

cx_Freeze.setup(
    name="BasilClient",
    options={"build_exe":{"packages":["tkinter","matplotlib"], "include_files":["ai_6mX_icon.ico"]}},
    version="0.01",
    description="Virtual Assistant",
    executables=executables
    )