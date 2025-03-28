from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="code-analyzer",
    version="0.1.0",
    author="Botir Bakhtiyarov",
    author_email="botirbakhtiyarovb@gmail.com",
    description="AI-powered code vulnerability scanner for GitHub repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BotirBakhtiyarov/code_analyzer",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
        'tqdm>=4.66.1',
        'python-dotenv>=1.0.0',
        'pygments>=2.17.2'
    ],
    entry_points={
        'console_scripts': [
            'code_analyzer=app:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    include_package_data=True,
)