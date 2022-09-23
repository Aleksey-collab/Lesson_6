# 4 Вини пух

def viny_song(song):
    vowels = ["а", "я", "у", "ю", "о", "е", "ё", "э", "и", "ы"]
    lst = [len(list(filter(lambda x: x in vowels,i))) for i in song.split()]
    return ('Пам парам','Парам пам-пам')[len(set(lst)) == 1]
    
s = 'пара-ра-рам рам-пем-папам па-ра-па-дам'
s2 = 'пара-ра-рам рам-пем-папам па-ра-па-дам пара-ра-рам рам-пем-папам па-ра-пб-дам'
s3 = 'пара-ра-рам рам-пем-папам па-ра-па-дам пара-ра-рам рам-пем-папам па-ра-пя-дам'

print(viny_song(s))
print(viny_song(s2))
print(viny_song(s3))