from django.shortcuts import render

def vetor(request):
    return render(request, 'vetor.html')


def ordena_vetor(request):
    if request.method == 'POST':
        vetor = list(request.POST['inputVetor'])
        vetor.sort()
        return render(request, 'index.html', {'vetor': vetor})
