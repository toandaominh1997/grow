from .user import USERDB
from .tinyurl import TinyURLDB
def init_db():
    USERDB().fit()
    TinyURLDB().fit()
