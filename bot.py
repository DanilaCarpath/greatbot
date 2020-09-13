import discord
from discord.ext import commands
from config import settings
import os
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix = settings['prefix'])

# @bot.command() 
# async def хелп(ctx):

#     helpEmbed = discord.Embed ()
#     helpEmbed.add_field (name = "вебхук", value = "Создает вебхук. !вебхук \"заголовок\" \"текст\" айди_канала", inline = False)
    
#     await ctx.send (embed = helpEmbed)

#команда бота
@bot.command() 
@has_permissions(administrator = True)
async def вебхук(ctx, head, body, theid):

    theid = int(theid)

    webhook = discord.Embed ()
    webhook.add_field (name = head, value = body, inline = False)

    channel = ctx.guild.get_channel (theid)

    await channel.send (embed = webhook)

# @bot.command() 
# @has_permissions(administrator = True)
# async def роль(ctx):

#     await ctx.message.delete ()

#     role1 = discord.utils.get(ctx.guild.roles, name = "титул")
#     role2 = discord.utils.get(ctx.guild.roles, name = "осн")
#     role3 = discord.utils.get(ctx.guild.roles, name = "цвет")

#     rolelist = [role1, role2, role3]

#     for i in ctx.guild.members:
        
#         for k in rolelist:

#             await i.add_roles (k)

@bot.command()
async def ник(ctx, new_nick):

    

    emb = discord.Embed ()
    emb.add_field (name = "Ник пользователя " + ctx.author.name + " изменен", value = "Новый никнейм: " + new_nick)
    
    await ctx.message.delete ()

    await ctx.send (embed = emb)
    
    await ctx.author.edit (nick = new_nick)

@bot.command()
@has_permissions(administrator = True)
async def никюзер(ctx, member: discord.Member, new_nick):

    

    emb = discord.Embed ()
    emb.add_field (name = "Ник пользователя " + member.name + " изменен", value = "Новый никнейм: " + new_nick)
    
    await ctx.message.delete ()

    await ctx.send (embed = emb)
    
    await member.edit (nick = new_nick)

    

#запуск бота
token = os.environ.get('BOT_TOKEN')
bot.run (token)


# bot.run (settings['token'])