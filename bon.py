import disnake
from disnake.ext import commands
import requests
from bs4 import BeautifulSoup
import random
import typing
import datetime
import wikipedia
import discord
import json
import asyncio
import os
from datetime import datetime
from disnake import ApplicationCommandInteraction
from discord import Intents
from dotenv import load_dotenv
from datetime import datetime, timedelta
from datetime import datetime, timezone

now = datetime.now(timezone.utc)

intents = Intents.default()
intents.members = True

bot = discord.Client(intents=intents)

intents = disnake.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.slash_command(description="Отправляем крутую фотку с котом")
async def котанус(context: disnake.ApplicationCommandInteraction):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    await context.response.send_message(data['file'])

facts = [
    "Кошки могут спать до 16 часов в день.",
    "Кошки пьют воду с помощью языка, образованного в форме ложечки.",
    "Кошки видят в темноте на 6 раз лучше, чем человек.",
    "У Зуфарчика большие планы на будущее",
    "Самця кенгуру називають бумером",
    "Медоносные пчелы ориентируются, используя Солнце в качестве компаса",
    "Среднее кучевое облако весит более 70 взрослых тираннозавров",
    "Утконосы потеют",
    "Вы всегда смотрите на свой нос, ваш мозг просто предпочитает его игнорировать",
    "Резиновые ленты служат дольше в холодильнике",
    "Радугу можно увидеть только утром или ближе к вечеру",
    "Колючие лангусты мигрируют группами по 50 и более особей, образуя линию конга на дне океана",
    "У тигров полосатая кожа, а не только полосатый мех",
    "Чтобы сделать один фунт меда, медоносная пчела должна собрать около двух миллионов цветков",
    "Колючие лангусты мигрируют группами по 50 и более особей, образуя линию конга на дне океана",
    "Полная луна в девять раз ярче полумесяца",
    "Коровы дают больше молока, когда слушают музыку",
    "Кошки имеют более 100 разных звуковых сигналов, чтобы выразить свои мысли.",
    "Самая длинная запись о кошке занимает 870 страниц и была написана в 1879 году."
]

@bot.slash_command(description="Самые интересные факты в мире")
async def факты(ctx: disnake.ApplicationCommandInteraction):
    random_факты = random.choice(facts)
    await ctx.response.send_message(random_факты)
  
messages = [
    "***Людмила не любит аниме***",
    "***Иван анимешник и ето факт***",
    "***Обещанный Неверленд***",
    "***Гуррен-Лаганн***",
    "***Патриотизм Мориарти***",
    "***Дарованный***",
    "***Семья шпиона***",
    "***Истребитель демонов***",
    "***Маг на полную ставку***",
    "***Без игры — нет жизни***",
    "***Добро пожаловать в класс превосходства***",
    "***Руководство гениального принца по вызволению страны из долгов***",
    "***Девушка на час***",
    "***Доблесть рыцаря-неудачника***",
    "***Гордость убийцы***",
    "***Абсолютный дуэт***",
    "***Эта фарфоровая кукла влюбилась***",
    "***Лучший в мире ассасин, переродившийся в другом мире как аристократ***",
    "***Плод эволюции: Жизнь наладилась в мгновение ока***",
    "***В другом мире со смартфоном***",
    "***Лунное путешествие приведёт к новому миру***"
]

# Функция, которая будет вызываться при получении команды от пользователя
@bot.slash_command(description="Выбераем, какое аниме ты будешь смотреть сегодня")
async def аниме(ctx: disnake.ApplicationCommandInteraction):
    # Если команда вызвана самим ботом, то ничего не делаем
    if ctx.author == bot.user:
        return

    # Если команда вызвана в текстовом канале, то случайно отправляем одно из сообщений
    if isinstance(ctx.channel, disnake.TextChannel):
        await ctx.response.send_message(random.choice(messages))

films_messages = [
    '''***Чёрная Пантера: Ваканда навеки***
||**https://rezka.ag/films/fiction/50385-chernaya-pantera-vakanda-naveki-2022.html**||''',
    '''***Не дыши 2***
||**https://rezka.ag/films/thriller/40714-ne-dyshi-2-2021.html**||''',
    '''***Призрак***
||**https://rezka.ag/films/family/8111-prizrak-2015.html**||''',
    '''***Жестокая ночь***
||**https://rezka.ag/films/action/52192-zhestokaya-noch-2022.html**||''',
    '''***Ночной оборотень***
||**https://rezka.ag/films/horror/51590-nochnoy-oboroten-2022.html**||''',
    '''***Морской бой***
||**https://rezka.ag/films/fiction/468-morskoy-boy-2012.html**||''',
    '''***Майор Гром: Чумной Доктор***
||**https://rezka.ag/films/action/37293-mayor-grom-chumnoy-doktor-2021.html**||''',
    '''***Пассажиры***
||**https://rezka.ag/films/fiction/20840-passazhiry-2016.html**||''',
    '''***Малыш на драйве***
||**https://rezka.ag/films/action/24148-malysh-na-drayve-2017.html**||''',
    '''***Невероятная история Острова роз***
||**https://rezka.ag/films/drama/36204-neveroyatnaya-istoriya-ostrova-roz-2020.html**||''',
    '''***Код 8***
||**https://rezka.ag/films/action/32737-kod-8-2019.html**||'''
]

# Функция, которая будет вызываться при получении команды от пользователя
@bot.slash_command(description="Выбераем, какой фильм ты будешь смотреть сегодня")
async def фильм(ctx: disnake.AppCommandInteraction):
    # Если команда вызвана самим ботом, то ничего не делаем
    if ctx.author == bot.user:
        return

    # Если команда вызвана в текстовом канале, то случайно отправляем одно из сообщений
    if isinstance(ctx.channel, disnake.TextChannel):
        await ctx.response.send_message(random.choice(films_messages))
          
