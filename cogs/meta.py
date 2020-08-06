import discord
from discord.ext import commands


class Meta(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        emb1 = discord.Embed(
            description="**Reaction Poll**\nCreate a reaction poll by typing `+poll *your message*`. "
            + "Poll Bot will automatically add the reactions 👍, 👎, and 🤷."
            + "\nCreate a reaction poll with multiple options by typing `+poll {title} [Option1] [Option2] [Option3]`."
            + "\n\n**Strawpoll**\nCreate a strawpoll by typing `+strawpoll {title} [Option1] [Option2] [Option 3]`, with up to 30 options."
            + "\n\n"
            + "But really nobody can help you.",
            colour=0x83BAE3,
        )
        await ctx.message.channel.send(embed=emb1)

    # @commands.command(name="donate")
    # async def donate(self, ctx):
    #     emb1 = discord.Embed(
    #         description="**Donate**\nThank you for considering donating to Poll Bot. Your donation will help pay for the monthly server costs.\n\n"
    #                     + "Donation Platforms:\n"
    #                     + "Patreon: https://www.patreon.com/pollbot\n"
    #                     + "Ko-Fi (one-time paypal donations): https://ko-fi.com/pollbot\n"
    #                     + "Bitcoin Address: 3EPBikSQ9MTsHrnowLvPfe83uYZ4bFvohM\n"
    #                     + "Bitcoin (via Lightning Network): https://tippin.me/@stayingqold\n"
    #                     + "Ether: 0x00C78c405B21c120c921991906A61A52A1D1DC71",
    #         colour=0x83BAE3,
    #     )
    #     await ctx.message.channel.send(embed=emb1)

    # @commands.command(name="invite")
    # async def invite(self, ctx):
    #     emb1 = discord.Embed(
    #         description="Invite Poll Bot to your server: <https://discordapp.com/oauth2/authorize?client_id=298673420181438465&scope=bot&permissions=0>",
    #         colour=0x83BAE3,
    #     )
    #     await ctx.message.channel.send(embed=emb1)

    # @commands.command(name="updates")
    # async def updates(self, ctx):
    #     emb1 = discord.Embed(
    #         description="**Please join the Poll Bot server and see #announcements to see the latest updates! <https://discord.gg/FhT6nUn>**"
    #     )
    #     await ctx.message.channel.send(embed=emb1)

    @commands.command(name="support_info")
    async def support_info(self, ctx):
        # the bot user in the guild the message was sent in
        me = ctx.guild.me

        # getting info about the Poll Bot's roles
        roles = me.roles
        top_role = me.top_role

        # getting the bots channel permissions
        # only checking for the ones Poll Bot needs:
        # read messages, send messages, add reactions, embed links, read message history
        # and admin perm (though admin is not necessary)
        channel_perms = me.permissions_in(ctx.channel)
        shard_id = str(ctx.guild.shard_id)

        desc = "**Support Info**\n\n" + "**Permissions**\n" + "Admin: " + str(channel_perms.administrator) + "\nRead Messages: " + str(channel_perms.read_messages) + "\nSend Messages: " + str(channel_perms.send_messages) + "\nAdd Reactions: " + str(channel_perms.add_reactions) +  "\nEmbed Links: " + str(channel_perms.embed_links) + "\nRead Message History: " + str(channel_perms.read_message_history) + "\n\n" + "**Other**\n" + "Shard ID: " + str(ctx.guild.shard_id)

        await ctx.message.channel.send(desc)



def setup(bot):
    bot.add_cog(Meta(bot))
