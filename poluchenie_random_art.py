def random_art():
    try:
        import os.path
        import random

        color = ["color", "blackandwhite", "red", "orange", "yellow", "green", "teal", "blue", "purple",
                 "pink", "white", "gray", "black", "brown"]
        type_foto = ['art', 'wallpapers', 'манга', 'manga']

        with open('Data/Anime.txt', 'r', encoding='UTF-8') as key:
            keyword = key.readlines()
            keyword = random.choice(keyword)

        from icrawler.builtin import GoogleImageCrawler

        google_crawler = GoogleImageCrawler(storage={
            'root_dir': r"Images/"
        })

        google_crawler.crawl(keyword=f"{keyword} {type_foto[random.randint(0, len(type_foto) - 1)]}", max_num=10,
                             filters={
                                 "color": f"{color[random.randint(0, len(color) - 1)]}",
                                 'size': 'large',
                             })

        DIR = 'Images'
        image = (open(os.path.join(DIR, random.choice(os.listdir(DIR))))).name

        import glob
        files = glob.glob('Images/*')
        for f in files:
            if f != image:
                os.remove(f)

        files.clear()
        del files

        return image, keyword

    except Exception as art_error:
        print(f"Произошла ошибка в функции random_art: {art_error}")
        return 'error'
