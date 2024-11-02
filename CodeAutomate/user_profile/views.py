from django.shortcuts import render

def index(request):
    # if request.method == 'POST':
    #     text_input = request.POST.get('text_input')
    #     context = {'text_input': text_input}
    # else:
    #     context = {}
    # return render(request, 'my_app/index.html', context)
    # text_input = None
    # icon_1 = None

    # if request.method == "POST":
    #     text_input = request.POST.get('text_input')
    #     icon_1 = request.POST.get('icon_1')

    # return render(request, 'my_app/index.html', {
    #     'text_input': text_input,
    #     'icon_1': icon_1,
    # })

    # Initialize context dictionary
    context = {}

    if request.method == 'POST':
        # Get the textarea input
        text_input = request.POST.get('text_input')

        # Get the value of the selected radio button
        icon_1 = request.POST.get('icon_1')

        # Update the context dictionary with the form data
        context['text_input'] = text_input
        context['icon_1'] = icon_1

    # Render the template with the context
    return render(request, 'user_profile/index.html', context)