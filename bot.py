import discord
from discord.ext import commands
from config import settings
import os
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
@has_permissions(administrator=True)
async def pingall (ctx):
    
    await ctx.message.delete ()
    await. ctx.send ("@everyone")

@bot.event
async def on_message(message):
    
    i_comm = ["я коммунист", "Я КОММУНИСТ", "Я коммунист", "я Коммунист"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in i_comm:
            if i in message.content:
                await message.channel.send (message.author.mention + " лох ты а не коммунист")

    maxis = ["Макси", "макси", "макся", "Максимилиана", "максимиллиана", "МАКС", "Макся"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in maxis:
            if i in message.content:
                await message.channel.send ("Макси сосет хуй")

    

    #переменные
    membr = message.author
    avatar = membr.avatar_url
    #сообщение с упоминанием автора
    messageAuthorTemp = '{0.author}'.format(message)
    messageAuthor = messageAuthorTemp[:-5]
        

    messageContent = '{0.content}'.format(message)
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
        
            await message.delete ()

            embed = discord.Embed (color=0x6600ff, description = messageContent )
            embed.set_author(name= messageAuthor, icon_url = avatar)
        
            

            #цикл на все сервера
            for k in bot.guilds:

                #канал, в который отправим
                channel = discord.utils.get (k.channels, name = "international")


                #проверка на наличие канала
                try:
                    #отправка сообщения
                    await channel.send (embed = embed)
                except:
                    continue

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
