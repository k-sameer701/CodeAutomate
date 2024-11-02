from django.shortcuts import render

def index(request):
    

    # Initialize context dictionary
    context = {}

    if request.method == 'POST':
        # Get the firstName input
        firstName = request.POST.get('firstName')

        # Get the email input
        email = request.POST.get('email')

        # Get the website input
        website = request.POST.get('website')

        # Get the bio input
        bio = request.POST.get('bio')

        # Get the value of the selected radio button
        icon_1 = request.POST.get('icon_1')

        # Update the context dictionary with the form data
        context['firstName'] = firstName
        context['email'] = email
        context['website'] = website
        context['bio'] = bio
        context['icon_1'] = icon_1

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)