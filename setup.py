from setuptools import setup

setup(
    name="docuwarp",
    version="1.0.1",
    packages=["docuwarp"],
    include_package_data=True,
    url="https://github.com/psthw/docuwarp",
    keywords="document, unwarp, photo",
    package_data={"docuwarp": ["artifacts/*.onnx"]},
    python_requires=">=3.5, <4",
    install_requires=["onnxruntime==1.18.1", "pillow==10.4.0"],
    entry_points={
        "console_scripts": ["docuwarp=docuwarp.cli:main"],
    },
    description="Unwarp documents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
