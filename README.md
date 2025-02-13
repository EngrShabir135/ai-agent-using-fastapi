# My Bot Project

This project consists of a chatbot application built with React for the frontend and FastAPI with SQLAlchemy for the backend. The chatbot interacts with users and stores message history in a PostgreSQL database.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Node.js](https://nodejs.org/) (for the frontend)
- [Python](https://www.python.org/) (for the backend)
- [PostgreSQL](https://www.postgresql.org/) (for the database)
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

## Setup Instructions

### Backend Setup

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required Python packages:**

   ```bash
   pip install fastapi[all] sqlalchemy psycopg2 python-dotenv langchain-openai
   ```

4. **Set up the PostgreSQL database:**

   - Create a new database in PostgreSQL (e.g., `postgres`).
   - Update the `DATABASE_URL` in `database.py` if necessary.

5. **Create a `.env` file in the backend directory:**

   ```plaintext
   Open_API_KEY="your_openai_api_key"
   ```

6. **Run the backend server:**

   ```bash
   uvicorn main:app --reload
   ```

   The backend will be running at `http://localhost:8000`.

### Frontend Setup

1. **Navigate to the frontend directory:**

   ```bash
   cd my-bot-frontend
   ```

2. **Install the required Node.js packages:**

   ```bash
   npm install
   ```

3. **Run the frontend application:**

   ```bash
   npm start
   ```

   The frontend will be running at `http://localhost:3000`.

## Usage

- Open your browser and navigate to `http://localhost:3000`.
- Enter your User ID and start chatting with the bot.

## API Endpoints

- **GET /history/{user_id}**: Fetches the message history for a specific user.
- **POST /chat/**: Sends a message to the bot and receives a response.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.