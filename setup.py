from setuptools import setup

setup(
    name="qcopy",
    version="0.1.0",
    py_modules=["qcopy"],
    install_requires=["Click", "pyperclip"],
    entry_points={
        "console_scripts": [
            "qcopy = qcopy:cli",
        ],
    },
)
