from django.shortcuts import render

def home(request):
    context = {"page_title": "Home", "is_home" : True}
    return render (request, "index.html", context) 

def wordc(request):
    if request.method == "POST":
        message = request.POST.get("message", "")
        words = message.split()
        words_count = len(words)
        context = {
            "message": message,
            "words_count": words_count,
            "page_title": "Word Counter"
        }
    else:
        # GET request, show empty form
        context = {
            "message": "",
            "words_count": None,
            "page_title": "Word Counter"
        }
    return render (request, "word_counter.html", context)

def wordfc(request):
    if request.method == "POST":
        message = request.POST.get("message")
        words = message.split(" ")
        words_counter = {}
        for word in words:
            if word in words_counter:
                frequency = words_counter[word]
                words_counter[word] = frequency +1
            else:
                words_counter[word] = 1
        context = {
            "message": message,
            "words_counted" : words_counter,
            "page_title": "Word Frequency Counter"
        }
    else:
        # GET request, show empty form
        context = {
            "message": "",
            "words_count": None,
            "page_title": "Word Frequency Counter"
        }
    return render (request, "wfcounter.html", context)

def about(request):
    context = {"page_title": "About"}
    return render(request, "about.html", context)
