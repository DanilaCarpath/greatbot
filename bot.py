import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    midd = message.author.id
    
    #765121432665325589
    if midd == 765121432665325589:
        await message.delete ()
    
    if "протокол ХУЙ" in message.content:
        
        i = 3
        
        while i != 0:
            
            i = i - 1
        
            await message.channel.send ("@everyone ВНИМАНИЕ! Чертик азазель узурпировал власть! Легитимное правительство бойкотирует переворот! Всем солидарным с легитимным правительством просьба выйти с этого сервера и зайти по данной ссылке https://discord.gg/Cv7z9Q ")
    
    if "suck" in message.content:
        
        await message.channel.send (message.author.mention + " fuck my ass")
    
    if message.content == "pingallsecret":
        await message.delete ()
        await message.channel.send ("@everyone активим сучки")
    
    messcont = str(message.content)
    messcontlowered = messcont.lower ()
    
    i_comm = ["комм", "соц", "маркс", "ленин", "сталин"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in i_comm:
            if i in messcontlowered:
                randcount = random.randint (1, 5)
                
                if randcount == 1:
                    await message.channel.send ("коммунизм пук")
                elif randcount == 2:
                    await message.channel.send ("СИЛЫ КОММУНИЗМА ПОБЕДЯТ")
                elif randcount == 3:
                    await message.channel.send ("да здравствует коммунистическая революция!")
                elif randcount == 4:
                    await message.channel.send ("во славу КОММУНИЗМА!")
                elif randcount == 5:
                    await message.channel.send ("союз нерушимых республик свободных...")
    #"Макси", "макси", "макся", "Максимилиана", "максимиллиана", "МАКС", "Макся"
    maxis = ["Мак", "мак" , "сакся", "сакси","Сакся","Сакси", "Членкси", "членкси", "сракси", "Сракси"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in maxis:
            if i in message.content:
                await message.channel.send (message.author.mention + " Макси? Макси сосет хуй")
    louis = ["Лу", "лу", "ЛУ"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in louis:
            if i in message.content:
                await message.channel.send (message.author.mention + " ЛУИ ВЕЛИЧАЙШИЙ БОГ И ЕБЫРЬ")


    

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
