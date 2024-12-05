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

        # AI-ML
        ai_1 = request.POST.get('ai_1')
        ai_2 = request.POST.get('ai_2')
        ai_3 = request.POST.get('ai_3')
        ai_4 = request.POST.get('ai_4')
        ai_5 = request.POST.get('ai_5')
        ai_6 = request.POST.get('ai_6')

        # DATABASE
        db_1 = request.POST.get('db_1')
        db_2 = request.POST.get('db_2')
        db_3 = request.POST.get('db_3')
        db_4 = request.POST.get('db_4')
        db_5 = request.POST.get('db_5')
        db_6 = request.POST.get('db_6')
        db_7 = request.POST.get('db_7')
        db_8 = request.POST.get('db_8')
        db_9 = request.POST.get('db_9')
        db_10 = request.POST.get('db_10')
        db_11 = request.POST.get('db_11')

        # DATA-VISULIZATION
        dv_1 = request.POST.get('dv_1')
        dv_2 = request.POST.get('dv_2')
        dv_3 = request.POST.get('dv_3')
        dv_4 = request.POST.get('dv_4')
        dv_5 = request.POST.get('dv_5')

        # DEVOPS
        do_1 = request.POST.get('do_1')
        do_2 = request.POST.get('do_2')
        do_3 = request.POST.get('do_3')
        do_4 = request.POST.get('do_4')
        do_5 = request.POST.get('do_5')
        do_6 = request.POST.get('do_6')
        do_7 = request.POST.get('do_7')

        # BAS
        bas_1 = request.POST.get('bas_1')
        bas_2 = request.POST.get('bas_2')
        bas_3 = request.POST.get('bas_3')
        bas_4 = request.POST.get('bas_4')

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

        # AI-ML
        context['ai_1'] = ai_1
        context['ai_2'] = ai_2
        context['ai_3'] = ai_3
        context['ai_4'] = ai_4
        context['ai_5'] = ai_5
        context['ai_6'] = ai_6

        # DATABASE
        context['db_1'] = db_1
        context['db_2'] = db_2
        context['db_3'] = db_3
        context['db_4'] = db_4
        context['db_5'] = db_5
        context['db_6'] = db_6
        context['db_7'] = db_7
        context['db_8'] = db_8
        context['db_9'] = db_9
        context['db_10'] = db_10
        context['db_11'] = db_11

        # DATA-VISULISATION
        context['dv_1'] = dv_1
        context['dv_2'] = dv_2
        context['dv_3'] = dv_3
        context['dv_4'] = dv_4
        context['dv_5'] = dv_5

        # DEVOPS
        context['do_1'] = do_1
        context['do_2'] = do_2
        context['do_3'] = do_3
        context['do_4'] = do_4
        context['do_5'] = do_5
        context['do_6'] = do_6
        context['do_7'] = do_7

        # BAS
        context['bas_1'] = bas_1
        context['bas_2'] = bas_2
        context['bas_3'] = bas_3
        context['bas_4'] = bas_4

        # SOCIAL LINKS

        # Get the GitHub input
        github = request.POST.get('github')

        # Get the Dev.to input
        devto = request.POST.get('devto')

        # Get the Twitter input
        twitter = request.POST.get('twitter')

        # Get the LinkedIn input
        linkedin = request.POST.get('linkedin')

        # Get the StackOverflow input
        stackoverflow = request.POST.get('stackoverflow')

        # Get the CodeSandbox input
        codesandbox = request.POST.get('codesandbox')

        # Get the Kaggle input
        kaggle = request.POST.get('kaggle')

        # Get the Facebook input
        facebook = request.POST.get('facebook')

        # Get the Instagram input
        instagram = request.POST.get('instagram')

        # Get the Dribbble input
        dribbble = request.POST.get('dribbble')

        # Get the Behance input
        behance = request.POST.get('behance')

        # Get the Hashnode input
        hashnode = request.POST.get('hashnode')

        # Get the Medium input
        medium = request.POST.get('medium')

        # Get the YouTube input
        youtube = request.POST.get('youtube')

        # Get the CodeChef input
        codechef = request.POST.get('codechef')

        # Get the HackerRank input
        hackerrank = request.POST.get('hackerrank')

        # Get the Codeforces input
        codeforces = request.POST.get('codeforces')

        # Get the LeetCode input
        leetcode = request.POST.get('leetcode')

        # Get the HackerEarth input
        hackerearth = request.POST.get('hackerearth')

        # Get the GeeksforGeeks input
        geeksforgeeks = request.POST.get('geeksforgeeks')

        # Get the TopCoder input
        topcoder = request.POST.get('topcoder')

        # Get the Discord input
        discord = request.POST.get('discord')

        # Update the context dictionary with the form data
        context['github'] = github
        context['devto'] = devto
        context['twitter'] = twitter
        context['linkedin'] = linkedin
        context['stackoverflow'] = stackoverflow
        context['codesandbox'] = codesandbox
        context['kaggle'] = kaggle
        context['facebook'] = facebook
        context['instagram'] = instagram
        context['dribbble'] = dribbble
        context['behance'] = behance
        context['hashnode'] = hashnode
        context['medium'] = medium
        context['youtube'] = youtube
        context['codechef'] = codechef
        context['hackerrank'] = hackerrank
        context['codeforces'] = codeforces
        context['leetcode'] = leetcode
        context['hackerearth'] = hackerearth
        context['geeksforgeeks'] = geeksforgeeks
        context['topcoder'] = topcoder
        context['discord'] = discord

        # GITHUB SPECIALS


        special_1 = request.POST.get('special_1')
        special_2 = request.POST.get('special_2')
        special_3 = request.POST.get('special_3')
        special_4 = request.POST.get('special_4')
        special_5 = request.POST.get('special_5')

        context['special_1'] = special_1
        context['special_2'] = special_2
        context['special_3'] = special_3
        context['special_4'] = special_4
        context['special_5'] = special_5
    
    # Render the template with the context
    return render(request, 'user_profile/index.html', context)

