from fastapi import APIRouter, Path
from schemas.poll import Poll, Question, Answer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.poll import PollService, QuestionService, AnswerService

poll_router = APIRouter()

@poll_router.get('/polls', tags=['polls'], status_code = 200)
def get_polls():
    db = Session()
    result = PollService(db).get_polls()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.post('/polls', tags=['polls'])
def create_poll(poll: Poll):
    db = Session()
    PollService(db).create_poll(poll)
    return JSONResponse(status_code = 201, content = {"message" : "The poll was successfully registered"})

#QUESTIONS -------------------------------------------------

@poll_router.get('/question', tags=['question'])
def get_questions():
    db = Session()
    result = QuestionService(db).get_questions()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.get('/question/{poll_id}', tags=['question'])
def get_question_by_poll_id(poll_id: int):
    db = Session()
    result = QuestionService(db).get_questions_by_poll_id(poll_id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': "Questions not found"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.post('/question', tags=['question'])
def create_question(question: Question):
    db = Session()
    created_question = QuestionService(db).create_question(question)
    if created_question:
        return JSONResponse(status_code = 201, content = {"message" : 'The Question was successfully registered '})
    return JSONResponse(status_code = 201, content = {"message" : 'Question registration failed'})

#ANSWERS -------------------------------------------------

@poll_router.get('/answer', tags=['answer'])
def get_answers():
    db = Session()
    result = AnswerService(db).get_answers()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.get('/answer/{question_id}', tags=['answer'])
def get_answer_by_question_id(question_id: int):
    db = Session()
    result = AnswerService(db).get_answers_by_question_id(question_id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': "Answers not found"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.post('/answer', tags=['answer'])
def create_answer(answer: Answer):
    db = Session()
    created_answer = AnswerService(db).create_answer(answer)
    if created_answer:
        return JSONResponse(status_code = 201, content = {"message" : 'The Answer was successfully registered '})
    return JSONResponse(status_code = 201, content = {"message" : 'Answer registration failed'})
    