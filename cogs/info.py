import disnake, aiohttp
from disnake.ext import commands
from config import settings
import os, psutil, time, platform, cpuinfo

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Info - Ready")

    infos = ["bot", "server"]
    @commands.slash_command(name="info", description="Получите информацию о Сервере/Боте")
    async def info(self, inter:disnake.CommandInteraction, action: str = commands.Param(name="информация", description="Какую информацию вы хотите получить?", choices=infos)):
        if action == "bot":
            #await inter.response.send_message(f"команда `{action}` пока не доступна")
            emb = disnake.Embed(title="__**Информация**__:")
            emb.add_field(name='<:memory:1095338273011941496> Использование ОЗУ', value=f'`{round(psutil.virtual_memory().used/1024/1024)}MB/{round(psutil.virtual_memory().total/1024/1024)}MB`', inline=False)
            emb.add_field(name="📁 Пользователей", value=f'`{len(inter.bot.users)} Пользователей`', inline=True)
            emb.add_field(name="📁 Серверов", value=f'`{len(inter.bot.guilds)} Серверов`', inline=True)
            emb.add_field(name="📁 Каналов", value=f'`{len(inter.bot.guilds)} Каналов`', inline=True)
            emb.add_field(name="<:disnake:1095338426695426080> Версия Disnake", value=f"`v{disnake.__version__}`", inline=True)
            emb.add_field(name="<:python:1095338334974398626> Версия Python", value=f"`v{platform.python_version()}`", inline=True)
            emb.add_field(name=":page_facing_up: Версия Бота", value=f"`v{settings['version']}`", inline=True)
            emb.add_field(name="<:cpu:1095338212207120484> CPU:", value=f"- 📚 Модель: `{cpuinfo.get_cpu_info()['brand_raw']}`\n- 📚 Ядер: `{psutil.cpu_count()}`\n- 🔥 Нагрузка: `{psutil.cpu_percent()}%`\n")
            await inter.response.send_message(embed=emb)
        elif action == "server":
            member_count = len(inter.guild.members)
            true_member_count = len([m for m in inter.guild.members if not m.bot])
            emb = disnake.Embed(title=f"Информация о {inter.guild.name}")
            emb.add_field(name="Владелец", value=f'<@{inter.guild.owner_id}>')
            emb.add_field(name="<:role:1095424900501602434> Ролей", value=f"`{inter.guild.roles.__len__()} Ролей`")
            emb.add_field(name="<:human_1:1095419984047521973> Участников", value=f"- <:human_2:1095420050372051075> Всего: `{member_count} Участников`\n- <:human_1:1095419984047521973> Людей: `{true_member_count} Человек`\n- <:bot:1095420133192769646> Ботов: `{member_count - true_member_count} Ботов`", inline=False)
            emb.set_footer(text=f"ID: {inter.guild.id} | Дата создания: {inter.guild.created_at.date()}")
            emb.add_field(name="<:channel:1095424330730569908> Каналов", value=f'- <:channel:1095424330730569908> Текстовых: {inter.guild.text_channels.__len__()}\n- <:voice:1095424825327095898> Голосовых: {inter.guild.voice_channels.__len__()}\n- <:forum:1095424427061162024> Форумов: {inter.guild.forum_channels.__len__()}\n- <:stage:1096484386444169277> Трибун: {inter.guild.stage_channels.__len__()}')
            emb.set_thumbnail(url=f"{inter.guild.icon.url}")
            await inter.response.send_message(embed=emb)
def setup(bot):
    bot.add_cog(info(bot))