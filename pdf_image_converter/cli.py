import argparse
import sys
from pathlib import Path
from .image_converter import ImageConverter
from .pdf_converter import PDFConverter


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf-converter",
        description="Convierte PDF a imagen y viceversa.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    pdf_to_images = subparsers.add_parser(
        "pdf-to-images",
        help="Convertir PDF a múltiples imágenes",
    )
    pdf_to_images.add_argument("pdf_file", help="Archivo PDF de entrada")
    pdf_to_images.add_argument("--output", required=True, help="Directorio de salida")
    pdf_to_images.add_argument("--format", default="png", choices=["png", "jpg", "bmp", "tiff"], help="Formato de imagen")
    pdf_to_images.add_argument("--dpi", type=int, default=150, help="DPI de salida")
    pdf_to_images.add_argument("--pages", nargs="+", type=int, help="Páginas específicas a convertir")

    page_to_image = subparsers.add_parser(
        "page-to-image",
        help="Convertir una sola página de PDF a imagen",
    )
    page_to_image.add_argument("pdf_file", help="Archivo PDF de entrada")
    page_to_image.add_argument("page_number", type=int, help="Número de página")
    page_to_image.add_argument("output", help="Archivo de salida")
    page_to_image.add_argument("--format", default="png", choices=["png", "jpg", "bmp", "tiff"], help="Formato de imagen")
    page_to_image.add_argument("--dpi", type=int, default=150, help="DPI de salida")

    images_to_pdf = subparsers.add_parser(
        "images-to-pdf",
        help="Convertir múltiples imágenes a un solo PDF",
    )
    images_to_pdf.add_argument("images", nargs="+", help="Archivos de imagen de entrada")
    images_to_pdf.add_argument("--output", required=True, help="Archivo PDF de salida")
    images_to_pdf.add_argument("--width", type=int, help="Ancho en píxeles")
    images_to_pdf.add_argument("--height", type=int, help="Alto en píxeles")

    image_to_pdf = subparsers.add_parser(
        "image-to-pdf",
        help="Convertir una sola imagen a PDF",
    )
    image_to_pdf.add_argument("image", help="Archivo de imagen de entrada")
    image_to_pdf.add_argument("output", help="Archivo PDF de salida")
    image_to_pdf.add_argument("--width", type=int, help="Ancho en píxeles")
    image_to_pdf.add_argument("--height", type=int, help="Alto en píxeles")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "pdf-to-images":
            pdf = PDFConverter(args.pdf_file)
            pages = args.pages if args.pages else None
            result = pdf.to_images(args.output, fmt=args.format, dpi=args.dpi, pages=pages)
            print("Archivos generados:")
            for path in result:
                print(path)

        elif args.command == "page-to-image":
            pdf = PDFConverter(args.pdf_file)
            output_path = pdf.page_to_image(
                args.page_number,
                args.output,
                dpi=args.dpi,
                fmt=args.format,
            )
            print(output_path)

        elif args.command == "images-to-pdf":
            converter = ImageConverter()
            size = (args.width, args.height) if args.width and args.height else None
            output_path = converter.images_to_pdf(args.images, args.output, size=size)
            print(output_path)

        elif args.command == "image-to-pdf":
            converter = ImageConverter()
            size = (args.width, args.height) if args.width and args.height else None
            output_path = converter.image_to_pdf(args.image, args.output, size=size)
            print(output_path)

        return 0
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
