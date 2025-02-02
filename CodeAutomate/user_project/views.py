from django.shortcuts import render
from .forms import MultiStepForm

def user_project(request):
    context = {}

    if request.method == 'POST':
        github_UserId = request.POST.get('github_UserId')
        project_title = request.POST.get('project_title')
        userName = request.POST.get('userName')
        project_description = request.POST.get('project_description')
        app_icon_url = request.POST.get('app_icon_url')
        screenshots_url = request.POST.get('screenshots_url')
        paypal_id = request.POST.get('paypal_id')
        buy_me_coffee = request.POST.get('buy_me_coffee')
        # steps = request.POST.getlist('steps')  # Corrected name for list input
        usage_steps = request.POST.getlist('usage_steps[]')  # Get all Usage steps
        feature_steps = request.POST.getlist('feature_steps[]')  # Get all Feature steps
        contribution_steps = request.POST.getlist('contribution_steps[]')  # Get all Contribution steps
        installation_steps = request.POST.getlist('installation_steps[]')

        context['github_UserId'] = github_UserId
        context['project_title'] = project_title
        context['userName'] = userName
        context['project_description'] = project_description
        context['app_icon_url'] = app_icon_url
        context['screenshots_url'] = screenshots_url
        context['paypal_id'] = paypal_id
        context['buy_me_coffee'] = buy_me_coffee
        context['usage_steps'] = usage_steps
        context['feature_steps'] = feature_steps
        context['contribution_steps'] = contribution_steps
        context['installation_steps'] = installation_steps

        return render(request, 'user_project.html', context)  # Fixed passing context

    form = MultiStepForm()
    context['form'] = form  # Include the form in context
    return render(request, 'user_project.html', context)  # Fixed passing context
