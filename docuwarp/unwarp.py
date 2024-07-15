import os
from typing import Tuple

import numpy as np
import onnxruntime as ort
from PIL import Image


class Unwarp:
    def __init__(
        self,
        model_path: str = os.path.join(
            os.path.dirname(__file__), "artifacts", "uvdoc.onnx"
        ),
        sess_options=ort.SessionOptions(),
        providers=["CPUExecutionProvider"],
        image_size: Tuple[int, int] = (488, 712),
        grid_size: Tuple[int, int] = (45, 31),
    ):
        self.image_size = image_size
        self.grid_size = grid_size
        self.session = ort.InferenceSession(
            model_path, sess_options=sess_options, providers=providers
        )
        self.bilinear_unwarping = ort.InferenceSession(
            os.path.join(
                os.path.dirname(__file__), "artifacts", "bilinear_unwarping.onnx"
            )
        )

    def prepare_input(
        self, image: Image.Image
    ) -> Tuple[np.ndarray, np.ndarray, Tuple[int, int]]:
        original_size = image.size
        image_array = np.array(image)

        resized_image = image.resize(self.image_size)
        resized_array = np.array(resized_image)

        normalized_original = image_array.transpose(2, 0, 1) / 255
        normalized_resized = resized_array.transpose(2, 0, 1) / 255

        return (
            np.expand_dims(normalized_resized, 0),
            np.expand_dims(normalized_original, 0),
            original_size,
        )

    def inference(self, image: Image.Image) -> Image.Image:
        resized_input, original_input, original_size = self.prepare_input(image)

        points, _ = self.session.run(None, {"input": resized_input.astype(np.float16)})

        unwarped = self.bilinear_unwarping.run(
            None,
            {
                "warped_img": original_input.astype(np.float32),
                "point_positions": points.astype(np.float32),
                "img_size": np.array(original_size),
            },
        )[0][0]

        unwarped_array = (unwarped.transpose(1, 2, 0) * 255).astype(np.uint8)

        return Image.fromarray(unwarped_array)
