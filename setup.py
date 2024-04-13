from setuptools import setup

setup(
    name="pytelegrambotapi_fixed",
    description="fixed version of pyTelegramBotApi",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="4.12.6",
    url="https://github.com/molokov-klim/pyTelegramBotAPI_fixed",
    license="MIT",
    py_modules=["telebot"],
    packages=["telebot"],
    install_requires=["pytest", "requests==2.31.0", "wheel==0.38.1", "aiohttp==3.9.0"],
    extras_require={"test": ["beautifulsoup4", "lxml", "requests"]},
    platforms="any",
    python_requires=">=3.8",
    classifiers=[
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
