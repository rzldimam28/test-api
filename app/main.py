import sys
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
  """
  This is endpoint for Home Page
  """
  return {"message": "Hello World"}

@app.get("/tests")
def test():
  """
  This is endpoint for Test Page
  """
  return {"message": "Test"}

if __name__ == "__main__":
    if len(sys.argv) == 2:
        match sys.argv[1]:
            case "api":
                reload = True
                uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=reload)
            case _:
                print("Invalid argument")
                exit(1)