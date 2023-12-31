from fastapi import FastAPI
from routes import item, products, category

app = FastAPI()

app.include_router(item.router, prefix="/items", tags=["items"])
app.include_router(products.router, prefix="/product", tags=['products'])
app.include_router(category.router, prefix="/category", tags=['category'])




# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})

#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# ================================
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"

# app = FastAPI()

# @app.get("/models/{model_name}")
# async def get_model(model_name : ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCun's LeNet"}

#     return {"model_name": model_name, "message": "Have some resuduals"}

# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/users/me")
# async def read_user_me():
#     return{"user_id": "The current user"}


# @app.get("users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
