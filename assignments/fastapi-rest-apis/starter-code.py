from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Book API Starter")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=0, le=2100)


books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt", "year": 1999},
    {"id": 2, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
]


@app.get("/books")
def get_books():
    """Return all books."""
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book by ID."""
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookCreate):
    """Create a new book and return it."""
    new_id = max((book["id"] for book in books), default=0) + 1
    new_book = {"id": new_id, **payload.model_dump()}
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, payload: BookCreate):
    """TODO: Students implement update logic."""
    raise HTTPException(status_code=400, detail="Not implemented yet")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    """TODO: Students implement delete logic."""
    raise HTTPException(status_code=400, detail="Not implemented yet")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
