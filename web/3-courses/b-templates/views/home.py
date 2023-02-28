from fastapi_chameleon import template
from fastapi import APIRouter

router = APIRouter()

@router.get('/')
@template()
async def index(course1: str = 'N/D'):
    return {
        'course1': course1,
        'course2': 'Math',
        'course3': 'Biogenetics',
    }

@router.get('/about')
@template()
async def about():
    return {}