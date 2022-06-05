## pyside6_app

## 环境按照

```bash
# CONDA creates Python virtual environment
conda create -n pyside6 python=3.8
# Activate environment
conda activate pyside6

# Installation Library
pip install -r requirements.txt

# Pack
# It is packaged into many files. It is recommended to use it when it is very dependent
pyinstaller pyside6_app.spec

# Package into a separate exe. It is recommended to use small files
# One drawback is that it will first read into memory and decompress the dependency to the cache directory.
# If the application is large, it is recommended to package it into a folder
pyinstaller pyside6_app_exe.spec
```