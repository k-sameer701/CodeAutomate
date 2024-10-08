from django.shortcuts import render

def index(request):
    # if request.method == 'POST':
    #     text_input = request.POST.get('text_input')
    #     context = {'text_input': text_input}
    # else:
    #     context = {}
    # return render(request, 'my_app/index.html', context)
    # text_input = None
    # fav_language = None

    # if request.method == "POST":
    #     text_input = request.POST.get('text_input')
    #     fav_language = request.POST.get('fav_language')

    # return render(request, 'my_app/index.html', {
    #     'text_input': text_input,
    #     'fav_language': fav_language,
    # })

    # Initialize context dictionary
    context = {}

    if request.method == 'POST':
        # Get the textarea input
        text_input = request.POST.get('text_input')

        # Get the value of the selected radio button
        fav_language = request.POST.get('fav_language')

        # Update the context dictionary with the form data
        context['text_input'] = text_input
        context['fav_language'] = fav_language

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)