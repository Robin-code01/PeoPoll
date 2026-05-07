from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.http import JsonResponse


@ensure_csrf_cookie
def set_csrf_token(request):
    """
    This view sets the CSRF cookie in the user's browser.
    """
    return JsonResponse({"details": "CSRF cookie set"}, status=200)


# // Next.js side
# const initializeApp = async () => {
#   await fetch('http://localhost:8000/api/set-csrf/', {
#     method: 'GET',
#     credentials: 'include', // CRITICAL: This allows the browser to save the cookie
#   });
# };
