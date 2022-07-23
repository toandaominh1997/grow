import os
from dotenv import dotenv_values

def load_env():
    config = dotenv_values("config/env")
    if config['dev']:
        config = {
            **os.environ,
            **config,
            **dotenv_values("config/dev/env"),
        }
    else:
        config = {
            **os.environ,
            **config,
            **dotenv_values("config/prod/env"),
        }
    return config

config = load_env()
