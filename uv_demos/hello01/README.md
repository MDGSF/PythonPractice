# hello01

```sh
uv init --python 3.13 hello01
uv venv --python 3.13
uv python pin 3.13
uv add requests
uv sync
uv lock
uv export -o requirements.txt
uv pip install --index-url http://127.0.0.1:9000/simple/ --target="pydependency_hello" -r requirements.txt
uv pip install --index-url https://pypi.tuna.tsinghua.edu.cn/simple --target="pydependency_hello" -r requirements.txt
```
