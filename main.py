from threading import Thread

from src.main import EverStudy


def start_tkinter_ever_study_app():
    global ever_study_app
    ever_study_app = EverStudy()
    try:
        ever_study_app.mainloop()
    except KeyboardInterrupt:
        ever_study_app.destroy()


if __name__ == "__main__":
    global ever_study_app
    ever_study_app = EverStudy()
    try:
        ever_study_app.mainloop()
    except KeyboardInterrupt:
        ever_study_app.destroy()
