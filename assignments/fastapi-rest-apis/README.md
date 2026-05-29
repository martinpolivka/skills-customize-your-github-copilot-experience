# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI by creating endpoints, validating request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Build a FastAPI application for managing a small in-memory list of books. Implement routes to list all books, get one book by ID, and create a new book.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return a single book
- Implement `POST /books` to add a new book with `title`, `author`, and `year`


### 🛠️	Add Validation and Error Handling

#### Description
Improve the API by adding input validation with Pydantic models and proper HTTP error responses for invalid data or missing records.

#### Requirements
Completed program should:

- Use a Pydantic model to validate `POST /books` request bodies
- Return `404` when a requested `book_id` does not exist
- Return `400` for invalid update requests (for example, empty fields)
- Add `PUT /books/{book_id}` and `DELETE /books/{book_id}` routes
