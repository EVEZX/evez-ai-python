from setuptools import setup

setup(
    name="evez-ai",
    version="1.0.0",
    description="EVEZ AI — Free AI API client, 49 models, $0/month",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="EVEZ",
    author_email="evez@evez.ai",
    url="https://github.com/EVEZX/evez-ai-python",
    py_modules=["evez_ai"],
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
