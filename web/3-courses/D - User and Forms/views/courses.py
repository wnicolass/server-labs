from fastapi import APIRouter
from fastapi_chameleon import template
from services import course_service
from common import base_viewmodel_with

AVAILABLE_COURSES_COUNT = 5

router = APIRouter()

@router.get('/courses')                            # type: ignore
@template()
async def courses():
    return courses_viewmodel()
#:

def courses_viewmodel():
    return base_viewmodel_with({
        'available_courses': course_service.available_courses(AVAILABLE_COURSES_COUNT)
    })
#:

@router.get('/courses/{course_id}')                            # type: ignore
@template()
async def course_details():
    return base_viewmodel_with({
        'id': 8,
        'name': 'Microsoldadura de SMD',
        'description': 'Incidunt vero deserunt explicabo sequi perferendis. Sint, sed. Explicabo blanditiis, sunt nesciunt delectus aperiam amet dignissimos exercitationem consequuntur soluta modi dolores a placeat qui corrupti ducimus. Esse, suscipit illum natus distinctio, sint repellendus quod expedita eveniet facere consequatur quas optio corrupti ratione non veniam deleniti dolor? Repudiandae harum iste libero non reprehenderit hic distinctio maxime esse repellendus, tempora at cupiditate qui nulla numquam! Fugit, saepe.',
        'trainer_name': 'Roberta Alexandra',
        'price': 280,
        'available_seats': 40,
        'schedule': 'Segundas e Quintas, 17 às 20h',
    })
#: