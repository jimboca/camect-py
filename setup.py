import setuptools

setuptools.setup(
    name="camect-py",
    version="0.2.0",
    author="Chao Liu",
    author_email="chao@camect.com",
    description="A client library to talk to Camect.",
    license="MIT License",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/camect/camect-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "websockets>=14.0",
    ],
    python_requires='>=3.6',
)
