import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, nullable=False)
    command = Column(String(100), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.today)

    params = relationship('RequestParameter', back_populates='request')

    def __init__(self, chat_id, command, params):
        super().__init__(chat_id=chat_id, command=command)

        for param_key in params:
            self.params.append(RequestParameter(name=param_key, value=params[param_key]))


class RequestParameter(Base):
    __tablename__ = 'requests_parameters'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    value = Column(Text)
    request_id = Column(Integer, ForeignKey('requests.id', ondelete='CASCADE'), nullable=False)

    request = relationship('Request', back_populates='params')
