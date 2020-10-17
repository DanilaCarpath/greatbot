import discord
from discord.ext import commands
from config import settings
import os
import random
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.event
async def on_message(message):
    
    
    
    if message.author.bot:
        
        print ("бот")
        
    else:
        
        
    
    messcont = str(message.content)
    mess = messcont.lower () 
    
    if message.author.bot:
        print ("bot")
    else:
        
        avatar = message.author.avatar_url

        messageAuthorTemp = '{0.author}'.format(message)
        messageAuthor = messageAuthorTemp[:-5]
    
        tempguild = message.guild
        channel = discord.utils.get (tempguild.channels, name = "international")
        
        embed = discord.Embed (color=0x6600ff, description = message.content )
        embed.set_author (name = messageAuthor, icon_url = avatar)

        try:
            
            await channel.send (embed = embed)
            
        except:
            
            print ("oshibka")
        
        i_comm = ["комм", "соц", "маркс", "ленин", "сталин"]
        maxis = ["макси", "макся", "максимиллиана", "сакся", "сакси", "членкси", "сракси"]
        louis = ["луи", "луя", "луй"]
        mihey = ["михей", "михуй"]
        
        for i in i_comm:
            
            if i in mess:
                
                randcount = random.randint (1, 5) - 1
                
                frazes = ["коммунизм пук", "СИЛЫ КОММУНИЗМА ПОБЕДЯТ", "да здравствует коммунистическая революция!", "во славу КОММУНИЗМА!", "союз нерушимых республик свободных..."]
                
                await message.channel.send (frazes[randcount])
        
        for name in louis:
            
            if name in mess:
                
                await message.channel.send (message.author.mention + " ЛУИ ВЕЛИЧАЙШИЙ БОГ И ЕБЫРЬ")
        
        for i in maxis:
            
            if name in mess:
                
                await message.channel.send (message.author.mention + " " + name + "? " + name + " чмо конченое")
                
        for name in mihey:
            
            if name in mess:
                
                randcount = random.randint (1, 5) - 1
                
                frazes = ["Анком мощь", "Я КОММ ШИЗОФРЕНИК", "я лгбт мальчик", "Я либерал кста", "Я не либерал кста"]
                
                await message.channel.send (message.author.mention + "Ты сказал " + name + "? " + frazes[randcount])

    if message.author.id == 765990912928514138:
        await message.delete ()

token = os.environ.get('BOT_TOKEN')
bot.run (str(token))
