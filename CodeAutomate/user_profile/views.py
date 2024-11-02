from django.shortcuts import render

def index(request):
    

    # Initialize context dictionary
    context = {}

    if request.method == 'POST':
        # Get the fullName input
        fullName = request.POST.get('fullName')

        # Get the currentlyLearning input
        currentLearning = request.POST.get('currentLearning')

        # Get the askMe input
        askMe = request.POST.get('askMe')

        # Get the email input
        email = request.POST.get('email')

        # Get the website input
        website = request.POST.get('website')

        # Get the articles input
        articles = request.POST.get('articles')

        # Get the experience input
        experience = request.POST.get('experience')

        # Get the fullName input
        currentLearning = request.POST.get('currentLearning')

        # Get the fullName input
        currentLearning = request.POST.get('currentLearning')

        

        

        # Get the bio input
        bio = request.POST.get('bio')

        # PROGRAMMING LANGUGAGE
        lang_1 = request.POST.get('lang_1')
        lang_2 = request.POST.get('lang_2')

        # Get the value of the selected radio button
        icon_1 = request.POST.get('icon_1')

        # Update the context dictionary with the form data
        context['fullName'] = fullName
        context['currentLearning'] = currentLearning
        context['askMe'] = askMe
        context['email'] = email
        context['website'] = website
        context['articles'] = articles
        context['experience'] = experience
      


        
        
     
        context['lang_1'] = lang_1
        context['lang_2'] = lang_2
        context['icon_1'] = icon_1

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)