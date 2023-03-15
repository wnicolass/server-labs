from fastapi import APIRouter
from fastapi_chameleon import template
from services import course_service
from common.viewmodels import ViewModel

AVAILABLE_COURSES_COUNT = 5

router = APIRouter()

@router.get('/courses')                            # type: ignore
@template()
async def courses():
    return courses_viewmodel()
#:

def courses_viewmodel():
    return ViewModel(
        available_courses = course_service.available_courses(AVAILABLE_COURSES_COUNT)
    )
#:

@router.get('/courses/{course_id}')
@template()
async def course_details(course_id: int):
    return course_details_viewmodel(course_id)

def course_details_viewmodel(course_id: int):
    if course := course_service.get_course_by_id(course_id):
        return ViewModel(
            course = course
        )
    return ViewModel(
        error = True,
        error_msg = 'Course not found'
    )
#: