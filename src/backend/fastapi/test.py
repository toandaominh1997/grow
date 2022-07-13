import os
from dotenv import dotenv_values

config = {
    **dotenv_values("config/.env"),
    **dotenv_values("config/dev/.env"),
    **os.environ
}
print("config", config)
