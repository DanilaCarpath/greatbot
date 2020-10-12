import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    messcont = str(message.content)
    mess = messcont.lower ()
    
    if message.author.id == 765121432665325589:
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
    
    i_comm = ["комм", "соц", "маркс", "ленин", "сталин"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in i_comm:
            if i in mess:
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
    #
    maxis = ["Макси", "макси", "макся", "Максимилиана", "максимиллиана", "МАКС", "Макся" , "сакся", "сакси","Сакся","Сакси", "Членкси", "членкси", "сракси", "Сракси"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in maxis:
            if i in message.content:
                await message.channel.send (message.author.mention + " " + i + "? " + i + " сосет хуй")
                
    louis = ["Лу", "лу", "ЛУ"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in louis:
            if i in message.content:
                await message.channel.send (message.author.mention + " ЛУИ ВЕЛИЧАЙШИЙ БОГ И ЕБЫРЬ")
                
    mihey = ["михей", "михуй"]
             
    if message.author.bot:
        print ("bot")
    else:
        for i in mihey:
            if i in mess:
                randcount = random.randint (1, 3) - 1
                
                frazes = ["Анком мощь", "Я КОММ ШИЗОФРЕНИК", "я лгбт мальчик"]
                
                await message.channel.send (message.author.mention + "Ты сказал " + i  + "? " + frazes[randcount])

    



token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
