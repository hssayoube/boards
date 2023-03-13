from django.shortcuts import render

def image_editor(request):
    return render(template_name='image_editor.html', request=request)