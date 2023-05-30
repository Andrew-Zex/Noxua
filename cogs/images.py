import disnake, aiohttp
from disnake.ext import commands
from translate import Translator

class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Images - Ready")


    imgs = ["neko", "waifu", "holo", "fox", "cat", "bird", "dog","panda"]
    @commands.slash_command(name="image", description="Случайные картинки")
    async def img(self, inter: disnake.CommandInteraction, action: str = commands.Param(name="картинка", description="Выберете картинку", choices=imgs)):
        if action == "neko":
            async with aiohttp.request("GET", f'https://api.waifu.pics/sfw/{action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":cat: Nyaa!")
                    emb.set_image(url=hent["url"])
                    await inter.response.send_message(embed=emb)
        elif action == "waifu":
            async with aiohttp.request("GET", f'https://api.waifu.pics/sfw/{action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":heart: Вайфочка<3")
                    emb.set_image(url=hent["url"])
                    await inter.response.send_message(embed=emb)
        elif action == "holo":
            async with aiohttp.request("GET", f'https://nekobot.xyz/api/image?type={action}') as resp:
                    hent = await resp.json()
                    emb = disnake.Embed(title=":wolf: Какая красота<3")
                    emb.set_image(url=hent["message"])
                    await inter.response.send_message(embed=emb)
        elif action == "fox":
            async with aiohttp.request("GET", f'https://some-random-api.ml/animal/{action}') as resp:
                    hent = await resp.json()
                    translator= Translator(to_lang="ru")
                    translation = translator.translate(f'{hent["fact"]}')
                    emb = disnake.Embed(title=":fox: Фыр-Фыр)")
                    emb.set_image(url=hent["image"])
                    emb.set_footer(text=f"Факт: {translation}")
                    await inter.response.send_message(embed=emb)
        elif action == "cat":
            async with aiohttp.request("GET", f'https://some-random-api.ml/animal/{action}') as resp:
                    hent = await resp.json()
                    translator= Translator(to_lang="ru")
                    translation = translator.translate(f'{hent["fact"]}')
                    emb = disnake.Embed(title=":cat: Мяяяяу)")
                    emb.set_image(url=hent["image"])
                    emb.set_footer(text=f"Факт: {translation}")
                    await inter.response.send_message(embed=emb)
        elif action == "bird":
            async with aiohttp.request("GET", f'https://some-random-api.ml/animal/{action}') as resp:
                    hent = await resp.json()
                    translator= Translator(to_lang="ru")
                    translation = translator.translate(f'{hent["fact"]}')
                    emb = disnake.Embed(title=":bird: Чик-Чирик)")
                    emb.set_image(url=hent["image"])
                    emb.set_footer(text=f"Факт: {translation}")
                    await inter.response.send_message(embed=emb)
        elif action == "dog":
            async with aiohttp.request("GET", f'https://some-random-api.ml/animal/{action}') as resp:
                    hent = await resp.json()
                    translator= Translator(to_lang="ru")
                    translation = translator.translate(f'{hent["fact"]}')
                    emb = disnake.Embed(title=":dog: ГАВ!")
                    emb.set_image(url=hent["image"])
                    emb.set_footer(text=f"Факт: {translation}")
                    await inter.response.send_message(embed=emb)
        elif action == "panda":
            async with aiohttp.request("GET", f'https://some-random-api.ml/animal/{action}') as resp:
                    hent = await resp.json()
                    translator= Translator(to_lang="ru")
                    translation = translator.translate(f'{hent["fact"]}')
                    emb = disnake.Embed(title=":panda_face: Милотаааа!")
                    emb.set_image(url=hent["image"])
                    emb.set_footer(text=f"Факт: {translation}")
                    await inter.response.send_message(embed=emb)

def setup(bot):
    bot.add_cog(images(bot))