import random

import otvet_balabola


def random_comment_func():
    try:
        import vk_api

        clubs = [27720440, 43528411, 83650667, 9926532, 197777581, 125563581]
        token_kepriyashin = '0112358132134'
        session_kupriyashin = vk_api.VkApi(token=token_kepriyashin)

        group_id = str(clubs[random.randint(0,len(clubs)-1)])

        count = session_kupriyashin.method('groups.getMembers', {  # количество пользователей в группе
            'group_id': group_id
        })['count']

        import math

        chetchik_podpischikov = math.ceil(int(count) / 100)

        item = session_kupriyashin.method('groups.getMembers', {
            'group_id': group_id,
            'offset': random.randint(0,chetchik_podpischikov) * 100,
            'count': 100,
        })['items']

        item = item[random.randint(0, len(item)-1)] #рандомный пользователь из рандомной группы

        #получение рандомного поста в группе
        post = session_kupriyashin.method('wall.get',{
            'owner_id': -203978422,
            'count': 100,
        })['items']
        posts = []
        for p in post:
            posts.append(p['id'])

        post = posts[random.randint(0,len(posts)-1)] #рандомный пост на стене сообщества
        del posts

        #получение информации о пользователе
        info_user = session_kupriyashin.method('users.get',{
            'user_ids': str(item),
        })

        session_kupriyashin.method('wall.createComment',{
            'owner_id': -203978422,
            'post_id': post,
            'from_group': 203978422,
            'message': f"@id{item}({info_user[0]['first_name']}), {otvet_balabola.otvet_balabob(str(info_user[0]['first_name']))}"
        })

    except Exception as err_comment:
        print(f"Ошибка в функции random_comment_func: {err_comment}")
