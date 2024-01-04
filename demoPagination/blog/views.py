from django.shortcuts import render
from .models import postModel
from django.core.paginator import Paginator
# Create your views here.
def list(request):
    pm = postModel.objects.all()
    paginator = Paginator(pm, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/listpost.html', {'page_obj': page_obj})