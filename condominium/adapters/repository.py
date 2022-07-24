from typing import Protocol

from sqlalchemy.orm import Session

from condominium.domain import Unity


class AbstractRepository(Protocol):
    def add(self, unity: Unity):
        pass

    def get(self, name: str) -> Unity:
        pass


class SqlRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, unity: Unity):
        self.session.add(unity)
        self.session.commit()

    def get(self, name: str) -> Unity:
        return self.session.query(Unity).filter_by(name=name).first()
