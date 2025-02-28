# hello

```sh
uv add requests
uv sync
uv lock
uv export -o requirements.txt
uv pip install --index-url http://127.0.0.1:9000/simple/ --target="pydependency_hello" -r requirements.txt
```
