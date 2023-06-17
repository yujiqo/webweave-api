from typing import Dict
from dotenv import dotenv_values


def read_env() -> Dict[str, str | None]:
    env = dotenv_values()

    return env

def setup_app(env: Dict[str, str | None]) -> None:
    pass
