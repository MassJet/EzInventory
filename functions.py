import datetime, customtkinter as ctk


def item_save():
    pass


def submission_time():
    submission_timee = f'Submitted on {datetime.date.today().month}/{datetime.date.today().day}/{datetime.date.today().year} at {datetime.datetime.now().strftime("%H:%M:%S")}'
    return submission_timee
