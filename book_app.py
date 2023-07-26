from typing import List

from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    published_year: int


class BookUpdate(BaseModel):
    author: str
    published_year: int


book_db: List[Book] = []


@app.get("/", tags=["Ping"])
def ping():
    return {"message": "ok"}


@app.get("/books/", tags=["Books"])
def get_books():
    return book_db


@app.post("/books/", response_model=Book, tags=["Books"])
def create_book(book: Book):
    book_db.append(book)
    return book


@app.get("/books/{book_id}", response_model=Book, tags=["Books"])
def get_book(book_id: int) -> Book:
    if book_id < 0 or book_id >= len(book_db):
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book_db[book_id]


@app.put("/books/{book_id}", response_model=Book, tags=["Books"])
def update_book(book_id: int, book: BookUpdate):
    if book_id < 0 or book_id >= len(book_db):
        raise HTTPException(status_code=404, detail="Книга не найдена")
    book_db[book_id].author = book.author
    book_db[book_id].published_year = book.published_year
    return book_db[book_id]


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8001)

