__all__ = (
    'base_viewmodel',
    'base_viewmodel_with',
    'is_valid_name',
    'form_field_as_str',
    'form_field_as_file'
)

from fastapi import UploadFile
from fastapi.datastructures import FormData

def base_viewmodel():
    return {
        'error': None,
        'error_msg': None,
        'user_id': None,
        'is_logged_in': False,
    }
#:

def base_viewmodel_with(update_data: dict) -> dict:
    vm = base_viewmodel()
    vm.update(update_data)
    return vm
#:

def form_field_as_str(form_data: FormData, field_name: str) -> str:
    field_value = form_data[field_name]
    if isinstance(field_value, str):
        return field_value
    raise TypeError(f'Form field {field_name} type is not str.')

def form_field_as_file(form_data: FormData, field_name: str) -> UploadFile:
    field_value = form_data[field_name]
    if isinstance(field_value, UploadFile):
        return field_value
    raise TypeError(f'Form field {field_name} type is UploadFile.')

def is_valid_name(name: str) -> bool:
    return all(part.isalphe() and len(part) > 2 for part in name.split())