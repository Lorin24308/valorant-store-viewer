import requests

TOKEN = "COLOQUE_SEU_TOKEN_AQUI"
CHAT_ID = "COLOQUE_SEU_CHAT_ID_AQUI"


def send_message(text: str) -> None:
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    response = requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    print("Resposta Telegram:", response.text)


def send_photo(photo_path: str, caption: str = "") -> None:
    url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"

    try:
        with open(photo_path, "rb") as photo:
            response = requests.post(
                url,
                data={
                    "chat_id": CHAT_ID,
                    "caption": caption
                },
                files={
                    "photo": photo
                }
            )

        print("Resposta Telegram:", response.text)

    except Exception as e:
        print("Erro ao enviar imagem:", e)