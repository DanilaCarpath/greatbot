import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    avatar = message.author.avatar_url

    messageAuthorTemp = '{0.author}'.format(message)
    messageAuthor = messageAuthorTemp[:-5]
    
    tempguild = message.guild
    channel = discord.utils.get (tempguild.channels, name = "international")
    
    if message.author.bot:
        
        print ("бот")
        
    else:
        
        embed = discord.Embed (color=0x6600ff, description = message.content )
        embed.set_author (name = messageAuthor, icon_url = avatar)

        try:
            
            await channel.send (embed = embed)
            
        except:
            
            print ("oshibka")
    
    messcont = str(message.content)
    mess = messcont.lower ()
    
    if "протокол ХУЙ" in message.content:
        
        i = 3
        
        while i != 0:
            
            i = i - 1
        
            await message.channel.send ("@everyone ВНИМАНИЕ! Чертик азазель узурпировал власть! Легитимное правительство бойкотирует переворот! Всем солидарным с легитимным правительством просьба выйти с этого сервера и зайти по данной ссылке https://discord.gg/Cv7z9Q ")
    
    if "suck" in message.content:
        
        await message.channel.send (message.author.mention + " fuck my ass")
        
    
    if message.author.bot:
        print ("bot")
    else:
        
        i_comm = ["комм", "соц", "маркс", "ленин", "сталин"]
        maxis = ["макси", "макся", "максимиллиана", "сакся", "сакси", "членкси", "сракси"]
        louis = ["луи", "луя", "луй"]
        mihey = ["михей", "михуй"]
        
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
    
        for i in maxis:
            if i in mess:
                await message.channel.send (message.author.mention + " " + i + "? " + i + " чмо конченое")
                
        
    
        for i in louis:
            if i in mess:
                await message.channel.send (message.author.mention + " ЛУИ ВЕЛИЧАЙШИЙ БОГ И ЕБЫРЬ")
                
        
             
        for name in mihey:
            if name in mess:
                randcount = random.randint (1, 5) - 1
                
                frazes = ["Анком мощь", "Я КОММ ШИЗОФРЕНИК", "я лгбт мальчик", "Я либерал кста", "Я не либерал кста"]
                
                await message.channel.send (message.author.mention + "Ты сказал " + name + "? " + frazes[randcount])

    if message.author.id == 765990912928514138:
        await message.delete ()

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
