from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routers.poll import poll_router
from config.database import engine, Base
from models.poll import Poll as ModelPoll, Question as Model_Question, Answer as Model_Answer

app = FastAPI()
app.title = "Vote_Api"
app.version = "0.0.1"

app.include_router(poll_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=["home"])
def home():
    return HTMLResponse('<h1>Welcome to the vote API!</h1>')