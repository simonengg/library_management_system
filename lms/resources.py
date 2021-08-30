from import_export import resources
from .models import AddBook


class AddBookResource(resources.ModelResource):
    class meta:
        model = AddBook
