from dotenv.main import load_dotenv
from application import init_app


app = init_app()

if __name__ == "__main__":
    app.run(load_dotenv=True)