# Streamlit + FastAPI App

This repository contains a **Streamlit** frontend and a **FastAPI** backend to create a seamless web application.

## Features
- 🚀 **FastAPI** for handling backend API requests
- 🎨 **Streamlit** for an interactive UI
- 🔄 **Asynchronous API calls** for better performance
- 🐳 **Docker support** for easy deployment

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip
- (Optional) Docker

### Clone the Repository
```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application

### Start the FastAPI Backend
```sh
uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

### Start the Streamlit Frontend
```sh
streamlit run frontend/app.py
```

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| POST | `/items` | Send input data |

## Docker Setup
Build and run the application using Docker:
```sh
docker-compose up --build
```

## Deployment
You can deploy the application using:
- **Heroku** (for Streamlit + FastAPI)
- **AWS/GCP/Azure** (via Docker)
- **Railway/Render** (for backend hosting)

## Contributing
Feel free to fork and contribute to this project. Pull requests are welcome!

## License
This project is licensed under the MIT License.
