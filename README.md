
# Docuwarp

Docuwarp is a Python library for unwarping documents. It uses for inference the model from the paper "UVDoc: Neural Grid-based Document Unwarping." For more information about the paper behind this model, you can read the paper [here](https://igl.ethz.ch/projects/uvdoc). The GitHub repository maintained by the author is available [here](https://github.com/tanguymagne/UVDoc/tree/main).


## Installation

To install Docuwarp, follow these steps:

For cpu

```bash
pip install "docuwarp[cpu]"
```

For cuda 11.X
```bash
pip install "docuwarp[gpu]"
```

For cuda 12.X
```bash
pip install "docuwarp[gpu]" --extra-index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/onnxruntime-cuda-12/pypi/simple/
```

## Usage

### Command Line Interface

You can use Docuwarp from the command line by providing an image file:

```bash
docuwarp examples/1.jpg
```

### Using in Code

You can also incorporate Docuwarp into your Python code as follows:

```python
from PIL import Image
from docuwarp.unwarp import Unwarp

unwarp = Unwarp()
image = Image.open('examples/1.jpg')
unwarped_image = unwarp.inference(image)
```

If you want to use CUDA:
```python
from PIL import Image
from docuwarp.unwarp import Unwarp

unwarp = Unwarp(providers=["CUDAExecutionProvider"])
image = Image.open('examples/1.jpg')
unwarped_image = unwarp.inference(image)
```

Check all execution providers [here](https://onnxruntime.ai/docs/execution-providers/).

### Example

<table>
    <thead>
        <tr>
            <td>original</td>
            <td>unwarp</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://raw.githubusercontent.com/pstwh/docuwarp/main/examples/1.jpg" width="256" /></td>
            <td><img src="https://raw.githubusercontent.com/pstwh/docuwarp/main/examples/1_unwarp.jpg" width="256" /></td>
        </tr>
        <tr>
            <td><img src="https://raw.githubusercontent.com/pstwh/docuwarp/main/examples/2.jpg" width="256" /></td>
            <td><img src="https://raw.githubusercontent.com/pstwh/docuwarp/main/examples/2_unwarp.jpg" width="256" /></td>
        </tr>
    </tbody>
</table>


## Citation

```
@inproceedings{UVDoc,
title={{UVDoc}: Neural Grid-based Document Unwarping},
author={Floor Verhoeven and Tanguy Magne and Olga Sorkine-Hornung},
booktitle = {SIGGRAPH ASIA, Technical Papers},
year = {2023},
url={https://doi.org/10.1145/3610548.3618174}
}
```