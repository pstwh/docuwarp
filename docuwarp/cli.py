import os
import argparse
from pathlib import Path

from PIL import Image
from docuwarp.unwarp import Unwarp


def get_args():
    parser = argparse.ArgumentParser(description="Process an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    parser.add_argument(
        "--model_path",
        type=str,
        help="Path to the onnx model",
        default=os.path.join(os.path.dirname(__file__), "artifacts", "uvdoc.onnx"),
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    image_path = Path(args.image_path)

    unwarp_filename = f"{image_path.stem}_unwarp{image_path.suffix}"
    new_path = image_path.parent / unwarp_filename

    image = Image.open(image_path).convert("RGB")
    output = Unwarp(model_path=args.model_path).inference(image=image)
    output.save(new_path)


if __name__ == "__main__":
    main()
