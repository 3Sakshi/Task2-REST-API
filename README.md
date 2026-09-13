## Task Management REST API
A simple REST API built using FastAPI for managing tasks.

## Features
- Create a new task
- Get all tasks
- Get a task by ID
- Update an existing task
- Delete a task
- Input validation using Pydantic
- Proper error handling
- Malformed JSON handling
- Automatic API documentation with Swagger UI
- Automated testing using pytest
- 100% test coverage for `main1.py`

## Technologies Used
- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- pytest-cov

## API Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{task_id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{task_id}` | Update a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

## Running the API
Start the server using:

```bash
uvicorn main1:app --host 127.0.0.1 --port 8000

Then open:
```bash
http://127.0.0.1:8000/docs
```
The /docs page provides interactive Swagger UI documentation.

## Running Tests
Run:
```bash
pytest -v
```

Test result:
```bash
11 passed
```

## Test Coverage
Run:
```bash
pytest --cov=main1 --cov-report=term-missing
```

Coverage result:
```bash
main1.py      44      0   100%
TOTAL         44      0   100%
```
An HTML coverage report can be generated using:
```bash
pytest --cov=main1 --cov-report=html
```

The coverage result is documented in `coverage-report.txt`. An HTML coverage report was also generated locally using pytest-cov.

## Testing
The test suite covers:
- Successful API requests
- Task creation
- Task retrieval
- Task update
- Task deletion
- Missing task errors (404)
- Missing required fields (422)
- Malformed JSON (422)

## Error Handling
The API returns appropriate HTTP status codes for invalid or unsuccessful requests.
Examples:
- 404 — Task not found
- 422 — Validation or malformed request error

## Project Structure
```bash
Task2_REST_API/
├── main1.py
├── test_main1.py
├── README.md
└── htmlcov/
```

## Author
Sakshi Tayade
