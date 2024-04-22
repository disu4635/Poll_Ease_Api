from schemas.poll import Poll, Question, Answer
from models.poll import Poll as PollModel, Question as QuestionModel, Answer as AnswerModel

class PollService():

    def __init__(self, db) -> None:
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
    
class QuestionService():

    def __init__(self, db) -> None:
        self.db = db

    def get_questions(self):
        result = self.db.query(QuestionModel).all()
        return result
    
    def get_questions_by_poll_id(self, poll_id):
        result = self.db.query(QuestionModel).filter(QuestionModel.poll_id == poll_id).all()
        return result

    def create_question(self, question: Question):
        # Los ** al inicio extrae los atributos y los pasa como parametros
        poll = self.db.query(PollModel).filter(PollModel.id == question.poll_id).first()
        if poll: 
            new_question = QuestionModel(**question.model_dump())
            self.db.add(new_question)
            self.db.commit()
            return True
        return False

class AnswerService():

    def __init__(self, db) -> None:
        self.db = db

    def get_answers(self):
        result = self.db.query(AnswerModel).all()
        return result
    
    def get_answers_by_question_id(self, question_id):
        result = self.db.query(AnswerModel).filter(AnswerModel.question_id == question_id).all()
        return result

    def create_answer(self, answer: Answer):
        # Los ** al inicio extrae los atributos y los pasa como parametros
        question = self.db.query(QuestionModel).filter(QuestionModel.id == answer.question_id).first()
        if question: 
            new_answer = AnswerModel(**answer.model_dump())
            self.db.add(new_answer)
            self.db.commit()
            return True
        return False
    