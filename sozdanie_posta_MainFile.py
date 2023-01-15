import requests
import vk_api
import datetime

token_kepriyashin = '0112358132134'
session_kupriyashin = vk_api.VkApi(token=token_kepriyashin)

dlya_posts_dt = datetime.datetime.today()
dlya_tegs_dt = datetime.datetime.today()

while True:

    osnov_dt = datetime.datetime.now()

    if osnov_dt >= dlya_posts_dt:

        try:

            from art_and_otvet import otvet_and_art

            text, image, anime = otvet_and_art()

            # {'album_id': 292146558, 'upload_url': 'https://pu.vk.com/c231231', 'user_id': 247636154} пример
            upload_url = session_kupriyashin.method('photos.getUploadServer', {
                'album_id': 278906770,
                'group_id': 203978422
            })['upload_url']

            request = requests.post(upload_url, files={'file': open(f"{image}", 'rb')})  # загружаем файл на сервер

            server = request.json()['server']
            photos_list = request.json()['photos_list']
            aid = request.json()['aid']
            hash = request.json()['hash']

            save_photo = session_kupriyashin.method('photos.save', {
                'album_id': 278906770,
                'group_id': 203978422,
                'server': server,
                'photos_list': photos_list,
                'hash': hash,
                'caption': f"{anime}"
            })[0]

            album_id = save_photo['album_id']
            id_image = save_photo['id']
            owner_id = save_photo['owner_id']

            print(id_image, datetime.datetime.now())
            print(owner_id, datetime.datetime.now())

            session_kupriyashin.method('wall.post', {
                'owner_id': owner_id,
                'from_group': 1,
                'message': f"{text}\n",
                'attachments': f"photo{owner_id}_{id_image}",
                'copyright': 'https://www.google.ru/search?q=fybvt&tbm=isch&ved=2ahUKEwisyY-wu6T8AhULBxAIHZJ7DNwQ2-cCegQIABAA&oq=fybvt&gs_lcp=CgNpbWcQAzIECAAQQzIECAAQQzIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjIHCAAQgAQQCjoECCMQJzoICAAQChABEEM6BAgAEB46CwgAEIAEEAoQARAYOgkIABCABBAKEBg6CQgAEIAEEAoQAToFCAAQgAQ6CAgAEIAEELEDOgsIABCABBCxAxCDAToHCCMQ6gIQJ1AAWNheYJBgaAJwAHgAgAGBAYgB_geSAQQxNS4ymAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=Y3ywY-yLGYuOwPAPkvex4A0&bih=990&biw=1370'

            })

            dlya_posts_dt = (osnov_dt + (datetime.timedelta(minutes=60)))

        except Exception as err_public:
            print(f"Произошла ошибка при публикации изображения: {err_public}")

    if osnov_dt >= dlya_tegs_dt:
        try:
            from random_comment import random_comment_func

            random_comment_func()
            dlya_tegs_dt = (osnov_dt + (datetime.timedelta(minutes=30)))
        except Exception as err_comment:
            print(f"Ошибка в постоянном цикле при отправки коммента: {err_comment}")
