from src.main import EverStudy

if __name__ == "__main__":
    app = EverStudy()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.destroy()


