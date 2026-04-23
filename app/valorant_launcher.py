from pathlib import Path
import subprocess


def launch_valorant() -> subprocess.Popen:
    path = Path(r"C:\Games\Riot Games\VALORANT\live\VALORANT.exe")

    return subprocess.Popen([str(path)], shell=False)