import time
from app.logger import setup_logger
from app.launcher import find_riot_client, launch_riot_client
from app.window_controller import connect_to_riot_client, focus_window
from app.riot_controller import click_valorant_icon, click_play_button
from app.valorant_window import connect_to_valorant, focus_valorant_window
from app.valorant_controller import click_store_button
from app.screenshot import take_store_screenshot
from app.store_reader import read_daily_offers
from app.telegram_sender import send_photo
from app.image_cropper import crop_skin_images


def main() -> None:
    logger = setup_logger()
    logger.info("Iniciando o projeto.")

    riot_client = find_riot_client()

    if not riot_client:
        logger.error("Riot Client não foi encontrado.")
        return

    logger.info(f"Riot Client encontrado em: {riot_client}")

    try:
        process = launch_riot_client(riot_client)
        logger.info(f"Riot Client iniciado. PID: {process.pid}")

        logger.info("Aguardando abertura da janela do Riot Client...")
        riot_window = connect_to_riot_client()

        if not riot_window:
            logger.error("Não foi possível encontrar a janela do Riot Client.")
            return

        logger.info("Janela do Riot Client encontrada com sucesso.")
        focus_window(riot_window)
        logger.info("Janela do Riot Client focada.")

        time.sleep(2)

        logger.info("Clicando no ícone do VALORANT...")
        click_valorant_icon()

        time.sleep(3)

        logger.info("Clicando no botão PLAY...")
        click_play_button()

        logger.info("Aguardando abertura da janela do VALORANT...")
        valorant_window = connect_to_valorant(timeout=90)

        if not valorant_window:
            logger.error("Não foi possível encontrar a janela do VALORANT.")
            return

        logger.info("Janela do VALORANT encontrada com sucesso.")
        focus_valorant_window(valorant_window)
        logger.info("Janela do VALORANT focada.")

        time.sleep(5)

        logger.info("Clicando no botão LOJA...")
        click_store_button()

        time.sleep(5)

        logger.info("Capturando screenshot da loja...")
        screenshot_path = take_store_screenshot()
        logger.info(f"Screenshot salva em: {screenshot_path}")

        # OCR
        logger.info("Lendo ofertas com OCR...")
        offers = read_daily_offers(str(screenshot_path))

        # RECORTE DAS IMAGENS
        skin_images = crop_skin_images(str(screenshot_path))

        # ENVIO PARA TELEGRAM (IMAGEM + TEXTO)
        for (name, price), image_path in zip(offers, skin_images):
            send_photo(str(image_path), f"{name} — {price} VP")

        logger.info("Ofertas enviadas para o Telegram com sucesso.")

        # Log no terminal
        for i, (name, price) in enumerate(offers, start=1):
            logger.info(f"{i}. {name} — {price} VP")

    except Exception as exc:
        logger.exception(f"Erro ao iniciar: {exc}")


if __name__ == "__main__":
    main()