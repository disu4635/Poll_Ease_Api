from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Poll(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    questions = relationship("Question", back_populates="poll")

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True)
    poll_id = Column(Integer, ForeignKey('polls.id'))
    question_number = Column(Integer)
    text = Column(String)
    poll = relationship("Poll", back_populates="questions")
    answers = relationship("Answer", back_populates="question")

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.id'))
    answer_number = Column(Integer)
    answer_text = Column(String)
    votes = Column(Integer, default=0)
    question = relationship("Question", back_populates="answers")