from pathlib import Path
import subprocess


def find_riot_client() -> Path:
    return Path(r"C:\Games\Riot Games\Riot Client\RiotClientServices.exe")


def launch_riot_client(executable: Path) -> subprocess.Popen:
    return subprocess.Popen([str(executable)], shell=False)