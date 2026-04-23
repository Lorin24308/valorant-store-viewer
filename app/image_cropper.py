from pathlib import Path
from PIL import Image


def crop_skin_images(image_path: str) -> list[Path]:
    image = Image.open(image_path)

    output_dir = Path("data/temp")
    output_dir.mkdir(parents=True, exist_ok=True)

    boxes = [
        (202, 966, 715, 1241),
        (725, 965, 1235, 1239),
        (1243, 966, 1755, 1238),
        (1762, 964, 2277, 1242),
    ]

    paths = []

    for i, box in enumerate(boxes, start=1):
        crop = image.crop(box)
        path = output_dir / f"skin_{i}.png"
        crop.save(path)
        paths.append(path)

    return paths