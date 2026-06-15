from pathlib import Path
from typing import List, Optional
from PIL import Image


class ImageConverter:
    def image_to_pdf(
        self,
        image_path: str,
        output_path: str,
        size: Optional[tuple[int, int]] = None,
    ) -> str:
        image_path = Path(image_path)
        output_path = Path(output_path)

        if not image_path.exists():
            raise FileNotFoundError(f"La imagen no existe: {image_path}")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        image = Image.open(image_path).convert("RGB")
        if size:
            image = image.resize(size, Image.LANCZOS)

        image.save(output_path, format="PDF")
        return str(output_path.resolve())

    def images_to_pdf(
        self,
        image_paths: List[str],
        output_path: str,
        size: Optional[tuple[int, int]] = None,
    ) -> str:
        if not image_paths:
            raise ValueError("La lista de imágenes no puede estar vacía")

        images = []
        for image_path in image_paths:
            image = Image.open(image_path).convert("RGB")
            if size:
                image = image.resize(size, Image.LANCZOS)
            images.append(image)

        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        images[0].save(output_path, save_all=True, append_images=images[1:])
        return str(output_path.resolve())
