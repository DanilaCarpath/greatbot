import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    message.channel == ctx
    
    tempguild = message.guild
    channel = discord.utils.get (tempguild.channels, name = "international")
    
    if ctx = channel:
        
        await ctx.send ("проверка пройдена")
    
    
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
        
        await ctx.send (message.author.mention + " fuck my ass")
    
    if message.content == "pingallsecret":
        await message.delete ()
        await ctx.send ("@everyone активим сучки")
    
    i_comm = ["комм", "соц", "маркс", "ленин", "сталин"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in i_comm:
            if i in mess:
                randcount = random.randint (1, 5)
                
                if randcount == 1:
                    await ctx.send ("коммунизм пук")
                elif randcount == 2:
                    await ctx.send ("СИЛЫ КОММУНИЗМА ПОБЕДЯТ")
                elif randcount == 3:
                    await ctx.send ("да здравствует коммунистическая революция!")
                elif randcount == 4:
                    await ctx.send ("во славу КОММУНИЗМА!")
                elif randcount == 5:
                    await ctx.send ("союз нерушимых республик свободных...")
    #
    maxis = ["Макси", "макси", "макся", "Максимилиана", "максимиллиана", "МАКС", "Макся" , "сакся", "сакси","Сакся","Сакси", "Членкси", "членкси", "сракси", "Сракси"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in maxis:
            if i in message.content:
                await ctx.send (message.author.mention + " " + i + "? " + i + " сосет хуй")
                
    louis = ["Луи", "луи", "ЛУИ", "Луй", "луя", "луй"]
    
    if message.author.bot:
        print ("bot")
    else:
        for i in louis:
            if i in message.content:
                await ctx.send (message.author.mention + " ЛУИ ВЕЛИЧАЙШИЙ БОГ И ЕБЫРЬ")
                
    mihey = ["михей", "михуй"]
             
    if message.author.bot:
        print ("bot")
    else:
        for i in mihey:
            if i in mess:
                randcount = random.randint (1, 5) - 1
                
                frazes = ["Анком мощь", "Я КОММ ШИЗОФРЕНИК", "я лгбт мальчик", "Я либерал кста", "Я не либерал кста"]
                
                await ctx.send (message.author.mention + "Ты сказал " + i  + "? " + frazes[randcount])

    



token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
