from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['userText']
    reversed_text = user_text[::-1]
    count_words = len(user_text.split())
    return render(request, 'reverse.html', {'userText': user_text, 'reversedText':reversed_text, 'countWords' : count_words})