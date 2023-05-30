import disnake
from disnake.ext import commands
import random

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog Math - Ready")

    maths = [
        "делить", "умножить", "сложить", "вычесть", "степень"
    ]
    @commands.slash_command(name="math", description="Математическое действие")
    async def math(self, inter: disnake.CommandInteraction, num1: int = commands.Param(name="первое_число", description="введите сюда число"),  act: str = commands.Param(name="действие", description="Выберете действие", choices=maths), num2: int = commands.Param(name="второе_число", description="введите сюда число")):
        try:
            if act == "делить":
                await inter.response.send_message(f"`{num1}/{num2}={num1/num2}`")
            elif act == "умножить":
                await inter.response.send_message(f"`{num1}*{num2}={num1*num2}`")
            elif act == "сложить":
                await inter.response.send_message(f"`{num1}+{num2}={num1+num2}`")
            elif act == "вычесть":
                await inter.response.send_message(f"`{num1}-{num2}={num1-num2}`")
            elif act == "степень":
                await inter.response.send_message(f"`{num1}^{num2}={num1**num2}`")
            else:
                await inter.reply("Неизвестное действие")
        except Exception as e:
            print(e)

    @commands.slash_command(name="ipv4", description="Случайный ip адрес")
    async def randIP(self, inter:disnake.CommandInteraction):
        await inter.response.send_message(f"`{'.'.join(str(random.randint(1, 255)) for _ in range(4))}`")

    #random ipv6 adress
    @commands.slash_command(name="ipv6", description="Случайный ipv6 адрес")
    async def randIPv6(self, inter:disnake.CommandInteraction):
        await inter.response.send_message(f"`{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}:{''.join(random.choice('0123456789abcdef') for _ in range(4))}`")

    #random uid
    @commands.slash_command(name="uid", description="Случайный uid")
    async def randUID(self, inter:disnake.CommandInteraction):
        await inter.response.send_message(f"`{''.join(random.choice('0123456789abcdef') for _ in range(8))}-{''.join(random.choice('0123456789abcdef') for _ in range(4))}-{''.join(random.choice('0123456789abcdef') for _ in range(4))}-{''.join(random.choice('0123456789abcdef') for _ in range(4))}-{''.join(random.choice('0123456789abcdef') for _ in range(12))}`")


def setup(bot):
    bot.add_cog(math(bot))