from setuptools import setup, find_packages
import sys
import platform

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Dependencias específicas por plataforma
install_requires = [
    "pdf2image>=1.16.0",
    "Pillow>=9.0.0",
    "PyPDF2>=3.0.0",
]

setup(
    name="pdf-image-converter",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Librería Python para convertir PDF a Imagen e Imagen a PDF",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pdf-image-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Environment :: Console",
        "Topic :: Office/Business",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "twine>=3.4.1",
            "wheel>=0.37.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "pdf-converter=pdf_image_converter.cli:main",
        ]
    },
    include_package_data=True,
    package_data={
        'pdf_image_converter': ['*.png', '*.ico'],
    },
)
