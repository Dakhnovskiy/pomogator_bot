from bot.model import Base
from bot.db_helpers import get_engine

if __name__ == '__main__':
    Base.metadata.create_all(get_engine())
