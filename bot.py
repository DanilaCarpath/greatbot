import discord
from discord.ext import commands
from config import settings
import os
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def c (ctx, _message):

    newmessage = "[" + ctx.author.name + "] " + _message

    for k in bot.guilds:
        if k != ctx.guild:
            try:
                channel = discord.utils.get (k.channels, name = "international")
                await channel.send (newmessage)
            except:
                continue    

@bot.event
async def on_message(message):

    #временный сервер для проверки канала
    tempguild = message.author.guild

    #канал для проверки
    checkchannel = discord.utils.get (tempguild.channels, name = "international")

    #проверка на соотствие канала, где написали и нужного канала
    if message.channel == checkchannel:

        #проверка на бота
        if message.author.bot:
            print ("бот")
        
        #если автор - не бот
        else:

            #сообщение с упоминанием автора
            newmessage = '{0.author}: {0.content}'.format(message)

            #цикл на все сервера
            for k in bot.guilds:

                #канал, в который отправим
                channel = discord.utils.get (k.channels, name = "international")

                #проверка, чтобы не отправлялось на сервер автора
                if k != message.guild:

                    #проверка на наличие канала
                    try:

                        #отправка сообщения
                        await channel.send (newmessage)
                    except:
                        continue

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
