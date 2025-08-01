from sqlalchemy.orm import DeclarativeBase


class BaseModel(DeclarativeBase):
    __abstract__ = True

    repr_cols_num = 5
    repr_cols = ()

    def __repr__(self) -> str:
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')

        return f'<{self.__class__.__name__} {", ".join(cols)}>'
