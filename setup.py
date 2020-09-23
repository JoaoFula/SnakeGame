from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "pygame", "random", "tkinter", "shelve"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "Snake",
    options = options,
    version = "0.1",
    description = 'A clone of the snake game',
    executables = executables
)
