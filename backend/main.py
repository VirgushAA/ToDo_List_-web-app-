from fastapi import FastAPI
from routes import notes


def main():

    app = FastAPI(title='ToDo List server')
    app.include_router(notes.router)

if __name__ == '__main__':
    main()
