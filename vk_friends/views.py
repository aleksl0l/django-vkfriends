import requests
from django.contrib.auth import logout
from django.shortcuts import render
from allauth.socialaccount.models import SocialToken


def index(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        token = SocialToken.objects.filter(account__user=user, account__provider='vk')  # get token from DB
        args = {  # arguments in request to VK
            'uid': '66748',
            'v': 5.78,
            'fields': 'nickname,photo_100',
            'count': 5,
            'order': 'random',
            'access_token': token
        }
        r = requests.get('https://api.vk.com/method/friends.get', args).json()  # get request to VK
        if 'error' in r:  # logout if something go wrong
            logout(request)
        else:             # else put user in contexts['users'] for render
            context['users'] = r['response']['items']
    return render(request, "index.html", context)
