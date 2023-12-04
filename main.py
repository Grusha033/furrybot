import disnake
from disnake.ext import commands 
import random

from getFurryImages import getFurryImage

bot = commands.Bot(command_prefix = "112.", help_command = None, intents = disnake.Intents.all())

destroyMessages = False
monkeyMode = False
targetMemberId = None

@bot.event
async def on_ready() :
    print(f"Bot {bot.user} ready!")
    
@bot.event
async def on_message(message) :
    await bot.process_commands(message)

    if message.author.id == targetMemberId : 
        if destroyMessages :
            await message.delete()
        elif monkeyMode :
            await message.channel.send(f"{message.author.mention} {randomAnswers()}")

@bot.command(name="мутік")
@commands.has_permissions(administrator=True)
async def spyMute(ctx) :
    global destroyMessages
    await ctx.message.delete()

    if destroyMessages == False :
        destroyMessages = True
        await ctx.send("шпіоньска заглушка була активована", delete_after = 5)
    elif destroyMessages == True :
        destroyMessages = False
        await ctx.send("шпіоньска заглушка була **ДЕ**активована", delete_after = 5)

@bot.command(name="таргет")
@commands.has_permissions(administrator=True)
async def targetId(ctx, command: disnake.Member) :
    await ctx.message.delete()
    global targetMemberId
    targetMemberId = command.id
    await ctx.send(f"таргет було поміняно на `{ctx.guild.get_member(targetMemberId)}`", delete_after = 5)

@bot.command(name="обізянка")
@commands.has_permissions(administrator=True)
async def monkey(ctx) :
    global monkeyMode
    await ctx.message.delete()
    if monkeyMode == False :
        monkeyMode = True
        await ctx.send("Режим обізянки був активований", delete_after = 5)
    elif monkeyMode == True :
        monkeyMode = False
        await ctx.send("Режим обізянки був **ДЕ**активований", delete_after = 5)

@bot.command(name="мусор")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int, member: disnake.Member = None) :
    await ctx.message.delete()

    if amount < 1001 : 
        if member is not None :
            def is_target_member(message):
                return message.author == member if member else True
            await ctx.channel.purge(limit=amount, check=is_target_member)
            await ctx.send(f"Я виніс мусор за **{member}** (**{amount}** сообщеній)", delete_after = 5)
        else:
            await ctx.channel.purge(limit = amount)
            await ctx.send(f"Я виніс мусор (**{amount}** сообщеній)", delete_after = 5)
    else :
        await ctx.send(f"Ебать ти припух. **{amount}** слішком дохуя, я можу винести тільки до **1000**", delete_after = 5)

@bot.command(name="інфо")
@commands.has_permissions(administrator=True)
async def info(ctx) :
    await ctx.message.delete()
    infoEmbed = disnake.Embed(
        title="Інфо", 
        description=f"Заглушка шпіона: **{enabledProp(destroyMessages)}**\nРежим обізянки: **{enabledProp(monkeyMode)}** \nтаргет: **{getName(ctx.guild.get_member(targetMemberId))}**",
        color=0xbcd9e7
    )
    infoEmbed.add_field(name="Команди ботіка", value="", inline=False)
    infoEmbed.add_field(name="112.таргет @нік", value="міня ціль для хейтінга", inline=False)
    infoEmbed.add_field(name="112.мутік", value="дела так шо у челіка будут удаляться всі сообщенія (скритно)", inline=False)
    infoEmbed.add_field(name="112.обізянка", value="хейт після сообщенія таргета", inline=False)
    infoEmbed.add_field(name="112.інфо", value="інфа по ботіку", inline=False)
    infoEmbed.add_field(name="112.мусор <колічество> <@нік (не обовязково)>", value="удаля задане колічество сообщеній", inline=False)
    infoEmbed.add_field(name="112.фуряшка", value="отправля фуряшку в чатік", inline=False)
    await ctx.send(embed=infoEmbed)

@bot.command(name="фуряшка")
@commands.has_permissions(administrator=True)
async def furryImg(ctx):
    await ctx.message.delete()
    url = getFurryImage()
    await ctx.send(f"{url}")

def randomAnswers() :
    answer = None
    with open("text.txt", encoding="utf-8") as file:
        lines = file.readlines()
        answer = random.choice(lines)
        file.close()
    return answer

def enabledProp(prop) :
    box = None
    if prop :
        box = "✅"
    elif prop != True:
        box = "❌"
    return box

def getName(name) :
    getedName = "Пусто"
    if name != None :
         getedName = name
    return getedName
        
bot.run("")
