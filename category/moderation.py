import discord
from discord.ext import commands
import sys
import random
import asyncio
sys.path.append('/app/modules')
from username601 import *
import canvas as Painter
import username601 as myself

class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def rolecolor(self, ctx, *args):
        unprefixed = ' '.join(list(args))
        if len(unprefixed.split('#'))==1:
            await ctx.send(f'Please provide a hex!\nExample: {Config.prefix}rolecolor {random.choice(ctx.message.guild.roles).name} #ff0000')
        else:
            if ctx.message.author.guild_permissions.manage_roles==False:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | You need the `MANAGE ROLES` permission to change role colors!')
            else:
                role = None
                for i in ctx.message.guild.roles:
                    if unprefixed.split('#')[0][:-1].lower()==str(i.name).lower():
                        print(unprefixed.split('#')[0][:-1].lower())
                        role = i
                        break
                if role==None:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | Invalid role input! :(')
                else:
                    try:
                        colint = myself.toint(unprefixed.split('#')[1].lower())
                        await role.edit(colour=discord.Colour(colint))
                        await ctx.send('Color of '+role.name+' role has been changed.', delete_after=5)
                    except Exception as e:
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error)) + f' | An error occured while editing role:```{e}```')
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def slowmode(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | How long in seconds?")
        else:
            cd = list(args)[0]
            if ctx.message.author.guild_permissions.manage_channels:
                if not cd.isnumeric():
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | That cooldown is not a number!s")
                else:
                    if int(cd)<0:
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Minus slowmode? Did you mean slowmode 0 seconds?")
                    elif int(cd)>21600:
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | That is too hecking sloow....")
                    else:
                        await ctx.message.channel.edit(slowmode_delay=cd)
                        await ctx.send(str(self.client.get_emoji(BotEmotes.success))+" | Channel slowmode cooldown has been set to "+myself.time_encode(int(cd)))
            else: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | You need the manage channels permission to do this command!")

    @commands.command(pass_context=True, aliases=['addrole', 'add-role'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ar(self, ctx, *args):
        args = list(args)
        if not ctx.message.author.guild_permissions.manage_roles:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | <@{str(ctx.message.author.id)}>, you don\'t have the `Manage Roles` permission!')
        else:
            try:
                toadd = None
                if '<@&' in ''.join(args):
                    toadd = ctx.message.guild.get_role(int(''.join(args).split('<@&')[1].split('>')[0]))
                else:
                    for i in ctx.message.guild.roles:
                        if str(i.name).lower()==str(ctx.message.content).split('> ')[1].lower():
                            toadd = ctx.message.guild.get_role(i.id)
                            break
                if toadd==None:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid input!")
                else:
                    aruser = ctx.message.mentions[0]
                    await aruser.add_roles(toadd)
                    await ctx.send('Congratulations, '+aruser.name+', you now have the '+toadd.name+' role! :tada:')
            except IndexError:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid arguments!")
    
    @commands.command(pass_context=True, aliases=['removerole', 'remove-role'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def rr(self, ctx, *args):
        args = list(args)
        if not ctx.message.author.guild_permissions.manage_roles:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | <@{str(ctx.message.author.id)}>, you don\'t have the `Manage Roles` permission!')
        else:
            try:
                toadd = None
                if '<@&' in ''.join(args):
                    toadd = ctx.message.guild.get_role(int(''.join(args).split('<@&')[1].split('>')[0]))
                else:
                    for i in ctx.message.guild.roles:
                        if str(i.name).lower()==str(ctx.message.content).split('> ')[1].lower():
                            toadd = ctx.message.guild.get_role(i.id)
                            break
                if toadd==None:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid input!")
                else:
                    rruser = ctx.message.mentions[0]
                    await rruser.remove_roles(toadd)
                    await ctx.send(rruser.name+', you lost the '+toadd.name+' role... :pensive:')
            except IndexError:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid arguments!")

    @commands.command(pass_context=True, aliases=['kick'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def ban(self, ctx, *args):
        if len(list(args))==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Nope. No arguments means no moderation:tm:.")
        elif len(ctx.message.mentions)==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Nope. No tagging means no moderation:tm:.")
        else:
            accept = True
            if 'kick' in ctx.message.content:
                if not ctx.message.author.guild_permissions.kick_members:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | No kick members permission?")
                    accept = False
            else:
                if not ctx.message.author.guild_permissions.ban_members:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | No ban members permission?")
                    accept = False
            if ctx.message.mentions[0].guild_permissions.administrator:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Nope, that guy probably has higher permissions than you.")
                accept = False
            elif ctx.message.mentions[0].roles[::-1][0].position>ctx.message.guild.get_member(self.client.user.id).roles[::-1][0].position:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Try moving my role higher than "+ctx.message.mentions[0].name+"'s role.")
            if accept:
                if 'kick' in ctx.message.content:
                    await ctx.message.guild.kick(ctx.message.mentions[0])
                    await ctx.send(str(self.client.get_emoji(BotEmotes.success))+" | Successfully kicked "+ctx.message.mentions[0].name+".")
                else:
                    await ctx.message.guild.ban(ctx.message.mentions[0])
                    await ctx.send(str(self.client.get_emoji(BotEmotes.success))+" | Successfully banned "+ctx.message.mentions[0].name+".")
    @commands.command(pass_context=True, aliases=['purge'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def clear(self, ctx, *args):
        if not ctx.message.author.guild_permissions.manage_channels:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | You need the manage channel permission!")
        else:
            if len(list(args))==0:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | How many messages to be purged?")
            else:
                if len(ctx.message.mentions)==0:
                    if not list(args)[0].isnumeric():
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Not a number!")
                    else:
                        if int(list(args)[0])<0:
                            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Minus?")
                        elif int(list(args)[0])>250:
                            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Too much! Use clone channel instead!")
                        else:
                            topurge = int(list(args)[0])+1
                            await ctx.message.channel.purge(limit=topurge)
                            await ctx.send(str(self.client.get_emoji(BotEmotes.success))+" | Done! {} messages has been cleared!".format(str(list(args)[0])), delete_after=3)
                else:
                    def check(m):
                        return m.author.id == ctx.message.mentions[0].id
                    dels = await ctx.message.channel.purge(check=check, limit=500)
                    await ctx.send(str(self.client.get_emoji(BotEmotes.success))+' | Done. Cleared '+str(len(dels))+' message by <@'+str(ctx.message.mentions[0].id)+'>.', delete_after=3)
    @commands.command(pass_context=True, aliases=['hidechannel'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lockdown(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | Invalid parameters. Correct Example: `{prefix}{args[0][1:]} [disable/enable]`')
        else:
            accept = True
            if not ctx.message.author.guild_permissions.administrator: await ctx.message.channel.send(str(self.client.get_emoji(BotEmotes.error))+' | You need the `Administrator` permission to do this, unless you are trying to mute yourself.')
            else:
                if 'enable' not in args[0].lower():
                    if 'disable' not in args[0].lower():
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Oops! Please type `enable` or `disable`.')
                        accept = False
                if accept:
                    try:
                        if args[0].lower()=='disable':
                            if 'hidechannel' in ctx.message.content: await ctx.message.channel.set_permissions(ctx.message.guild.default_role, read_messages=True)
                            if 'lockdown' in ctx.message.content: await ctx.message.channel.set_permissions(ctx.message.guild.default_role, send_messages=True)
                        elif args[0].lower()=='enable':
                            if 'hidechannel' in ctx.message.content: await ctx.message.channel.set_permissions(ctx.message.guild.default_role, read_messages=False)
                            if 'lockdown' in ctx.message.content: await ctx.message.channel.set_permissions(ctx.message.guild.default_role, send_messages=False)
                        await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +f' | Success! <#{ctx.message.channel.id}>\'s {str(ctx.message.content).split(" ")[0][1:]} has been {args[0]}d!')
                    except Exception as e:
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | For some reason, i cannot change <#{ctx.message.channel.id}>\'s :(\n\n```{e}```')

    @commands.command(pass_context=True, aliases=['serverinfo', 'server', 'servericon'])
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def servercard(self, ctx):
        if 'servericon' in ctx.message.content:
            if ctx.message.guild.is_icon_animated(): link = 'https://cdn.discordapp.com/icons/'+str(ctx.message.guild.id)+'/'+str(ctx.message.guild.icon)+'.gif?size=1024'
            else: link = 'https://cdn.discordapp.com/icons/'+str(ctx.message.guild.id)+'/'+str(ctx.message.guild.icon)+'.png?size=1024'
            theEm = discord.Embed(title=ctx.message.guild.name+'\'s Icon', url=link, colour=discord.Colour.from_rgb(201, 160, 112))
            theEm.set_image(url=link)
            await ctx.send(embed=theEm)
        else:
            humans, bots, online = 0, 0, 0
            for i in ctx.message.guild.members:
                if i.status != 'offline': online += 1
                if i.bot: bots += 1
                if not i.bot: humans += 1
            image = Painter.servercard("./assets/pics/card.jpg", str(ctx.message.guild.icon_url).replace(".webp?size=1024", ".jpg?size=128"), ctx.message.guild.name, str(ctx.message.guild.created_at)[:-7], ctx.message.guild.owner.name, str(humans), str(bots), str(len(ctx.message.guild.channels)), str(len(ctx.message.guild.roles)), str(ctx.message.guild.premium_subscription_count), str(ctx.message.guild.premium_tier), str(online))
            await ctx.send(content='Here is the '+ctx.message.guild.name+'\'s server card.', file=discord.File(image, ctx.message.guild.name+'.png'))
    
    @commands.command(pass_context=True, aliases=['nickname'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nick(self, ctx, *args):
        if len(list(args))<2:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid args!")
        else:
            if not ctx.message.author.guild_permissions.change_nickname:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Invalid permissions! You need the change nickname permission to do this")
            else:
                if len(ctx.message.mentions)==0 or not list(args)[0].startswith('<@'):
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Go mention someone!")
                else:
                    try:
                        newname = ' '.join(list(args)).split('> ')[1]
                        await ctx.message.mentions[0].edit(nick=newname)
                        await ctx.send(str(self.client.get_emoji(BotEmotes.success))+" | Changed the nickname to {}!".format(newname))
                    except:
                        await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Try making my role higher than the person you are looking for!")
def setup(client):
    client.add_cog(moderation(client))