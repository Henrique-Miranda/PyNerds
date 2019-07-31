from django.shortcuts import render
from .forms import NLetterForm

# Create your views here.
def home(request):
    aviso = ''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NLetterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = request.POST.get('your_email')
            return render(request, 'news.html', {'email': email})
        else:
            aviso = 'E-mail inválido, tente novamente.'
            form = NLetterForm()
            return render(request, 'base.html', {'aviso': aviso, 'form': form})
    else:
        form = NLetterForm()
        return render(request, 'base.html', {'aviso': aviso, 'form': form})
