from django.template.defaultfilters import title
from django.utils.termcolors import background

from .models import Poster
from datetime import datetime


p1 = Poster(title='БОЛЬШОЙ СОЛЬНЫЙ КОНЦЕРТ ВИА ВОЛГА-ВОЛГА',
            creator='Салакаев Антон Викторович',
            place='Максимилианс - Клубный ресторан',
            short_description='Дудки, гармонь, гитары, барабаны — адепт придуманного им «волжского расколбаса»...',
            full_description='Дудки, гармонь, гитары, барабаны — адепт придуманного им «волжского расколбаса», ВИА «Волга-Волга» 16 ноября дает большой сольный концерт в Самаре!\n\nСтилистическое направление музыканты определяют как ска-фолк-рок-бардак и приправляют его легким городским романсом .\n\nВ программе концерта - авторские хиты из нового альбома группы и самые забойные каверы.\n\nТанцевать будут все!\n\nВ 2022 году группа отметила 25-летие. Сегодн я «Волга-Волга» дает более 150 концертов в год, участвует в знаковых музыкальных фестивалях и масштабных проектах страны, ежегодно организует и проводит собственныйодноименный музыкальный фестиваль.\n\nПесни «Волги-Волги» находятся в ротации на федеральных радиостанциях, звучат в фильмах и сериалах.\n\nОснователь и солист группы — Антон Салакаев.',
            time_event=datetime(2024, 10, 30, 15, 30),
            preview_image='poster1_preview.webp',
            background_image='poster1_background.webp')

p2 = Poster(title='Жениться Вам надо, барин',
            creator='Туголуков Игорь Олегович',
            place='Самарская государственная филармония',
            short_description='По мотивам повести Н. Некрасова «Осенняя скука»',
            full_description='Действие спектакля происходит в поместье. За окном стужа и темень. До ближайшей усадьбы несколько вёрст. Скука и осенняя тоска одолевают барина Ласукова ежедневно. Он спит весь день, а по вечерам, не зная, чем себя занять, заставляет слуг развлекать его, изображая то цыган с бубном, то петухов на утренней заре и вообще всё, что ему в голову взбредёт. \n\nПодобные вечера случаются практически каждый день. Слуги валятся с ног от усталости, и пока они, переходя от пантомимы к танцам, от игры на пианино обратно к пантомиме, мечтают об отмене крепостного права и о смерти барина одновременно, зрители смеются до слёз и аплодируют. \n\nНо в ходе спектакля становится понятно, что перед нами не просто красочный калейдоскоп скоморошества, плясок, музыкальных номеров. Спектакль выстроен по принципу контраста — в разгар веселья он призывает задуматься о достаточно серьёзных вещах. Ведь не только барин Ласуков, а многие поколения русских людей мучительно пытаются найти ответы на вопросы: «Что делать?», «Кто виноват?», «Как жить?»… \n\nЗамечательный актёрский состав, гротеск и изящно ввёрнутые режиссёром в постановку современные шутки заряжают невероятно позитивным настроением, а потрясающая импровизация актёров со зрительным залом позволяет почувствовать себя частью происходящего на сцене.',
            time_event=datetime(2024, 11, 26, 19, 00),
            preview_image='poster2_preview.webp',
            background_image='poster2_background.webp'
            )

p3 = Poster(title='Кипелов',
            creator='ООО "Артисты и Звёзды"',
            place='СКК "Дворец Спорта имени Владимира Высоцкого"',
            short_description='«Кипелов» — российская рок-группа под руководством Валерия Кипелова',
            full_description='«Кипелов» — российская рок-группа под руководством Валерия Кипелова, основанная в 2002 году. По словам Валерия, группа играет в стиле Хард-н-хеви, а главные ориентиры в творчестве — это «хорошая красивая мелодия и достойный текст». \n\nЛауреат премии «MTV Russia Music Awards» 2004 года как лучший рок-проект. \n\nВ дискографии коллектива семь студийных лонгплеев, пять лайв-релизов, среди достижений - разнообразные номинации и премии: «Чартова дюжина», «Русский топ», «MTV Russia Music Awards», «Золотой венец Победы» и многие другие. «Кипелов» — частый гость фестивалей «Нашествие», «Рок над Волгой», «Славянский базар», «Тамань» и других. Это одна из наиболее успешных в России рок-групп. В настоящее время музыканты активно выступают, принимают участие в крупнейших рок-фестивалях.',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster3_preview.webp',
            background_image='poster3_background.webp'
            )

