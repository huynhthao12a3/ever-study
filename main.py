from src.main import EverStudy


if __name__ == "__main__":
    ever_study_app = EverStudy()
    try:
        ever_study_app.mainloop()
    except KeyboardInterrupt:
        ever_study_app.destroy()
