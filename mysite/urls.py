from django.http import JsonResponse
from django.urls import path

BRANCH = "py/django"


def root(request):
    return JsonResponse({"branch": BRANCH, "lang": "python", "framework": "django"})


def healthz(request):
    return JsonResponse({"ok": True})


urlpatterns = [path("", root), path("healthz", healthz)]
