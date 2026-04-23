from pathlib import Path
from app.store_reader import crop_daily_offer_names, extract_text_from_offer, read_daily_offers


def main() -> None:
    image_path = Path("data/screenshots/store.png")

    if not image_path.exists():
        print("Imagem não encontrada em data/screenshots/store.png")
        return

    print("Gerando recortes...\n")

    cropped_paths = crop_daily_offer_names(str(image_path))

    print("OCR bruto por recorte:\n")
    for i, path in enumerate(cropped_paths, start=1):
        text = extract_text_from_offer(path)
        print(f"{i}. {path.name}")
        print(f"   OCR bruto: {text}")
        print("-" * 50)

    print("\nResultado final:\n")
    offers = read_daily_offers(str(image_path))
    for i, (name, price) in enumerate(offers, start=1):
        print(f"{i}. {name} — {price} VP")


if __name__ == "__main__":
    main()