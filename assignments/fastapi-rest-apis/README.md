# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a collection of books with FastAPI. Practice HTTP methods, request and response models, input validation, and appropriate status codes.

## 📝 Tasks

### 🛠️ List and Create Books

#### Descrição
Complete the `GET /books` and `POST /books` endpoints in `starter-code.py`. The API should store books in memory while it runs. Start the server with `uvicorn starter-code:app --reload` and use the interactive documentation at `/docs` to try the endpoints.

#### Requisitos
O programa concluído deve:

- Return all books as a JSON list from `GET /books` (an empty list when there are no books)
- Accept a book with a title, author, and publication year at `POST /books`
- Assign each new book a unique integer ID and return the created book with status code `201`


### 🛠️ Find a Book by ID

#### Descrição
Implement `GET /books/{book_id}` so a client can request one book using its ID. Handle requests for IDs that are not in the collection.

#### Requisitos
O programa concluído deve:

- Return the matching book as JSON when it exists
- Raise `HTTPException` with status code `404` when the ID is not found
- Verify both a valid ID and a missing ID using `/docs`


### 🛠️ Update and Delete Books

#### Descrição
Complete `PUT /books/{book_id}` and `DELETE /books/{book_id}`. Use the provided Pydantic model to validate book data, then test successful requests and invalid input in `/docs`.

#### Requisitos
O programa concluído deve:

- Replace a book's title, author, and year with `PUT`, returning the updated book
- Return status code `204` with no response body after a successful `DELETE`
- Return status code `404` when updating or deleting an unknown ID
- Reject an empty title or author and a year less than 1 with FastAPI's validation response
