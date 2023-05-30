import disnake, aiohttp
from disnake.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Avatar - Ready")

    @commands.slash_command(name="help", description="Список команд")
    async def info(self, inter:disnake.CommandInteraction):
        #await inter.response.send_message(f"Пока не доступно")
        emb = disnake.Embed(title="Список команд")
        emb.add_field(name=':park: Изображения', value='</avatar:1092066730987229224> - `Пока не доступно`\n</image:1091989637171531787> `Изображение` - Показывает случайное изображение\n</nsfw:1092376900107763782> `Действие` - Немного хорни в боте))', inline=False)
        emb.add_field(name=':sunglasses: РП', value='</action:1091291219180670986> `Действие(Обязательно)` `Пользователь(Необязательно)` - Покажите ваши эмоции)', inline=False)
        emb.add_field(name=':pencil:  Информация', value='</help:1097846718311190528> - Список команд\n</info:1092059808745656370> `информация` - показывает информацию о боте/сервере', inline=False)
        emb.add_field(name=':tools: Прочее', value='</ipv4:1093257851520168037> - Случайный IP адрес\n</ipv6:1093257851520168038> - Случайный IPv6 адрес\n</math:1093257851520168036> `INT1` `действие` `INT2` - Математические действия\n</uid:1093257851520168039> - случайный Уникальный идентификатор(uID)', inline=False)
        await inter.response.send_message(embed=emb)
def setup(bot):
    bot.add_cog(help(bot))