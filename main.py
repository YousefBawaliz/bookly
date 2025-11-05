from fastapi import FastAPI, Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/greet/{age}')
async def greet_name(name:str , age:int) -> dict:
     return {
            "message" : f"Hello {name}",
            "age" : f"{age}"
            }


@app.get('/greet-optional')
async def greet_name_optional(name: str | None = None) -> dict:
    if name is None:
        return {"message": "no name"}
    else:
        return {"message": f"{name}"}


class bookSchema(BaseModel):
    author:str
    title:str

@app.post('/create_book')
async def create_book(book: bookSchema):
    return {
        "title" : book.author,
        "author" : book.author
    }
    

@app.get('/get_headers', status_code=201)
async def get_headers(
    accept:str =Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host:str = Header(None)
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["content-type"] = content_type
    request_headers["User-agent"] = user_agent
    request_headers["host"] = host

    return request_headers