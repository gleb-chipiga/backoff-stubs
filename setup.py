from pathlib import Path

from setuptools import setup

DIR = Path(__file__).parent

setup(
    name='backoff-stubs',
    author='Gleb Chipiga',
    version='1.10.0.post4',
    description='External type annotations for the backoff library',
    long_description=(DIR / 'README.rst').read_text('utf-8').strip(),
    long_description_content_type="text/x-rst",
    url='https://github.com/gleb-chipiga/backoff-stubs',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    license='MIT',
    keywords=['retry', 'backoff', 'decorators', 'stubs', 'mypy'],
    packages=['backoff-stubs'],
    package_data={'backoff-stubs': ['__init__.pyi']},
    python_requires='>=3.8'
)
