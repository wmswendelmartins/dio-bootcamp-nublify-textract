import json
from pathlib import Path

import boto3
from botocore.exceptions import ClientError


BASE_DIR = Path(__file__).parent
IMAGE_PATH = BASE_DIR / "images" / "lista-material-escolar.jpeg"
CACHE_PATH = BASE_DIR / "response.json"


def detect_file_text(image_path: Path, output_cache: Path) -> DetectDocumentTextResponseTypeDef:
    client = boto3.client("textract")

    if not image_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {image_path}")

    with open(image_path, "rb") as f:
        document_bytes = f.read()

    try:
        response: DetectDocumentTextResponseTypeDef = client.detect_document_text(
            Document={"Bytes": document_bytes}
        )
        with open(output_cache, "w", encoding="utf-8") as f:
            json.dump(response, f, indent=2, default=str)
        return response
    except ClientError as e:
        print(f"Erro ao processar documento com Textract: {e}")
        raise


def get_lines() -> list[str]:
    # 1. Se o cache não existir, chama o Textract diretamente
    if not CACHE_PATH.exists():
        data = detect_file_text(IMAGE_PATH, CACHE_PATH)
    else:
        with open(CACHE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

    # 2. Extrai linhas com segurança
    blocks = data.get("Blocks", [])
    return [
        block["Text"]
        for block in blocks
        if block.get("BlockType") == "LINE" and "Text" in block
    ]


if __name__ == "__main__":
    for line in get_lines():
        print(line)