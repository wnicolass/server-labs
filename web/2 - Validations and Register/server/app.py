from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import database as db
import models
import schemas as sch
from schemas import ErrorCode

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

@app.post('/register')
async def register(player: sch.PlayerRegister) -> sch.PlayerRegisterResult:
    tourn_id = player.tournament_id
    if tourn_id is None:
        error = ErrorCode.ERR_UNSPECIFIED_TOURNAMENT
        raise HTTPException(status_code = 400, detail=error.details())

    if tourn_id not in (1, 2, 3):
        error = ErrorCode.ERR_UNKNOWN_TOURNAMENT_ID
        raise HTTPException(status_code = 404, detail=error.details(tourn_id = tourn_id))

    return sch.PlayerRegisterResult(
        id = tourn_id,
        full_name = player.full_name,
        email = player.email,
    )

###################################
def main():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
  app.py [-c | -c -d] [-p PORT] [-h HOST_IP]

Options:
  -p PORT, --port=PORT                 Listen on this port [default: 8000]
  -c, --create-ddl                     Create datamodel in the database
  -d, --populate-db                    Populate the DB with dummy for testing purposes
  -h HOST_IP, --host=HOST_IP           Listen on this IP address [default: 127.0.0.1]
"""
    args = docopt(help_doc)
    create_ddl = args['--create-ddl']
    populate_db = args['--populate-db']
    if create_ddl:
        db.create_metadata()
        if populate_db:
            models.populate_db()
    
            
    uvicorn.run(
        'app:app', 
        port = int(args['--port']),
        host = args['--host'],
        reload = True,
    )

if __name__ == '__main__':
    main()


