import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from app.database.queries import delete_expired_files
from app import app


def init_bg_tasks():
    scheduler = BackgroundScheduler(daemon=True)
    scheduler.start()

    scheduler.add_job(
        _file_expiration_deleter,
        'interval',
        minutes=app.config["FILE_EXPIRATION_CHECK_INTERVAL"],
        id='file_expiration_deleter'
    )

    atexit.register(lambda: scheduler.shutdown(wait=False))


def _file_expiration_deleter():
    print("File expiration deleter task executes...")
    delete_expired_files()
