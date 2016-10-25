import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from apis import facebook

__all__ = [
    'friends_ranking'
]


def friends_ranking(request):
    if request.GET.get('error'):
        return HttpResponse('사용자 로그인 거부')
    if request.GET.get('code'):
        redirect_url = 'http://{host}{url}'.format(
            host=request.META['HTTP_HOST'],
            url=reverse('sns:friends_ranking')
        )
        print('%s' % redirect_url)
        code = request.GET.get('code')
        access_token = facebook.get_access_token(code, redirect_url)
        user_id = facebook.get_user_id_from_token(access_token)

        url_request_feed = 'https://graph.facebook.com/v2.8/{user_id}/feed?' \
                           'fields=from{{name}},message,comments.limit(100){{from{{name,picture}},message,comments{{from{{name,picture}},message}}}}&' \
                           'access_token={access_token}'.format(
                            user_id=user_id,
                            access_token=access_token,
        )
        r = requests.get(url_request_feed)
        dict_feed_info = r.json()
        json_data = json.dumps(dict_feed_info, indent=2)
        print(json_data)

        feed_count = {}

        for feed in dict_feed_info['data']:
            if 'comments' in feed:
                for feed2 in feed['comments']['data']:
                    if 'comments' in feed2:
                        for feed3 in feed2['comments']['data']:
                            if feed3['from']['name'] in feed_count:
                                feed_count[feed3['from']['name']] += 1
                            else:
                                feed_count[feed3['from']['name']] = 1
                    if feed2['from']['name'] in feed_count:
                        feed_count[feed2['from']['name']] += 1
                    else:
                        feed_count[feed2['from']['name']] = 1




        return render(request, 'sns/facebook.html', {'feed_count': feed_count})
