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
        lang_3 = request.POST.get('lang_3')
        lang_4 = request.POST.get('lang_4')
        lang_5 = request.POST.get('lang_5')
        lang_6 = request.POST.get('lang_6')
        lang_7 = request.POST.get('lang_7')
        lang_8 = request.POST.get('lang_8')
        lang_9 = request.POST.get('lang_9')
        lang_10 = request.POST.get('lang_10')
        lang_11 = request.POST.get('lang_11')
        lang_12 = request.POST.get('lang_12')
        lang_13 = request.POST.get('lang_13')
        lang_14 = request.POST.get('lang_14')
        lang_15 = request.POST.get('lang_15')
        lang_16 = request.POST.get('lang_16')

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
        context['lang_3'] = lang_3
        context['lang_4'] = lang_4
        context['lang_5'] = lang_5
        context['lang_6'] = lang_6
        context['lang_7'] = lang_7
        context['lang_8'] = lang_8
        context['lang_9'] = lang_9
        context['lang_10'] = lang_10
        context['lang_11'] = lang_11
        context['lang_12'] = lang_12
        context['lang_13'] = lang_13
        context['lang_14'] = lang_14
        context['lang_15'] = lang_15
        context['lang_16'] = lang_16
        context['icon_1'] = icon_1

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)