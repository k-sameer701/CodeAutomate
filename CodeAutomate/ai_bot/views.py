import cohere
from django.shortcuts import render
from .forms import ChatForm
from django.conf import settings

def ai_bot(request):
    form = ChatForm()
    output = None

    if request.method == "POST":
        form = ChatForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["text"]
            co = cohere.Client(settings.COHERE_API_KEY)  # Use hidden API key

            response = co.chat(
                model="command-nightly",
                message=text
            )
            
            output = response.text  # Extract chat response

    return render(request, "ai_bot.html", {"form": form, "output": output})
