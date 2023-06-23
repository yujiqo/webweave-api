from dotenv import dotenv_values
from redis import Redis


environ = dotenv_values()


if not environ.get("HOST"):
    raise ValueError("Host is not specified!")

if not environ.get("PORT"):
    raise ValueError("Port is not specified!")


try:
    REDIS = {
        "host": str(environ.get("HOST")),
        "port": int(str(environ.get("PORT")))
    }
except ValueError as error:
    print(error)
    raise ValueError("Specified port is not a number")


connection = Redis(
    host=REDIS["host"],
    port=REDIS["port"],
    decode_responses=True
)
