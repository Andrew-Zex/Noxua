import disnake
from disnake.ext import commands
import aiohttp
import random

list_hug = [
    "Объятия это так мило<3",
    "Вай, милота))"
]
l1 = random.choice(list_hug)
list_kiss = [
    "Поцелуй? Вааау!",
    "Хочу ещё поцелуйчик)"
]
l2 = random.choice(list_kiss)
list_pat = [
    "Приятно, когда тебя гладят)",
    "Главное не вгладить..."
]
l3 = random.choice(list_pat)
list_feed = [
    "Ммм, вкусно)",
    "Вай) кормят с ложечки))"
]
l4 = random.choice(list_feed)
list_smug = [
    "Самодовольно)",
    "Хехе)"
]
l5 = random.choice(list_smug)
list_slap = [
    "Вот тебе, гад!",
    "Это должно быть больно..."
]
l6 = random.choice(list_slap)
list_poke = [
    "ой, ай)",
    "Прекратиии, щекотно же))"
]
l7 = random.choice(list_poke)
list_blush = [
    "ой, ой...",
    "блииин... не смущааай..."
]
l8 = random.choice(list_blush)
list_cry = [
    "обидно же...",
    "ты заставил меня плакать..."
]
l9 = random.choice(list_cry)
list_kill = [
    "Цель устранена!",
    "уничтожение не избежно!"
]
l10 = random.choice(list_kill)

