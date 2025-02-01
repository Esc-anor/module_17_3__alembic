from fastapi import FastAPI
from routers import task, user

app = FastAPI()

app.include_router(task.router)
app.include_router(user.router)


@app.get('/')
def welcome():
    return {"message": "Welcome to Taskmanager"}

# cd app
# -m uvicorn main:app --reload
# alembic init app/migrations
# alembic revision --autogenerate -m "Initial migration"
