
from fastapi import FastAPI
from langserve import add_routes

from agent import agent

app = FastAPI(
    title="Coding Crew Agent",
    version="1.0"
)

add_routes(
    app,
    agent,
    path="/"
)
