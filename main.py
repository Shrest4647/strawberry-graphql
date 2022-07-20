from datetime import datetime
import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from typing import Any, List, Union


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


authors: List = [
    {}
]

my_arr: List = [{
    "task_name" : "Run dog1",
    "time": datetime.now(),
},
{
    "task_name" : "Run dog2",
    "time": datetime.now(),
},{
    "task_name" : "Run dog3",
    "time": datetime.now(),
},
]
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"

    @strawberry.field
    def allTasks(self)-> List:
        return my_arr.copy()
    
    @strawberry.field
    def taskById(self, index: int )-> dict:
        return my_arr[index]
    
    


schema = strawberry.Schema(Query)


graphql_app = GraphQLRouter(schema)


app.include_router(graphql_app, prefix="/graphql")