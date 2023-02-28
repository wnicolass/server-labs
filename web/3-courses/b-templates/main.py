from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
from fastapi_chameleon import global_init, template
import uvicorn
from fastapi.staticfiles import StaticFiles

from views import (
    account, courses, home
)

app = FastAPI()

def main():
    config()
    start_uvicorn()

def start_uvicorn():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
  main.py [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT                 Listen on this port [default: 8000]
  -h HOST_IP, --host=HOST_IP           Listen on this IP address [default: 127.0.0.1]
  -r, --reload                         Reaload app
"""
    args = docopt(help_doc)

            
    uvicorn.run(
        'main:app', 
        port = int(args['--port']),
        host = args['--host'],
        reload = args['--reload'],
        reload_includes = ['*.pt']
    )

def config():
    config_templates()
    config_routes()

def config_templates():
    global_init('templates')

def config_routes():
    app.mount('/static', StaticFiles(directory='static'), name='static')
    for view in [home, courses, account]:
        app.include_router(view.router)

if __name__ == '__main__':
    main()
else:
    config()
