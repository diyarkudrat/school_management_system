from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

""" example found on Github from github.com/Abdoulrasheed """

def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    ''' Decorator for views that checks that the logged in user is a student, redirects to the log-in page if necessary. '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.student_access or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def lecturer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    ''' Decorator for views that checks that the logged in user is a teacher, redirects to the log-in page if necessary. '''

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.teacher_access or u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator