from fastapi import APIRouter, Path
from schemas.poll import Poll, Question, Answer
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from config.database import Session
from services.poll import PollService, QuestionService, AnswerService

poll_router = APIRouter()

#POLLS -------------------------------------------------

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

@poll_router.put('/polls/{id}', tags=['polls'])
def update_poll(id: int, poll: Poll):
    db = Session()
    updated_poll = PollService(db).update_poll(id, poll)
    if not updated_poll:
        return JSONResponse(status_code = 404, content = {"message" : "Poll not founded"})
    return JSONResponse(status_code = 201, content = {"message" : "The poll was successfully updated"})

@poll_router.delete('/polls/{id}', tags=['polls'])
def delete_poll(id: int):
    db = Session()
    deleted_poll = PollService(db).delete_poll(id)
    if not deleted_poll:
        return JSONResponse(status_code = 404, content = {"message" : "Poll not founded"})
    return JSONResponse(status_code = 201, content = {"message" : "The poll was successfully deleted"})

#QUESTIONS -------------------------------------------------

@poll_router.get('/questions', tags=['questions'])
def get_questions():
    db = Session()
    result = QuestionService(db).get_questions()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.get('/questions/{poll_id}', tags=['questions'])
def get_question_by_poll_id(poll_id: int):
    db = Session()
    result = QuestionService(db).get_questions_by_poll_id(poll_id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': "Questions not found"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.post('/questions', tags=['questions'])
def create_question(question: Question):
    db = Session()
    created_question = QuestionService(db).create_question(question)
    if not created_question:
        return JSONResponse(status_code = 201, content = {"message" : 'Question registration failed'})
    return JSONResponse(status_code = 201, content = {"message" : 'The Question was successfully registered '})

@poll_router.put('/questions/{id}', tags=['questions'])
def update_poll(id: int, question: Question):
    db = Session()
    updated_question = QuestionService(db).update_question(id, question)
    if not updated_question:
        return JSONResponse(status_code = 404, content = {"message" : "Question not founded"})
    return JSONResponse(status_code = 201, content = {"message" : "The Question was successfully updated"})

@poll_router.delete('/questions/{id}', tags=['questions'])
def delete_question(id: int):
    db = Session()
    deleted_question = QuestionService(db).delete_question(id)
    if not deleted_question:
        return JSONResponse(status_code = 404, content = {"message" : "Question not founded"})
    return JSONResponse(status_code = 201, content = {"message" : "The Question was successfully deleted"})

#ANSWERS -------------------------------------------------

@poll_router.get('/answers', tags=['answers'])
def get_answers():
    db = Session()
    result = AnswerService(db).get_answers()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.get('/answers/{question_id}', tags=['answers'])
def get_answer_by_question_id(question_id: int):
    db = Session()
    result = AnswerService(db).get_answers_by_question_id(question_id)
    if not result:
        return JSONResponse(status_code = 404, content = {'message': "Answers not found"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@poll_router.post('/answers', tags=['answers'])
def create_answer(answer: Answer):
    db = Session()
    created_answer = AnswerService(db).create_answer(answer)
    if created_answer:
        return JSONResponse(status_code = 201, content = {"message" : 'The Answer was successfully registered '})
    return JSONResponse(status_code = 201, content = {"message" : 'Answer registration failed'})

@poll_router.put('/answers/{id}', tags=['answers'])
def update_poll(id: int, answer: Answer):
    db = Session()
    updated_answer = AnswerService(db).update_answer(id, answer)
    if not updated_answer:
        return JSONResponse(status_code = 404, content = {"message" : "Answer not founded"})
    return JSONResponse(status_code = 201, content = {"message" : "The Answer was successfully updated"})

@poll_router.delete('/answers/{id}', tags=['answers'])
def delete_answer(id: int):
    db = Session()
    answer_deleted = AnswerService(db).delete_answer(id)
    if not answer_deleted:
        return JSONResponse(status_code = 404, content = {"message" : 'Answer not found'})
    return JSONResponse(status_code = 201, content = {"message" : 'The Answer was successfully deleted'})
    