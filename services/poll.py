from schemas.poll import Poll, Question, Answer
from models.poll import Poll as PollModel, Question as QuestionModel, Answer as AnswerModel
from sqlalchemy.sql import exists
from sqlalchemy.orm import Session, joinedload


class PollService():

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_polls(self):
        result = self.db.query(PollModel).all()
        return result

    def create_poll(self, poll: Poll):
        # Los ** al inicio extrae los atributos y los pasa como parametros
        new_poll = PollModel(**poll.model_dump())
        self.db.add(new_poll)
        self.db.commit()
        return
    
    def update_poll(self, id: int, data: Poll):
        poll = self.db.query(PollModel).filter(PollModel.id == id).first()
        if not poll:
            return False
        poll.description = data.description
        poll.title = data.title
        self.db.commit()
        return True
    
    def delete_poll(self, id: int):
        poll = self.db.query(PollModel).options(joinedload(PollModel.questions).joinedload(QuestionModel.answers)).filter(PollModel.id == id).one_or_none()
        if not poll:
            return False 
        self.db.delete(poll)
        self.db.commit()
        return True
    
class QuestionService():

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_questions(self):
        result = self.db.query(QuestionModel).all()
        return result
    
    def get_questions_by_poll_id(self, poll_id):
        result = self.db.query(QuestionModel).filter(QuestionModel.poll_id == poll_id).all()
        return result

    def create_question(self, question: Question):
        # Los ** al inicio extrae los atributos y los pasa como parametros
        poll = self.db.query(exists().where(PollModel.id == question.poll_id)).scalar()
        if not poll:
            return None 
        new_question = QuestionModel(**question.model_dump())
        self.db.add(new_question)
        self.db.commit()
        return new_question
    
    def update_question(self, id: int, data: Question):
        question = self.db.query(QuestionModel).filter(QuestionModel.id == id).first()
        if not question:
            return False
        question.question_number = data.question_number
        question.text = data.text
        self.db.commit()
        return True
    
    def delete_question(self, id: int):
        question = self.db.query(QuestionModel).options(joinedload(QuestionModel.answers)).filter(QuestionModel.id == id).one_or_none()
        if not question:
            return False 
        self.db.delete(question)
        self.db.commit()
        return True

class AnswerService():
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_answers(self):
        result = self.db.query(AnswerModel).all()
        return result
    
    def get_answers_by_question_id(self, question_id):
        result = self.db.query(AnswerModel).filter(AnswerModel.question_id == question_id).all()
        return result

    def create_answer(self, answer: Answer):
        # Los ** al inicio extrae los atributos y los pasa como parametros
        question = self.db.query(exists().where(QuestionModel.id == answer.question_id)).scalar()
        if not question: 
            return None
        new_answer = AnswerModel(**answer.model_dump())
        self.db.add(new_answer)
        self.db.commit()
        return new_answer
    
    def delete_answer(self, id: int):
        answer = self.db.query(AnswerModel).filter(AnswerModel.id == id).first()
        if not answer:
            return False
        self.db.delete(answer)
        self.db.commit()
        return True
    
    def update_answer(self, id: int, data: Answer):
        answer = self.db.query(AnswerModel).filter(AnswerModel.id == id).first()
        if not answer:
            return False
        answer.answer_number = data.answer_number
        answer.answer_text = data.answer_text
        self.db.commit()
        return True
        
    