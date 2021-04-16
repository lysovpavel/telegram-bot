from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from .views.command import create_command, get_commands, get_command_by_id, count_commands


def get_app():
    app = FastAPI()
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "http://localhost:8000",
        "http://localhost:3000"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

app = get_app()