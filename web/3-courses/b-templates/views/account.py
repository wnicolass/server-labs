from fastapi_chameleon import template
from fastapi import APIRouter

router = APIRouter()

@router.get('/account')
async def account():
    return {}

@router.get('/account/login')
async def login():
    return {}

@router.get('/account/register')
async def login():
    return {}