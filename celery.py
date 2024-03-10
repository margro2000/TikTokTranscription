import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Add imports that contain celery tasks here
# e.g. "api.celery.example_task"
TASKS = (
    "api.generate.course_generator",
    "commands.hydrate_module_from_title",
)

celery = Celery(
    __name__,
    broker=os.environ.get("REDIS_URL"),
    backend=os.environ.get("REDIS_URL"),
    config_source={
        "broker_connection_retry_on_startup": True,
        "imports": TASKS,
    },
)
