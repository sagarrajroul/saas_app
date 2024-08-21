from django.http import HttpResponse
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello, world!</h1>")
