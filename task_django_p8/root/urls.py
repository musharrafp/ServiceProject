import time

from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
#
# from apps.client_admin import client_admin_site
# from root import settings
#
# admin.site.site_header = "P8 group"
# admin.site.site_title = "P8 group ning Adminkasi"
# admin.site.index_title = "P8 group saytiga xush kelibsiz!"
#
from django.core.cache import cache

from apps.documents import CarDocument
from apps.models import Car, Post

# def view(request):
#     user_id = request.user.id
#     if cache.get(user_id):
#         return HttpResponse(user_id)
#     cache.set(user_id, request.user.username)
#     time.sleep(3)
#     return HttpResponse(request.user.username)


# httpx.post('django_url:8000', data)
# def view(request, word):
#     # request.POST['username']
#     # request.POST['password']
#     # User.objects.create()
#
#     # car = Car.objects.create(
#     #     name="Car one",
#     #     color="red",
#     #     type=1,
#     #     description="A beautiful car"
#     # )
#
#     s = CarDocument.search().query("match", name=word)
#     data = []
#     for hit in s:
#         data.append(
#             "Car name : {}, description {}".format(hit.name, hit.description)
#         )
#     return HttpResponse(data)
from django.views.decorators.csrf import csrf_exempt
def view(request):
    if request.method == 'POST':
        Post.objects.create(word=request.POST.get('word'))
        return HttpResponse('saved')
    return HttpResponse('error')


urlpatterns = [
    path('data', csrf_exempt(view)),
    path('admin/', admin.site.urls),
    #   path('client-admin/', client_admin_site.urls),
    #   path('', include('apps.urls')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
