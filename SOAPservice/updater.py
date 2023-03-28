from apscheduler.schedulers.background import BackgroundScheduler
from .Curr_Update import update_currencies


def start():
    update_currencies()
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_currencies, 'interval', days=1)
    scheduler.start()