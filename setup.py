from setuptools import setup, find_packages

setup(
    name="evez-ai",
    version="1.0.0",
    description="Free AI API client — 35 models, OpenAI-compatible, $0/month",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="EVEZ",
    author_email="evez@evez.ai",
    url="https://github.com/EVEZX/evez-ai",
    packages=find_packages(),
    python_requires=">=3.7",
    keywords=["ai", "openai", "llm", "free", "evez"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
