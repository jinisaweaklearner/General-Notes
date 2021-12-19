# Colab

```
pip install jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws
jupyter notebook   --NotebookApp.allow_origin='https://colab.research.google.com'   --port=8888   --NotebookApp.port_retries=0
```

local files/folders with colab
- https://research.google.com/colaboratory/local-runtimes.html
- https://medium.com/@thedatadetective/getting-local-with-google-colab-a4d69f373364