@bot.slash_command(description="Не нажимай братан, а то...")
async def пупупу(interaction: disnake.AppCmdInter):
    await interaction.send('''**Здесь могла бы быть ваша реклама.**
    
Заказать рекламу: https://t.me/Andremuhamed''')     

@bot.slash_command(description="Отправляем крутую фотку с собакой")
async def собатанус(context: disnake.ApplicationCommandInteraction):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    await context.response.send_message(data['message'])

anecdotes = [
    "Как-то раз программисты решили поехать в поход. Но на месте оказалось, что им не хватает топлива. Как быть? Делать новый алгоритм, который бы экономил топливо? Нет, они просто добавили еще один программиста, который не пойдет в поход.",
    "Если вы думаете, что можете научиться программировать за 24 часа, то вы также можете научиться готовить за 24 минуты, играть в шахматы за 24 секунды, и побеждать в войну за 24 дня.",
    "Если вы программист, то лучший способ выучить что-то новое - это попробовать написать код на эту тему. Если вы не программист, то лучший способ выучить что-то новое - это попробовать написать код на эту тему и сделать его работающим.",
    "Одна веб-страница спрашивает пользователя: 'Вы робот?' Если вы выберете ответ 'Нет', то она спросит: 'А как тогда вы провернули такую сложную капчу?'",
    "Программист и его жена решили взять кошку. Программист назвал ее 'Код'. 'Почему ты назвал ее Код?' - спросила жена. 'Потому что она всегда делает что-то не то, что нужно', - ответил программист.",
    "Как говорят, программисты любят три вещи: кофе, клавиатуру и ошибки. Из них только первые две полезны.",
    "Хороший программист - это тот, кто гуглит быстрее, чем вы.",
"Какая разница между программистом и ученым-исследователем? Ученый-исследователь думает, что каждая его программа - это уникальное исследование. А программист знает, что каждая его программа - это копия предыдущей.",
    "Один программист спрашивает другого: 'Почему ты так долго работаешь над этой программой?' - 'Я хочу, чтобы она была готова к завтрашнему дню' - отвечает другой. - 'Но завтра же выходной!' - удивляется первый. - 'Ну и что? Моя программа работает по будням и по выходным!'"
]

@bot.slash_command(description="Отправляем анекдоты")
async def анекдот(ctx: disnake.ApplicationCommandInteraction):
    random_анекдот = random.choice(anecdotes)
    await ctx.response.send_message(random_анекдот)
  
UNSPLASH_API_KEY = "4E1JqzRfSm47fuk_sQxmU2NjdWtbBVXIo6ScVeVZALY"

@bot.slash_command(description="Отправляет фото машин")
async def машинус(context: disnake.ApplicationCommandInteraction):
    response = requests.get(f'https://api.unsplash.com/photos/random?query=car&client_id={UNSPLASH_API_KEY}')
    data = response.json()
    image_url = data['urls']['regular']
    await context.send(content=image_url)

API_KEY = "rjl"

@bot.slash_command(description="Отправляет фото цветка")
async def цвенус(context: disnake.ApplicationCommandInteraction):
    response = requests.get(f'https://api.unsplash.com/photos/random?query=flowers&client_id={API_KEY}')
    data = response.json()
    image_url = data['urls']['regular']
    await context.send(content=image_url)

PLASH_API_KEY = "rjl"

@bot.slash_command(description="Отправляет фото компьютеров")
async def комнус(context: disnake.ApplicationCommandInteraction):
    response = requests.get(f'https://api.unsplash.com/photos/random?query=computer&client_id={PLASH_API_KEY}')
    data = response.json()
    image_url = data['urls']['regular']
    await context.send(content=image_url)
  
message_threshold_1 = 60
message_counter_1 = 0
message_threshold_2 = 40
message_counter_2 = 0

users = {}

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
    global message_counter_1, message_counter_2

    # Перевірка, що повідомлення не від бота і не знаходиться в приватному повідомленні
    if not message.author.bot and isinstance(message.channel, disnake.TextChannel):
        message_counter_1 += 1
        message_counter_2 += 1

        if message_counter_1 == message_threshold_1:
            channel = message.channel
            await channel.send('''**Не забудьте подписаться на наши каналы нашего сервера:**
ANIME CAT: https://www.youtube.com/@anime_catanus
Xiaomi IGROMAH: https://www.youtube.com/@Xiaomigroman

А также присоединяйтесь к нашей группе в ВК: https://vk.com/cinanima''')
            message_counter_1 = 0

        if message_counter_2 == message_threshold_2:
            channel = message.channel
            await channel.send('''**Стать акционером:**  
ↈ https://donatello.to/andremuhamad
ↈ https://www.donationalerts.com/r/andremuhamad
''')
            message_counter_2 = 0

    if isinstance(message.channel, disnake.DMChannel):
        user_id = message.author.id
        if user_id not in users:
            users[user_id] = 0
        if users[user_id] < 1:
            await message.channel.send("Благодарю вас за сообщение! На данный момент я не могу общаться, так как занят работой круглосуточно на сервере https://discord.gg/fZ8vnRUcH8")
            users[user_id] += 1
        else:
            dm_channel = await message.author.create_dm()
            await dm_channel.send('''Пожалуйста, больше мне не пишите! Я сейчас работаю на сервере https://discord.gg/fZ8vnRUcH8''')
            await message.author.block() 

    await bot.process_commands(message) 


bot.run('njrty')

3каа4а54еп4еп5еп5п5нр6
