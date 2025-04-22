# demo22

```sh
uv init -p 3.11.11 --name demo .
uv venv
source .venv/bin/activate
deactivate
uv add --index https://mirrors.aliyun.com/pypi/simple/ "fastapi[all]" "uvicorn[standard]" python-multipart

# 启动
uvicorn main:app --reload
# 文档
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```