p4 = Poster(title='Любэ',
            creator='ООО «Л-Бюро»',
            place='Самарская государственная филармония',
            short_description='Группа была основана в 1989-м году И. Матвиенко и Н. Расторгуевым.',
            full_description='Группа была основана в 1989-м году И. Матвиенко и Н. Расторгуевым. Идея создания группы принадлежала композитору Игорю Матвиенко, а своё странное название получила с лёгкой руки Николая Расторгуева(жаргонное словечко из детства Николая, означающее «разный» , «любой» и тп).\n\nЖанр, в котором существует Любэ трудно определить, хотя, его вполне можно назвать - «Фолк-Рок». А социально-патриотическая направленность прослеживается на протяжении всего творческого пути группы.\nХарактерной особенностью Любэ является невероятное количество хитов - песен, которые стали поистине народными:\nАтас, Не валяй дурака, Америка, Конь, Там за туманами, Берёзы, Позови меня тихо по имени, Комбат, Давай за, и много-много других - это песни, которые прошли испытание временем и, популярны по сей день!\n\nЗа 30 с лишним лет группа Любэ дала невероятное количество концертов. Живые выступления группы за эти годы увидели миллионы зрителей в России и за рубежом и сопровождались неизменными аншлагами! Следует отметить, что группа с первого своего появления, мгновенно стала популярной. Песни, написанные Игорем Матвиенко вместе поэтами Александром Шагановым и Михаилом Андреевым , практически, все стали хитами; неповторимый тембр Николая Расторгуева; узнаваемый, характерный стиль аранжировок; уникальное общее звучания группы; наличие хоров во многих произведениях, только подчёркивающие самобытность Любэ - вот это всё, наверно, и объясняет невероятный успех, популярность и любовь зрителя многие годы?!\n\n\nВот уже 30 с лишним лет прошло со дня появления Любэ на сцене, третье поколение зрителей приходит на концерты группы - потому что песни группы Любэ не потеряли своей своей актуальности, привлекательности по сей день!!!',
            time_event=datetime(2024, 11, 5, 19, 00),
            preview_image='poster4_preview.webp',
            background_image='poster4_background.webp'
            )

p5 = Poster(title='Юмористическое шоу команды города Пятигорск',
            creator='ООО КОМАНДА Б',
            place='КРЦ Звезда',
            short_description='Долгожданное событие, гастрольный тур одной из самых ярких команд...',
            full_description='Долгожданное событие, гастрольный тур одной из самых ярких команд в сетке телевизионного вещания, среди юмористических программ, главного канала страны.\n\nКоманда города Пятигорск начала свой путь в 2009 году. Участие в играх межрегиональной лиги, в Краснодаре, что укрепило веру в собственные силы участников команды, что уже в 2011 году позволило выиграть бронзу Высшей лиги. В 2013 году команда становится Чемпионом Высшей лиги параллельно собрав всех больших Кивинов. Дважды побеждала в летних кубках чемпионов.\n\nОдна из самых титулованных команд за всю историю Российского юмора.\n\nКоманда много лет неизменна в своем составе:\nОльга Картункова\nЕкатерина Моргунова\nВладислав Хелоян\nАртур Диланян\nТатьяна Винокурова\nМаксим Киселев\nАнтон Остерников\nАлександр Савченко\nЗаурбек Байцаев\n\nОдна из самых поющих команд покажет свои лучшие эфирные номера и выступления, которые вы могли видеть в проектах Первого канала, в проектах «Игра» и «Концерты» на канале ТНТ.\n\nВ данный момент участники коллектива активно продолжают свое триумфальное шествие в составе команды а так же принимают участие в записи шоу как на телевидении, так на просторах интернета, снимаются в кино и сериалах.',
            time_event=datetime(2024, 11, 9, 19, 00),
            preview_image='poster5_preview.webp',
            background_image='poster5_background.webp'
            )

p6 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 9, 19, 00),
            preview_image='poster6_preview.webp',
            background_image='poster6_background.webp'
            )

p7 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster7_preview.webp',
            background_image='poster7_background.webp'
            )

p8 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster8_preview.webp',
            background_image='poster8_background.webp'
            )

p9 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster9_preview.webp',
            background_image='poster9_background.webp'
            )

p10 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster10_preview.webp',
            background_image='poster10_background.webp'
            )

p11 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster11_preview.webp',
            background_image='poster11_background.webp'
            )

p12 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster12_preview.webp',
            background_image='poster12_background.webp'
            )

p13 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster13_preview.webp',
            background_image='poster13_background.webp'
            )

p14 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster14_preview.webp',
            background_image='poster14_background.webp'
            )

p15 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster15_preview.webp',
            background_image='poster15_background.webp'
            )

p16 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster16_preview.webp',
            background_image='poster16_background.webp'
            )

p17 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster17_preview.webp',
            background_image='poster17_background.webp'
            )

p18 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster18_preview.webp',
            background_image='poster18_background.webp'
            )

p19 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster19_preview.webp',
            background_image='poster19_background.webp'
            )

p20 = Poster(title='',
            creator='',
            place='',
            short_description='',
            full_description='',
            time_event=datetime(2024, 11, 1, 19, 00),
            preview_image='poster20_preview.webp',
            background_image='poster20_background.webp'
            )
