from datetime import date
from fastapi import APIRouter, Request
from fastapi_chameleon import template
from common import base_viewmodel_with, is_valid_name, form_field_as_file, form_field_as_str

router = APIRouter()

MIN_DATE = date.fromisoformat('1920-01-01')

@router.get('/account')
async def index():
    return {

    }
#:

@router.get('/account/register')
@template()
async def register():
    return register_viewmodel()
#:

def register_viewmodel():
    return base_viewmodel_with({
        'name': '',
        'email': '',
        'password': '',
        'birth_date': '',
        'checked': False,
        'min_date': MIN_DATE,
        'max_date': date.today(),
    })
#:

@router.post('/account/register')
@template(template_file = 'account/register.pt')
async def register(request: Request):
    return post_register_viewmodel(request)
#:

async def post_register_viewmodel(request: Request):
    form_data = await request.form()
    name = form_field_as_str(form_data, 'name')
    email = form_field_as_str(form_data, 'name')

    if not is_valid_name(name):
        error, error_msg = True, 'Nome inválido!'
    else:
        error, error_msg = False, ''

    return base_viewmodel_with({
        'name': '',
        'email': '',
        'password': '',
        'checked': ''
    })
#:

@router.get('/account/login')                            # type: ignore
@template()
async def login():
    return base_viewmodel_with({
        'error': False,
        'error_msg': 'There was an error with your data. Please try again.'
    })
#:

