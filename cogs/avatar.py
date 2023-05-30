import disnake, aiohttp
from disnake.ext import commands

class ava(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Avatar - Ready")

    infos = ["triggered", "jail", "glass", "rainbow"]
    @commands.slash_command(name="avatar", description="Получите информацию о Сервере/Боте")
    async def info(self, inter:disnake.CommandInteraction, action: str = commands.Param(name="действие", description="Какое действие с аватаром вы хотите сделать?", choices=infos)):
        if action == "triggered":
            await inter.response.send_message(f"команда `{action}` пока не доступна")
        elif action == "jail":
            await inter.response.send_message(f"команда `{action}` пока не доступна")
        elif action == "glass":
            await inter.response.send_message(f"команда `{action}` пока не доступна")
def setup(bot):
    bot.add_cog(ava(bot))