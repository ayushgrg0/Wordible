from django.shortcuts import render
from django.views.generic import View


def home(request):
    context = {"page_title": "Home", "home_page": True}
    return render(request, "index.html", context)


class WordCounter(View):
    def get(self, request):
        context = {
            "page_title": "Word Counter",
            "word_counter_page": True,
        }
        return render(request, "word_counter.html", context)

    def post(self, request):
        message = request.POST.get("message", "")
        words = message.split()
        words_count = len(words)
        context = {
            "message": message,
            "words_count": words_count,
            "page_title": "Word Counter",
            "word_counter_page": True,
        }
        return render(request, "word_counter.html", context)


class WordFrequencyCounter(View):
    def get(self, request):
        context = {
            "page_title": "Word Frequency Counter",
            "frequency_counter_page": True,
        }
        return render(request, "wfcounter.html", context)

    def post(self, request):
        message = request.POST.get("message")
        words = message.split(" ")
        words_counter = {}
        for word in words:
            if word in words_counter:
                frequency = words_counter[word]
                words_counter[word] = frequency + 1
            else:
                words_counter[word] = 1
        context = {
            "message": message,
            "words_counted": words_counter,
            "page_title": "Word Frequency Counter",
            "frequency_counter_page": True,
        }
        return render(request, "wfcounter.html", context)


class About(View):

    def get(self, request):
        context = {
            "page_title": "About",
            "about_page": True,
        }
        return render(request, "about.html", context)

    def post(self, request):
        context = {
            "page_title": "About",
            "about_page": True,
        }
        return render(request, "about.html", context)
