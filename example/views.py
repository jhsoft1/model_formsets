from django.forms import modelformset_factory
from django.shortcuts import render

from example.models import Example


def index(request):
    ExampleFormSet = modelformset_factory(Example, fields=('name', 'location'), extra=4)
    if request.method == 'POST':
        form = ExampleFormSet(request.POST)
        instances = form.save()
    form = ExampleFormSet()  # queryset=Example.objects.all())
    return render(request, 'example/index.html', {'form': form})
