from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

setup(
    name='V_MTEB',
    version='1.0.0',
    description='Vietnamese Massive Text Embedding Benchmark',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='nguyenducnhan.work@gmail.com',
    url='https://github.com/haisonle001/V-MTEB/tree/main',
    packages=find_packages(),
    install_requires=[
        'mteb[beir]',
    ],
)
