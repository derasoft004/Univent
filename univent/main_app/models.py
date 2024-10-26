from django.db import models


class Poster(models.Model):
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    price = models.IntegerField()
    short_description = models.TextField(blank=True, null=True)
    full_description = models.TextField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_event = models.DateTimeField()
    preview_image = models.CharField(max_length=255)
    background_image = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.creator}_{self.title}'

# p1 = Poster(title='БОЛЬШОЙ СОЛЬНЫЙ КОНЦЕРТ ВИА ВОЛГА-ВОЛГА', creator='Максимилианс - Клубный ресторан', short_description='Дудки, гармонь, гитары, барабаны — адепт придуманного им «волжского расколбаса»...', full_description='Дудки, гармонь, гитары, барабаны — адепт придуманного им «волжского расколбаса», ВИА «Волга-Волга» 16 ноября дает большой сольный концерт в Самаре!\n\nСтилистическое направление музыканты определяют как ска-фолк-рок-бардак и приправляют его легким городским романсом .\n\nВ программе концерта - авторские хиты из нового альбома группы и самые забойные каверы.\n\nТанцевать будут все!\n\nВ 2022 году группа отметила 25-летие. Сегодн я «Волга-Волга» дает более 150 концертов в год, участвует в знаковых музыкальных фестивалях и масштабных проектах страны, ежегодно организует и проводит собственныйодноименный музыкальный фестиваль.\n\nПесни «Волги-Волги» находятся в ротации на федеральных радиостанциях, звучат в фильмах и сериалах.\n\nОснователь и солист группы — Антон Салакаев.', time_event=datetime(2024, 10, 30, 15, 30), preview_image='images/poster1_preview.webp')


class User(models.Model):
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    about = models.TextField(blank=True, null=True)
    hobby = models.TextField(blank=True, null=True)
    is_creator = models.BooleanField(default=False)
    events = models.ManyToManyField('Poster', related_name='poster')

    def __str__(self):
        return self.nickname