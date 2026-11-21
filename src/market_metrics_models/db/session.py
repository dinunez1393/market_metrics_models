from collections.abc import Generator
from contextlib import contextmanager
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session


_engines: dict[str, Engine] = {}
_session_factories: dict[str, sessionmaker[Session]] = {}


def _get_session_factory(db_url: str) -> sessionmaker[Session]:
    """
    Helper function for client to pass the DB URL. Function creates a DB session maker.
    Args:
        db_url: The URL for the DB.

    Returns:
        The DB session maker.
    """
    if db_url not in _session_factories:
        connect_args = {"check_same_thread": False} if db_url.startswith("sqlite") else {}
        engine = create_engine(db_url, connect_args=connect_args)
        _engines[db_url] = engine
        _session_factories[db_url] = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    return _session_factories[db_url]


@contextmanager
def get_session(db_url: str) -> Generator[Session, None, None]:
    """
    DB connection session getter for client.
    Args:
        db_url: The URL for the DB.

    Returns:
        A DB connection session object.
    """
    factory = _get_session_factory(db_url)
    session: Session = factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
