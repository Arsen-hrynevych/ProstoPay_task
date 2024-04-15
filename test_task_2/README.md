## Installation

1. Install dependencies:
   ```
   poetry install
   ```
2. Rename `.env.example` to `.env`.
3. Inside the `.env` file, replace `DATABASE_URL=your_database_url_here` with your actual database URL.

## Folder Structure
- **db**: Contains database related files.
- **models**: Includes model classes for the application.
- **schemas**: Contains schema definitions.
- **tests**: Contains unit tests for the application.
- **user_service.py**: Main logic for the application.
- **utils.py**: Utilities for handling environment variables.

## Testing
Run tests:
   ```
   python3 -m pytest tests/user_service.py
   ```

Absolutely, here's a more human-friendly description:

## Implementation Explanation

I add to `UserService` class special methods `__aenter__` and `__aexit__` because:

- **Easy Management**: (`__aenter__`), (`__aexit__`). This makes it simple to handle database connections without worrying about opening and closing them manually.

- **Interaction**:  You can start your database work with a simple "async with" and let the `UserService` handle the rest behind the scenes.
