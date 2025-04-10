from setuptools import setup, find_packages

setup(
    name="quarto_book_builder",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0",
        "openai>=1.0.0",
        "requests>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "quarto-book-builder=quarto_book_builder.cli:cli",
        ],
    },
    python_requires=">=3.8",
    author="Quarto Book Builder Team",
    author_email="example@example.com",
    description="A CLI tool for building books with Quarto and AI-generated images",
    keywords="quarto, book, cli, openai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
