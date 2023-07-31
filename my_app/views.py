from django.shortcuts import render

# Create your views here.
def data_render(request):
    d = {'name': 'NAHID', 'age': 25, 'gender': 'FEMALE'}
    return render(request, 'data_render.html', context = d)

def if_condition(request):
    d2 = {'a': 100}
    return render(request, 'if_condition.html', context = d2)

def if_else(request):
    d3 = {'a': 100, 'b': 200}
    return render(request, 'if_else.html', context = d3)

def if_elif_else(request):
    d4 = {'a': 100, 'b': 200, 'c': 50}
    return render(request, 'if_elif_else.html', context = d4)

def nested_if(request):
    d5 = {'a': 50, 'b': 100, 'c': 500}
    return render(request, 'nested_if.html', context = d5)

def for_loop(request):
    d6 = {'name': 'NAHID', 'age': 25, 'gender': 'FEMALE', 'hobbies': ['Travel', 'Painting', 'Dance', 'Reading books']}
    return render(request, 'for_loop.html', context = d6)