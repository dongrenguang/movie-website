import media
import fresh_tomatoes

MrTree = media.Movie('Hello！树先生', 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p1271999126.webp', 'http://59.108.140.32/vhot2.qqvideo.tc.qq.com/AWwBSK8Buv93HSGWbYFQIsWCoEGmW2BexdO4xpYVMEMU/x052612vu0v.p712.1.mp4?sdtfrom=v1010&guid=0a4e1676c4e7dc81f10a388917982cb9&vkey=44683E0FCB93511AFD89824883E0B7E2BE8844ECA549C1DC9263DCDF805A59D6A882302BAFDEE85210DD1AA80D6E08BD2B3CC59AF8FFAE2CF0C416A899AE5BED4E4D9DC113CB433DDED303F2D94FE5CB7C3063E73A01E343A972030CF9ECD0C68DF3ED0B0FF7D109E2DE354D0DE88FBF7365BE9B8BC434AB&platform=2')
songOfThePhoenix = media.Movie('百鸟朝凤', 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2332714135.webp', 'https://v.qq.com/x/cover/gxe3ckvdykdxmfo.html')
theManFromEarth = media.Movie('这个男人来自地球', 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p513303986.webp', 'http://v.youku.com/v_show/id_XNTg2OTc3OTgw.html?spm=a2h0j.8191423.vpofficiallistv5_wrap.5~5~5~5~5~5~A')
duckweed = media.Movie('乘风破浪', 'https://img1.doubanio.com/view/movie_poster_cover/lpst/public/p2408407697.webp', 'https://v.qq.com/x/cover/yrk9u3rwbp1gmws.html?ptag=douban.movie')
bigFish = media.Movie('大鱼海棠', 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2361744534.webp', 'https://v.qq.com/x/cover/we35g3aduiwkudp.html?ptag=douban.movie')
gattaca = media.Movie('千钧一发', 'https://img3.doubanio.com/view/movie_poster_cover/lpst/public/p2195672555.webp', 'https://v.qq.com/x/cover/fqc9exx7n20bjuj.html?ptag=douban.movie')

movies = [MrTree, songOfThePhoenix, theManFromEarth, duckweed, bigFish, gattaca]
fresh_tomatoes.open_movies_page(movies)
