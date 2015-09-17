# py-leveldb-windows
A Visual Studio project to build leveldb python wrapper

## Usage
1. Change the compile mode to Release X64.

2. Modify the python path in the settings.

3. Compile

4. Copy `./x64/Release/leveldb.pyd` to `YOUR_PYTHON_ROOT/Lib/site-packages`.

5. Run `python ./test-py-leveldb.py`. If everything is ok, you will get `hello world` response and a folder named `db`.