class emote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Emote - Ready")
    
    acts = ["hug", "kiss", "pat", "feed", "smug", "slap", "poke", "blush", "cry", "kill"]
    @commands.slash_command(name="action", description="Вы можете что-то сделать с человеком;)")
    async def help_command(self, inter: disnake.CommandInteraction, action: str = commands.Param(name="действие", description="Выберете действие", choices=acts), target: disnake.Member = commands.Param(default=None, name="пользователь", description="Выберите пользователя")):
        try:
            if target is inter.author:
                if action == "hug":
                        async with aiohttp.request("GET", "https://nekos.life/api/v2/img/hug") as resp:
                            hug = await resp.json()
                            emb = disnake.Embed(title=":relieved: Обнимашкиии!", description=f'{inter.author.mention} обнимает себя!!')
                            emb.set_image(hug["url"])
                            emb.set_footer(text=l1)
                            await inter.response.send_message(embed=emb)
                elif action == "kiss":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/kiss") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":kissing_heart: Поцелуйчики<3", description=f'{inter.author.mention} целует себя!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l2)
                        await inter.response.send_message(embed=emb)
                elif action == "pat":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/pat") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":relaxed: Поглаживание)", description=f'{inter.author.mention} гладит себя!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l3)
                        await inter.response.send_message(embed=emb)
                elif action == "feed":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/feed") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":drooling_face: ЕДАААА!)", description=f'{inter.author.mention} кушает!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l4)
                        await inter.response.send_message(embed=emb)
                elif action == "smug":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/smug") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sunglasses: Хихихи)", description=f'{inter.author.mention} доволен собой)')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l5)
                        await inter.response.send_message(embed=emb)
                elif action == "slap":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/slap") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":anger: Хтыщь-Хтыщь!", description=f'{inter.author.mention} бьёт себя(')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l6)
                        await inter.response.send_message(embed=emb)
                elif action == "poke":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/poke") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":point_right: Тык-Тык!", description=f'{inter.author.mention} тыкает себя))')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l7)
                        await inter.response.send_message(embed=emb)
                elif action == "blush":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/blush") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":flushed: ой!", description=f'{inter.author.mention} смущается...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l8)
                        await inter.response.send_message(embed=emb)
                elif action == "cry":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/cry") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sob: Хнык-Хнык!", description=f'{inter.author.mention} плачет...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l9)
                        await inter.response.send_message(embed=emb)
                elif action == "kill":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/kill") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":skull_crossbones: СМЭРТЬ!", description=f'{inter.author.mention} самовыпилился...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l10)
                        await inter.response.send_message(embed=emb)

            elif target is None:
                if action == "hug":
                        async with aiohttp.request("GET", "https://nekos.life/api/v2/img/hug") as resp:
                            hug = await resp.json()
                            emb = disnake.Embed(title=":relieved: Обнимашкиии!", description=f'{inter.author.mention} обнимает Всех!!')
                            emb.set_image(hug["url"])
                            emb.set_footer(text=l1)
                            await inter.response.send_message(embed=emb)
                elif action == "kiss":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/kiss") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":kissing_heart: Поцелуйчики<3", description=f'{inter.author.mention} целует Всех!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l2)
                        await inter.response.send_message(embed=emb)
                elif action == "pat":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/pat") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":relaxed: Поглаживание)", description=f'{inter.author.mention} гладит Всех!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l3)
                        await inter.response.send_message(embed=emb)
                elif action == "feed":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/feed") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":drooling_face: ЕДАААА!)", description=f'{inter.author.mention} кормит Всех!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l4)
                        await inter.response.send_message(embed=emb)
                elif action == "smug":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/smug") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sunglasses: Хихихи)", description=f'{inter.author.mention} Доволен Всеми)')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l5)
                        await inter.response.send_message(embed=emb)
                elif action == "slap":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/slap") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":anger: Хтыщь-Хтыщь!", description=f'{inter.author.mention} бьёт Всех(')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l6)
                        await inter.response.send_message(embed=emb)
                elif action == "poke":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/poke") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":point_right: Тык-Тык!", description=f'{inter.author.mention} тыкает Всех))')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l7)
                        await inter.response.send_message(embed=emb)
                elif action == "blush":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/blush") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":flushed: ой!", description=f'{inter.author.mention} кто-то смущает...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l8)
                        await inter.response.send_message(embed=emb)
                elif action == "cry":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/cry") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sob: Хнык-Хнык!", description=f'{inter.author.mention} плачет из-за кого-то...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l9)
                        await inter.response.send_message(embed=emb)
                elif action == "kill":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/kill") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":skull_crossbones: СМЭРТЬ!", description=f'{inter.author.mention} мёртв...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l10)
                        await inter.response.send_message(embed=emb)

            else:
                if action == "hug":
                        async with aiohttp.request("GET", "https://nekos.life/api/v2/img/hug") as resp:
                            hug = await resp.json()
                            emb = disnake.Embed(title=":relieved: Обнимашкиии!", description=f'{inter.author.mention} обнимает {target.mention}!!')
                            emb.set_image(hug["url"])
                            emb.set_footer(text=l1)
                            await inter.response.send_message(embed=emb)
                elif action == "kiss":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/kiss") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":kissing_heart: Поцелуйчики<3", description=f'{inter.author.mention} целует {target.mention}!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l2)
                        await inter.response.send_message(embed=emb)
                elif action == "pat":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/pat") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":relaxed: Поглаживание)", description=f'{inter.author.mention} гладит {target.mention}!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l3)
                        await inter.response.send_message(embed=emb)
                elif action == "feed":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/feed") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":drooling_face: ЕДАААА!)", description=f'{inter.author.mention} кормит {target.mention}!!')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l4)
                        await inter.response.send_message(embed=emb)
                elif action == "smug":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/smug") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sunglasses: Хихихи)", description=f'{inter.author.mention} доволен {target.mention})')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l5)
                        await inter.response.send_message(embed=emb)
                elif action == "slap":
                    async with aiohttp.request("GET", "https://nekos.life/api/v2/img/slap") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":anger: Хтыщь-Хтыщь!", description=f'{inter.author.mention} бьёт {target.mention}(')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l6)
                        await inter.response.send_message(embed=emb)
                elif action == "poke":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/poke") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":point_right: Тык-Тык!", description=f'{inter.author.mention} тыкает {target.mention}))')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l7)
                        await inter.response.send_message(embed=emb)
                elif action == "blush":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/blush") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":flushed: ой!", description=f'{inter.author.mention} смущает {target.mention}...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l8)
                        await inter.response.send_message(embed=emb)
                elif action == "cry":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/cry") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":sob: Хнык-Хнык!", description=f'{inter.author.mention} плачет из-за {target.mention}...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l9)
                        await inter.response.send_message(embed=emb)
                elif action == "kill":
                    async with aiohttp.request("GET", "https://api.waifu.pics/sfw/kill") as resp:
                        hug = await resp.json()
                        emb = disnake.Embed(title=":skull_crossbones: СМЭРТЬ!", description=f'{inter.author.mention} убил {target.mention}...')
                        emb.set_image(hug["url"])
                        emb.set_footer(text=l10)
                        await inter.response.send_message(embed=emb)

        except Exception as e:
            print(e)

def setup(bot):
    bot.add_cog(emote(bot))