from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class CRUD:
    @classmethod
    def create(cls, session: Session, **kwargs):
        if 'birth_date' in kwargs and isinstance(kwargs['birth_date'], str):
            kwargs['birth_date'] = datetime.strptime(kwargs['birth_date'], '%Y-%m-%d').date()
        instance = cls(**kwargs)
        session.add(instance)
        session.commit()
        return instance
    
    @classmethod
    def get(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).first()
    
    @classmethod
    def get_all(cls, session: Session, **kwargs):
        return session.query(cls).filter_by(**kwargs).all()
    
    @classmethod
    def update(cls, session: Session, pk, **kwargs):
        instance = session.query(cls).filter_by(id=pk).first()
        for key, value in kwargs.items():
            setattr(instance, key, value)
        session.commit()
        return instance
    
    @classmethod
    def delete(cls, session: Session, pk, **kwargs):
        instance = session.query(cls).filter_by(id=pk).first()
        session.delete(instance)
        session.commit()