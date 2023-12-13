from django.shortcuts import render,HttpResponse
from openai import OpenAI
import openai
import os
from django.conf import settings

# Create your views here.


client = OpenAI()

def home(request): 
  return HttpResponse("<h1> prueba 1 de que esto funciona</h1>")



def chatbot(request):
  chatbot_response = None

  if request.method =='POST':
    user_input = request.POST.get('user_input')

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "eres el mejor guia turistico y donde es,un resumen de los atractivos turisticos y fechas para visitar "},
                {"role": "user", "content": user_input},
            ],
        )


    print(response)

    chatbot_response =response["choices"][0]["message"]["content"]
    return   render(request,'main.html',{"response":chatbot_response})
  
  return render(request, 'main.html', {"response": ""})

