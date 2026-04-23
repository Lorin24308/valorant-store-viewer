from pathlib import Path
from app.image_cropper import crop_skin_images


def main() -> None:
    image_path = Path("data/screenshots/store.png")

    if not image_path.exists():
        print("Imagem não encontrada em data/screenshots/store.png")
        return

    cropped = crop_skin_images(str(image_path))

    print("Imagens geradas:")
    for path in cropped:
        print(path)


if __name__ == "__main__":
    main()