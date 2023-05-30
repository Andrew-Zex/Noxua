import disnake
from disnake.ext import commands
import random
import aiohttp
# https://nekobot.xyz/api/image?type={action}
class nswf(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog NSFW - Ready")
    acts = ["hentai", "pussy", "boobs", "yaoi", "hkitsune", "hneko"]
    @commands.slash_command(name="nsfw", description="ONLY FOR NSWF CHANNELS")
    async def nswf(self, inter: disnake.CommandInteraction, action: str = commands.Param(name="действие", description="Выберете действие", choices=acts)):
        if inter.channel.is_nsfw():
            if action == "hentai":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: HENTAI")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
            elif action == "pussy":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: Pussy")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
            elif action == "boobs":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: СИСЬКИ!")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
            elif action == "yaoi":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: Яойчик)")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
            elif action == "hkitsune":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: Хентай Китсунэ<3")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
            elif action == "hneko":
                async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":underage: Неко-тянки!!!")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
        else:
            await inter.response.send_message("Это не NSFW канал")

def setup(bot):
    bot.add_cog(nswf(bot))