from django.shortcuts import render


def pass_cad(request):
    return render(request, 'app/pass_cad.html', {})
