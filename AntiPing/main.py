# main.py
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!")

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		client.load_extension("cogs." + f[:-3])

client.run("token")

# cogs / test.py
from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, client):
		self.client = client # sets the client variable so we can use it in cogs
	
	@commands.Cog.listener()
	async def on_ready(self):
		# an example event with cogs
	
	@commands.command()
	async def command(self, ctx):
		# an example command with cogs

def setup(client):
	client.add_cog(Test(client))
