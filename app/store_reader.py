from pathlib import Path
import re

from PIL import Image, ImageOps, ImageFilter
import pytesseract


TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

WEAPONS = [
    "CLASSIC", "SHORTY", "FRENZY", "GHOST", "SHERIFF",
    "STINGER", "SPECTRE", "BUCKY", "JUDGE",
    "BULLDOG", "GUARDIAN", "PHANTOM", "VANDAL",
    "MARSHAL", "OPERATOR", "ARES", "ODIN"
]


def crop_daily_offer_names(image_path: str) -> list[Path]:
    image = Image.open(image_path)
    width, height = image.size

    output_dir = Path("data/temp")
    output_dir.mkdir(parents=True, exist_ok=True)

    boxes = [
        (int(width * 0.05), int(height * 0.77), int(width * 0.27), int(height * 0.845)),
        (int(width * 0.28), int(height * 0.77), int(width * 0.49), int(height * 0.845)),
        (int(width * 0.49), int(height * 0.77), int(width * 0.70), int(height * 0.845)),
        (int(width * 0.70), int(height * 0.77), int(width * 0.93), int(height * 0.845)),
    ]

    cropped_paths = []
    for index, box in enumerate(boxes, start=1):
        crop = image.crop(box)
        output_path = output_dir / f"offer_{index}.png"
        crop.save(output_path)
        cropped_paths.append(output_path)

    return cropped_paths


def preprocess_for_ocr(image_path: Path) -> Image.Image:
    image = Image.open(image_path)

    image = ImageOps.grayscale(image)
    image = ImageOps.autocontrast(image)

    width, height = image.size
    image = image.resize((width * 3, height * 3))

    image = image.point(lambda p: 255 if p > 140 else 0)
    image = image.filter(ImageFilter.SHARPEN)

    return image


def clean_ocr_text(text: str) -> str:
    cleaned = text.strip().upper()
    cleaned = cleaned.replace("\n", " ")
    cleaned = " ".join(cleaned.split())
    cleaned = re.sub(r"[^A-Z0-9&' \-]", "", cleaned)
    return cleaned


def extract_text_from_offer(image_path: Path) -> str:
    processed = preprocess_for_ocr(image_path)
    text = pytesseract.image_to_string(processed, config="--psm 7")
    return clean_ocr_text(text)


def split_name_and_price(text: str) -> tuple[str, str]:
    match = re.search(r"(\d{3,5})$", text)

    if match:
        price = match.group(1)
        name = text[:match.start()].strip()
    else:
        price = "N/A"
        name = text

    return name, price


def fix_weapon_name(name: str) -> str:
    parts = name.split()
    
    if name == "IMPERIUM":
        return "IMPERIUM VANDAL"

    if not parts:
        return name

    last = parts[-1]

    # se já está correto → mantém
    if last in WEAPONS:
        return name

    # correções específicas (seguras)
    corrections = {
        "SORE": "PHANTOM",
        "PHAMTOM": "PHANTOM",
        "PHANTON": "PHANTOM",
        "SPECTER": "SPECTRE",
        "SPEC TRE": "SPECTRE",
        "SHERIF": "SHERIFF",
        "GH0ST": "GHOST",
    }

    if last in corrections:
        parts[-1] = corrections[last]
        return " ".join(parts)

    return name


def read_daily_offers(image_path: str) -> list[tuple[str, str]]:
    cropped_paths = crop_daily_offer_names(image_path)

    results = []
    for path in cropped_paths:
        text = extract_text_from_offer(path)
        name, price = split_name_and_price(text)
        name = fix_weapon_name(name)
        results.append((name, price))

    return results