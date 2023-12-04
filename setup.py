from pathlib import Path

from setuptools import find_packages, setup


THIS_DIR = Path(__file__).parent


def read_requirements(path_dir):
    with open(path_dir / 'requirements.txt') as file:
        lines = [ln.strip() for ln in file.readlines()]
    return lines


setup(
    name='toxic-classification',
    version='1.0.0',
    author='Igor Dronnikov',
    author_email='dronnikovigor@gmail.com',
    description='Toxic comment classification and interpretation',
    install_requires=read_requirements(THIS_DIR),
    long_description=(THIS_DIR / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
    ],
)
