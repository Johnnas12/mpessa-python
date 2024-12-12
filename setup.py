from setuptools import setup, find_packages

setup(
    name="mpessa-python",
    version="0.1.0",
    description="A Python SDK for Mpesa payments.",
    author="Yohanes Mesfin",
    author_email="yohanesmesfin3@gmail.com",
    url="https://github.com/yourusername/mpessa-python", 
    packages=find_packages(), 
    install_requires=[
        "httpx>=0.24.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
