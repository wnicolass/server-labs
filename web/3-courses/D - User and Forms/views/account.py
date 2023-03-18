from datetime import date
from fastapi import APIRouter, Request, responses, status   
from fastapi_chameleon import template
from services import student_service
from common.common import (
    is_valid_name, 
    is_valid_email,
    is_valid_password,
    is_valid_iso_date
)
from common.viewmodels import ViewModel
from common.fastapi_utils import (
    form_field_as_str,
    form_field_as_file
)
from common.auth import set_auth_cookie, delete_auth_cookie, get_auth_from_cookie

router = APIRouter()

MIN_DATE = date.fromisoformat('1920-01-01')

@router.get('/account/register')
@template()
async def register():
    return register_viewmodel()
#:

def register_viewmodel():
    return ViewModel(
        name = '',
        email = '',
        password = '',
        birth_date = '',
        checked = False,
        min_date = MIN_DATE,
        max_date = date.today()
    )
    
#:

@router.post('/account/register', response_model = None)
@template(template_file = 'account/register.pt')
async def register(request: Request) -> dict | responses.Response:
    vm = await post_register_viewmodel(request)
    
    if vm['error']:
        return vm

    response = responses.RedirectResponse(url='/', status_code = status.HTTP_302_FOUND)
    set_auth_cookie(response, vm.new_student_id)
    return response
#:

async def post_register_viewmodel(request: Request):
    def is_valid_birth_date(birth_date: str) -> bool:
        return (is_valid_iso_date(birth_date) and date.fromisoformat(birth_date) >= MIN_DATE)

    form_data = await request.form()
    vm = ViewModel(
        name = form_field_as_str(form_data, 'name'),
        email = form_field_as_str(form_data, 'email'),
        password = form_field_as_str(form_data, 'password'),
        birth_date = form_field_as_str(form_data, 'birth_date'),
        new_student_id = None,
        min_date = MIN_DATE,
        max_date = date.today(),
        checked = False
    )

    if not is_valid_name(vm.name):
        vm.error, vm.error_msg = True, 'Nome inválido!'
    elif not is_valid_email(vm.email):
        vm.error, vm.error_msg = True, 'Email inválido!'
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Senha inválida!'
    elif not is_valid_birth_date(vm.birth_date):
        vm.error, vm.error_msg = True, 'Data inválida!'
    elif student_service.get_student_by_email(vm.email):
        vm.error, vm.error_msg = True, f'Endereço de email {vm.email} já existe'
    else:
        vm.error, vm.error_msg = False, ''

    if not vm.error:
        student = student_service.create_account(
            vm.name,
            vm.email,
            vm.password,
            date.fromisoformat(vm.birth_date)
        )
        vm.new_student_id = student.id
    return vm
#:

@router.get('/account/login')                            # type: ignore
@template()
async def login():
    return login_viewmodel()
#:

def login_viewmodel():
    return ViewModel(
        email = '',
        password = '',
    )

@router.post('/account/login')
@template(template_file = 'account/login.pt')
async def post_login(request: Request):
    vm = await post_login_viewmodel(request)

    if vm.error:
        return vm
    
    response = responses.RedirectResponse(url = '/', status_code = status.HTTP_302_FOUND)
    set_auth_cookie(response, vm.student_id)
    return response

async def post_login_viewmodel(request: Request) -> ViewModel:
    form_data = await request.form()
    vm = ViewModel(
        email = form_field_as_str(form_data, 'email'),
        password = form_field_as_str(form_data, 'password'),
        student_id = None,
    )

    if not is_valid_email(vm.email):
        vm.error, vm.error_msg = True, 'Invalid user or password!'
    elif not is_valid_password(vm.password):
        vm.error, vm.error_msg = True, 'Invalid password!'
    elif not (student := student_service.authenticate_student_by_email(vm.email, vm.password)):
        vm.error, vm.error_msg = True, 'User not found!'
    else:
        vm.error, vm.error_msg = False, ''
        vm.student_id = student.id

    return vm

@router.get('/account/logout')
async def logout():
    response = responses.RedirectResponse(url = '/', status_code = status.HTTP_302_FOUND)
    delete_auth_cookie(response)
    return response

@router.get('/account')
@template()
async def my_account() -> ViewModel:
    return my_account_viewmodel()
#:

def my_account_viewmodel() -> ViewModel:
    student = student_service.get_current_student()
    return ViewModel(
        name = student.name,
        email = student.email
    )
#:

@router.post('/account/update')
@template(template_file = 'account/my_account.pt')
async def update_user(request: Request) -> ViewModel:
    vm = await update_user_viewmodel(request)
    
    return vm

async def update_user_viewmodel(request: Request) -> ViewModel:
    form_data = await request.form()
    current_user = student_service.get_current_student()
    print(current_user)
    vm = ViewModel(
        id = current_user.id,
        name = current_user.name,
        email = form_field_as_str(form_data, 'email'),
        password = form_field_as_str(form_data, 'password'),
        new_password = form_field_as_str(form_data, 'new-password'),
        repeat_password = form_field_as_str(form_data, 'repeat-password')
    )

    if not student_service.hash_password(vm.password) == current_user.password:
        vm.error, vm.error_msg = True, 'Password inválida.'
    elif not is_valid_email(vm.email):
        vm.error, vm.error_msg = True, 'Email inválido.'
    elif vm.email != current_user.email or is_valid_password(vm.new_password):
        if not vm.new_password:
            student_service.update_student(vm, False)
        elif vm.new_password == vm.repeat_password:
            student_service.update_student(vm, True)
        else:
            vm.error, vm.error_msg = True, 'Senhas não correspondem.'
    else:
        vm.error, vm.error_msg = True, 'Nenhuma informação alterada.'
        
    return vm
