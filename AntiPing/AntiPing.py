from discord.ext import commands
import discord
import itertools
import datetime

def iter_all_mentions(message):
    return itertools.chain(message.mentions, message.channel_mentions, message.role_mentions)

class AntiPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        text = message.content
        message.channel.send("A message was sent.")
        for i, mentioned in enumerate(iter_all_mentions(message)):
            message.channel.send("Iteration Worked.")
            allowed_roles = {1089165585214087270, 1010144986806878290, 1000701304110338170, 1032993373470085160, 1070260250709590057}
            if mentioned.id == 746966989347618858: #and not any(role.id in allowed_roles for role in message.author.roles)
                message.channel.send("Send Embed")
                DateTime = datetime.datetime.now()
                embed = discord.Embed(
                    title="Please refrain from pinging the Founder",
                    description="We do not allow you to ping our Founder at this time. For support, please send a Direct Message to <@1009340261282889729>. Multiple pings to the Founder may result in further moderation action taken.",
                    color=0xffe1b4
                )
                embed.set_footer(text=f"Pleasant Support • Pleasant Corporation • Today at {DateTime.strftime('%x %H:%M')}")
                embed.set_image(url="https://tenor.com/en-GB/view/discord-reply-discord-reply-off-discord-reply-gif-22150762")
                await message.channel.send(embed=embed)

async def setup(bot):
    bot.add_cog(AntiPing(bot))
