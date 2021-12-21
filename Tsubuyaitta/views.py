from django.shortcuts import render,redirect

from django.views import View
from .models import Question

class TsubuView(View):

    def get(self, request, *args, **kwargs):

        questions  = Question.objects.all()
        context = { "questions":questions }

        return render(request,"Tsubu/index.html",context)

    def post(self, request, *args, **kwargs):

        posted  = Question( comment = request.POST["comment"] )
        posted.save()

        return redirect("Tsubu:index")

index   = TsubuView.as_view()

def index(request):
    if request.method == 'POST':
        question = Question(id=request.POST['id'], content=request.POST['text'])
        question.save()
        return redirect()
