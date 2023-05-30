import disnake
from disnake.ext import commands
import os
from config import settings
import typing

class PersistentViewBot(commands.Bot): 
    def __init__(self): 
        super().__init__(command_prefix=settings['prefix'], intents=disnake.Intents().all(), activity=disnake.Game(name="Эмоции))")) 
        self.persistent_views_added = False
    async def on_ready(self):
        if not self.persistent_views_added:
            
            self.persistent_views_added = True
        print(f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nБот запущен\nName: {bot.user.name}#{bot.user.discriminator}\nID: {bot.user.id}\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

bot = PersistentViewBot()

list_cogs = []
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension("cogs." + filename[:-3])
        list_cogs.append(filename[:-3])

@bot.slash_command(description='Загрузить модуль бота')
async def load(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля")):
    if inter.author.id in settings["owners"]:
        bot.load_extension(f"cogs.{module}")
        await inter.response.send_message(f"Загружен модуль `{module}`",ephemeral=True)
    else:
        await inter.response.send_message(f"Нельзя загружать модули администраторам",ephemeral=True)

@bot.slash_command(description='Выгрузить модуль бота')
async def unload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля", choices=list_cogs)):
    if inter.author.id in settings["owners"]:
        bot.unload_extension(f"cogs.{module}")
        await inter.response.send_message(f"Выгружен модуль `{module}`",ephemeral=True)
    else:
        await inter.response.send_message(f"Вы не можете выгружать этот модуль",ephemeral=True)
    
@bot.slash_command(description="Перезагрузить модуль бота")
async def reload(inter: disnake.CommandInteraction, module: str = commands.Param(name="module", description="Название модуля", choices=list_cogs)):
    if inter.author.id in settings["owners"]:
        bot.reload_extension(f"cogs.{module}")
        await inter.response.send_message(f"Перезагружен модуль `{module}`",ephemeral=True)
    else:
        await inter.response.send_message(f"Нельзя перезагружать модуль `{module}`",ephemeral=True)

bot.run(settings["token"])