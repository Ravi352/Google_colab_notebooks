{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyNuc+Il0Yqa/9OXJPwPXw6e"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":3,"metadata":{"id":"u5aBIt2jCxAm","executionInfo":{"status":"ok","timestamp":1673528072250,"user_tz":-330,"elapsed":626,"user":{"displayName":"Ravi Kumar","userId":"12176873388585538917"}}},"outputs":[],"source":["from typing import Union\n","\n","from fastapi import FastAPI\n","\n","app = FastAPI()\n","\n","\n","@app.get(\"/\")\n","def read_root():\n","    return {\"Hello\": \"World\"}\n","\n","\n","@app.get(\"/items/{item_id}\")\n","def read_item(item_id: int, q: Union[str, None] = None):\n","    return {\"item_id\": item_id, \"q\": q}"]},{"cell_type":"code","source":["!pip install fastapi"],"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"zO-8StoEC3yI","executionInfo":{"status":"ok","timestamp":1673528068244,"user_tz":-330,"elapsed":5263,"user":{"displayName":"Ravi Kumar","userId":"12176873388585538917"}},"outputId":"f48c2d1c-a257-4883-b61a-eb916f6a6100"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n","Collecting fastapi\n","  Downloading fastapi-0.89.1-py3-none-any.whl (55 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m55.8/55.8 KB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hRequirement already satisfied: pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2 in /usr/local/lib/python3.8/dist-packages (from fastapi) (1.10.4)\n","Collecting starlette==0.22.0\n","  Downloading starlette-0.22.0-py3-none-any.whl (64 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m64.3/64.3 KB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hCollecting anyio<5,>=3.4.0\n","  Downloading anyio-3.6.2-py3-none-any.whl (80 kB)\n","\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m80.6/80.6 KB\u001b[0m \u001b[31m11.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n","\u001b[?25hRequirement already satisfied: typing-extensions>=3.10.0 in /usr/local/lib/python3.8/dist-packages (from starlette==0.22.0->fastapi) (4.4.0)\n","Collecting sniffio>=1.1\n","  Downloading sniffio-1.3.0-py3-none-any.whl (10 kB)\n","Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.8/dist-packages (from anyio<5,>=3.4.0->starlette==0.22.0->fastapi) (2.10)\n","Installing collected packages: sniffio, anyio, starlette, fastapi\n","Successfully installed anyio-3.6.2 fastapi-0.89.1 sniffio-1.3.0 starlette-0.22.0\n"]}]}]}