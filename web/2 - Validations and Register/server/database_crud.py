from sqlalchemy.orm import Session

import schemas
import models
import utils

def get_tournament_by_id(db_session: Session, tournament_id: int) -> models.Tournament | None:
    return db_session.query(models.Tournament).filter(
        models.Tournament.id == tournament_id
    ).first()

def get_player_by_email(db_session: Session, email: str) -> models.Player | None:
    return db_session.query(models.Player).filter(
        models.Player.email == email
    ).first()

def get_tournament_by_name(db_session: Session, name: str) -> models.Tournament | None:
    return db_session.query(models.Tournament).filter(
        models.Tournament.name == name
    ).first()

def get_player_by_id(db_session: Session, player_id: int) -> models.Player | None:
    return db_session.query(models.Player).filter(
        models.Player.id == player_id
    ).first()

def create_player(db_session: Session, player: schemas.PlayerBase) -> models.Player:
    fake_hashed_password = player.password + '-hashedpw'
    db_player = models.Player(
        full_name = player.full_name,
        email = player.email,
        hashed_password = fake_hashed_password,
        phone_number = player.phone_number,
        level = player.level,
    )
    db_session.add(db_player)
    db_session.commit()
    db_session.refresh(db_player) # to get auto increment id
    return db_player;

def create_tournament(db_session: Session, tournament: schemas.TournamentBase) -> models.Tournament:
    db_tournament = models.Tournament(
        name = tournament.name,
        start_date = utils.handle_date(tournament.start_date),
        end_date = utils.handle_date(tournament.end_date)
    )
    db_session.add(db_tournament)
    db_session.commit()
    db_session.refresh(db_tournament)
    return db_tournament

def update_player_tournament(
        db_session: Session,
        db_player: models.Player,
        tournament: models.Tournament
):
    db_player.tournament.append(tournament)
    db_session.commit()