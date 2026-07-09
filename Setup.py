import os
from cx_Freeze import setup, Executable

path = os.path.join(os.path.dirname(__file__), "asset")
asset_list = os.listdir(path)
asset_list_completa = [(os.path.join(path, asset), os.path.join("asset", asset)) for asset in asset_list]

executables = [Executable("main.py")]

setup(
    name="LixchiniShock",
    version="1.0",
    description="Lixchini Shock app",
    options={"build_exe": {"packages": ["pygame"], "include_files": asset_list_completa}},
    executables=executables
)