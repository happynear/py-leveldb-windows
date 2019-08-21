# py-leveldb-windows
A Visual Studio project to build leveldb python wrapper

## Pre-built Binaries

Python2.7 (64-bit): [Google Drive](https://drive.google.com/open?id=0B0OhXbSTAU1HcFBJUTNyczF6RjQ), [Baidu Yun](http://pan.baidu.com/s/1dE3FDHR)

Python3.6 (64-bit): [Google Drive](https://drive.google.com/open?id=0B0OhXbSTAU1HLWFpS0NjcmZFZm8), [Baidu Yun](http://pan.baidu.com/s/1jI3LE8e)

Put the `leveldb.pyd` in folder `YOUR_PYTHON_ROOT/Lib/site-packages`. 

Run `python ./test-py-leveldb.py`(python2) or `python ./test-py3-leveldb.py`(python3). If everything is ok, you will get `hello world` response and a folder named `db`.

## Usage
1. Change the compile mode to Release X64.

2. Modify the python path in the settings (Additional Include Directories, Additional Library Directories, Additional Dependencies).

3. Compile

4. Copy `./x64/Release/leveldb.pyd` to `YOUR_PYTHON_ROOT/Lib/site-packages`.

5. Run `python ./test-py-leveldb.py`. If everything is ok, you will get `hello world` response and a folder named `db`.

## Compile using Python3
1. Change the python path in the settings (Additional Include Directories, Additional Library Directories, Additional Dependencies).

2. Use this version of `leveldb.def` to replace `/win32_impl_src/leveldb.def`: https://github.com/happynear/py-leveldb-windows/blob/5fa0361a46ef0a75123ea785bdb15af1b2e64600/win32_impl_src/leveldb.def .
