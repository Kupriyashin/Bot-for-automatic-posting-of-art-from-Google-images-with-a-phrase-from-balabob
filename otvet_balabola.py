def otvet_balabob(text):
    try:

        import json
        import urllib.request

        headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4) AppleWebKit/605.1.15 '
                          '(KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Origin': 'https://yandex.ru',
            'Referer': 'https://yandex.ru/',
        }

        API_URL = 'https://zeapi.yandex.net/lab/api/yalm/text3'
        payload = {"query": f"{text}", "intro": 6, "filter": 1}
        params = json.dumps(payload).encode('utf8')
        req = urllib.request.Request(API_URL, data=params, headers=headers)
        response = urllib.request.urlopen(req)
        response = json.load(response)
        # print(response.read().decode('utf8'))

        return response['text']

    except Exception as err_otvet_balabob:
        print(f"Ошибка при ответе бабалобы: {err_otvet_balabob}")
        return 'error'
