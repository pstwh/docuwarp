import os
import unittest
from glob import glob

import numpy as np
from PIL import Image, ImageChops

from docuwarp import Unwarp


class TestUnwarp(unittest.TestCase):
    def setUp(self):
        self.unwarp = Unwarp()

    def images_are_equal(self, img1, img2):
        if img1.size != img2.size or img1.mode != img2.mode:
            return False

        diff_pil = np.array(ImageChops.difference(img1, img2)).sum()
        diff_pil = diff_pil // (img1.size[0] * img1.size[1])
        
        return diff_pil < 10.0

    def test_unwarp(self):
        unwarp_examples_glob = os.path.join(
            os.path.dirname(__file__), "../examples/*_unwarp.jpg"
        )
        unwarp_examples = glob(unwarp_examples_glob)

        outputs = []
        for example in unwarp_examples:
            before_path = example.replace("_unwarp", "")
            after_path = example
            with open(before_path, "rb") as fb, open(after_path, "rb") as fa:
                before_image = Image.open(fb)
                after_image = Image.open(fa)

                before_unwarped = self.unwarp.inference(before_image)

                outputs.append(self.images_are_equal(before_unwarped, after_image))

        self.assertTrue(all(outputs))


if __name__ == "__main__":
    unittest.main()
