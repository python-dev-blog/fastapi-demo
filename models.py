from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    students = relationship('Student', backref='group', lazy=True)

    def __repr__(self):
        return f"<Group {self.name}>"


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birth_date = Column(Date)
    male = Column(Boolean, nullable=False, default=True)
    group_id = Column(Integer, ForeignKey('group.id'))

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"
