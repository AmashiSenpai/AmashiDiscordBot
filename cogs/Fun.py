
from pycord.discord.ext import commands
import pycord.discord as discord
import requests

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  async def get_insult(self):
    res = requests.get("https://evilinsult.com//generate_insult.php")
    return res.text

  def create_embed(self, title: str, text: str):
    return discord.Embed(
      title=title,
      color=self.color,
      description=text
    )


  @commands.command(name="insult")
  async def insult(self, ctx: commands.Context):
    insult = await self.get_insult()

    await ctx.send(
      embed=self.create_embed("Insult", f"> {insult}")
    )






def setup(bot):
  bot.add_cog(Fun(bot))
