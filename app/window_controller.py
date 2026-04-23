from pywinauto import Application
import time


def connect_to_riot_client(timeout: int = 15):
    """
    Tenta encontrar e conectar na janela do Riot Client
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            app = Application(backend="uia").connect(title_re=".*Riot Client.*")
            window = app.window(title_re=".*Riot Client.*")
            return window
        except Exception:
            time.sleep(1)

    return None


def focus_window(window):
    """
    Traz a janela para frente
    """
    try:
        window.set_focus()
        window.restore()
    except Exception:
        pass