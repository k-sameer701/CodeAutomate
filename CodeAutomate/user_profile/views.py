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

        # FRONTEND LANGUGAGE
        fe_1 = request.POST.get('fe_1')
        fe_2 = request.POST.get('fe_2')
        fe_3 = request.POST.get('fe_3')
        fe_4 = request.POST.get('fe_4')
        fe_5 = request.POST.get('fe_5')
        fe_6 = request.POST.get('fe_6')
        fe_7 = request.POST.get('fe_7')
        fe_8 = request.POST.get('fe_8')
        fe_9 = request.POST.get('fe_9')
        fe_10 = request.POST.get('fe_10')
        fe_11 = request.POST.get('fe_11')
        fe_12 = request.POST.get('fe_12')
        fe_13 = request.POST.get('fe_13')
        fe_14 = request.POST.get('fe_14')

        # BACKEND LANGUGAGE
        be_1 = request.POST.get('be_1')
        be_2 = request.POST.get('be_2')
        be_3 = request.POST.get('be_3')
        be_4 = request.POST.get('be_4')

        # MOBILE LANGUAGE
        mobile_1 = request.POST.get('mobile_1')
        mobile_2 = request.POST.get('mobile_2')
        mobile_3 = request.POST.get('mobile_3')
        mobile_4 = request.POST.get('mobile_4')

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
      
        # PROGRAMMING LANGUAGE 

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

        # FRONT-END
        context['fe_1'] = fe_1
        context['fe_2'] = fe_2
        context['fe_3'] = fe_3
        context['fe_4'] = fe_4
        context['fe_5'] = fe_5
        context['fe_6'] = fe_6
        context['fe_7'] = fe_7
        context['fe_8'] = fe_8
        context['fe_9'] = fe_9
        context['fe_10'] = fe_10
        context['fe_11'] = fe_11
        context['fe_12'] = fe_12
        context['fe_13'] = fe_13
        context['fe_14'] = fe_14
       
        # BACKEND LANGUAGE
        context['be_1'] = be_1
        context['be_2'] = be_2
        context['be_3'] = be_3
        context['be_4'] = be_4

        # MOBILE LANGUAGE
        context['mobile_1'] = mobile_1
        context['mobile_2'] = mobile_2
        context['mobile_3'] = mobile_3
        context['mobile_4'] = mobile_4

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)