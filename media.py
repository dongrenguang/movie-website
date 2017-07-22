import webbrowser

class Movie():
    """ 电影类，包含电影标题、海报图片链接、youtube上的预告片地址等 """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url  = trailer_youtube_url
