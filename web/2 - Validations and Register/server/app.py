from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session
from sqlalchemy import column

import database as db
import schemas as sch
import database_crud as crud
import models
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

def get_db_session():
    db_session = db.SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

@app.get("/tournaments")
async def get_tournaments(db_session: Session = Depends(get_db_session)) -> list:
    tournaments = db_session.query(column('id'), column('name')).select_from(models.Tournament)
    ordered_tournaments = tournaments.order_by(models.Tournament.id).all()
    
    if len(ordered_tournaments) == 0:
        error = ErrorCode.ERR_NO_TOURNAMENT_AVAILABLE
        raise HTTPException(status_code = 500, detail=error.details())

    return ordered_tournaments

@app.post('/tournaments', response_model= sch.TournamentRegisterResult)
async def register_tournament(
    tournament: sch.TournamentRegister, 
    db_session: Session = Depends(get_db_session)
) -> sch.TournamentRegisterResult:
    db_tournament = crud.get_tournament_by_name(db_session, tournament.name)
    if not db_tournament:
        db_tournament = crud.create_tournament(db_session, tournament)
    else:
        error = ErrorCode.ERR_TOURNAMENT_ALREADY_EXISTS
        raise HTTPException(status_code = 400, detail=error.details(tourn_name = db_tournament.name))

    return db_tournament

@app.post('/register', response_model = sch.PlayerRegisterResult)
async def register(
    player: sch.PlayerRegister, 
    db_session: Session = Depends(get_db_session)
) -> sch.PlayerRegisterResult:
    tourn_id = player.tournament_id
    if tourn_id is None:
        error = ErrorCode.ERR_UNSPECIFIED_TOURNAMENT
        raise HTTPException(status_code = 400, detail=error.details())

    db_player = crud.get_player_by_email(db_session, player.email)
    if not db_player:
        db_player = crud.create_player(db_session, player)

    tournament = crud.get_tournament_by_id(db_session, tourn_id)
    
    if tournament is None:
        error = ErrorCode.ERR_UNKNOWN_TOURNAMENT_ID
        raise HTTPException(status_code = 400, detail=error.details(tourn_id = tourn_id))
    
    for tourn in db_player.tournament:
        if tourn.id == tournament.id:
            error = ErrorCode.ERR_PLAYER_ALREADY_ENROLLED
            raise HTTPException(status_code = 400, detail=error.details(tourn_id = tourn_id))
    
    crud.update_player_tournament(db_session, db_player, tournament)

    return db_player

###################################
def main():
    import uvicorn
    from docopt import docopt

    help_doc = """
A Web accessible FastAPI server that allow players to register/enroll for tournaments.

Usage:
  app.py [-c | -c -d] [-p PORT] [-h HOST_IP] [-r]

Options:
  -p PORT, --port=PORT                 Listen on this port [default: 8000]
  -c, --create-ddl                     Create datamodel in the database
  -d, --populate-db                    Populate the DB with dummy for testing purposes
  -h HOST_IP, --host=HOST_IP           Listen on this IP address [default: 127.0.0.1]
  -r, --reload                         Reaload the application
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
        reload = args['--reload'],
    )

if __name__ == '__main__':
    main()


