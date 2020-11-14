from django.views.decorators.csrf import csrf_exempt
from ...models.todo import ToDo

@csrf_exempt
def create_todo(request):
    if request.method == "POST":
        form_data = request.POST