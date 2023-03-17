
from datetime import date
from random import randrange
from typing import List
from data.models import Testimonial, Student
from common.common import (
    is_valid_email,
    find_in
)
from common.viewmodels import ViewModel
_students = []

def student_count() -> int:
    return 2315
#:

def create_account(
    name: str,
    email: str,
    password: str,
    birth_date: date
):
    student = Student(
        randrange(10_000, 100_000),
        name,
        email,
        hash_password(password),
        birth_date
    )
    _students.append(student)
    return student

def get_student_by_email(email: str) -> Student | None:
    if not is_valid_email(email):
        raise ValueError(f'Invalid email address: {email}')
    return (find_in(_students, lambda student: student.email == email))
#:

def get_current_student() -> Student | None:
    return (find_in(_students, lambda student: student.id == ViewModel().user_id))
#:

def authenticate_student_by_email(email: str, password: str) -> Student | None:
    if not is_valid_email(email):
        raise ValueError(f'Invalid email address: {email}')
    if student := get_student_by_email(email):
        if hash_password(password) == student.password:
            return student
    return None

def hash_password(password: str) -> str:
    return password + '-hashpw'

def get_testimonials(count: int) -> List[Testimonial]:
    return [
            Testimonial(
                user_id = 239,
                user_name = 'Saul Goodman',
                user_occupation = 'CEO & Founder',
                text = 'Quidem HUEHUEHUE odit voluptate, obcaecati, explicabo nobis corporis perspiciatis nihil doloremque eius omnis officia voluptates, facere saepe quas consequatur aliquam unde. Ab numquam reiciendis sequi.',
            ),
            Testimonial(
                user_id = 1001,
                user_name = 'Sara Wilson',
                user_occupation = 'Designer',
                text = 'Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.',
            ),
            Testimonial(
                user_id = 704,
                user_name = 'Jena Karlis',
                user_occupation = 'Store Owner',
                text = 'Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.',
            ),
            Testimonial(
                user_id = 1002,
                user_name = 'Matt Brandon',
                user_occupation = 'Freelancer',
                text = 'Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.',
            ),
            Testimonial(
                user_id = 1589,
                user_name = 'John Larson',
                user_occupation = 'Entrepreneur',
                text = 'Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.',
            ),
        ][:count]