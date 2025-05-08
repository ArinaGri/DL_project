from setuptools import setup, find_packages

setup(
    name="bayes",
    version="0.1.0",
    author="Алина Чеснокова, Арина Гришаева",
    author_email="grishaevaarina2004@gmail.com",
    description="Байесовская нейронная модель для пространственно-временных данных",
    py_modules=["bayes"],  
    packages=[],
    install_requires=[
        "torch>=1.10.0",
        "numpy>=1.21.0",
        "python-dateutil>=2.8.2",  
        "pandas>=1.3.0",
        "pyro-ppl>=1.8.0",
    ],
    python_requires=">=3.8",
)