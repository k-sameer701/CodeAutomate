from django.shortcuts import render
from .forms import StepForm

def user_project(request):
    context = {}

    if request.method == 'POST':
        project_title = request.POST.get('project_title')
        steps = request.POST.getlist('steps')  # Corrected name for list input
        
        context['project_title'] = project_title
        context['steps'] = steps

        return render(request, 'user_project.html', context)  # Fixed passing context

    form = StepForm()
    context['form'] = form  # Include the form in context
    return render(request, 'user_project.html', context)  # Fixed passing context
