from celery import Celery
from celery.schedules import crontab

app = Celery('app', broker='redis://localhost:6379/0')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=10, minute=0),
        generate_and_upload_excel.s(),
    )
