import discord
from discord.ext import commands
import sys
sys.path.append('/app/modules')
import username601 as myself
from username601 import *
from datetime import datetime as t

class bothelp(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx, *args):
        data = myself.jsonisp("https://vierofernando.github.io/username601/assets/json/commands.json")
        types = Config.cmdtypes
        args = list(args)
        if len(args)<1:
            cate = ''
            for i in range(0, len(types)):
                cate += f'**{str(i+1)}. **{Config.prefix}help {str(types[i])}\n'
            embed = discord.Embed(
                title='Username601\'s commands',
                description='INFO: Bot is currently being rewritten. Most commands won\'t respond yet. Sorry for the inconvenience!\n[Join the support server]('+str(Config.SupportServer.invite)+') | [Vote us on top.gg](https://top.gg/bot/'+str(Config.id)+'/vote)\n\n**[More information on our website here.](https://vierofernando.github.io/username601/commands)**\n**Command Categories:** \n'+str(cate),
                colour=discord.Colour.from_rgb(201, 160, 112)
            )
            embed.set_footer(text=f'Type {Config.prefix}help <command/category> for more details.')
            await ctx.send(embed=embed)
        else:
            source = None
            typ = ''
            category_name = None
            query = ' '.join(list(args))
            for i in range(0, len(types)):
                if query==types[i].lower():
                    source = data[i][types[i]]
                    typ = 'Category'
                    category_name = types[i]
                    break
            if source==None:
                for i in range(0, len(data)):
                    for j in range(0, len(data[i][types[i]])):
                        if query==data[i][types[i]][j]['n'].lower():
                            source = data[i][types[i]][j]
                            typ = 'Command'
                            break
                    if not typ=='':
                        break
            if source==None:
                await ctx.send('Oops... Your command doesn\'t seem to exist.')
            else:
                if typ=='Category':
                    cmds = []
                    for i in range(0, len(source)):
                        cmds.append(source[i]['n'])
                    cmds = myself.dearray(cmds)
                    embed = discord.Embed(title='Category help for '+str(category_name)+':', description='**Commands:** \n```'+str(cmds)+'```', colour=discord.Colour.from_rgb(201, 160, 112))
                if typ=='Command':
                    parameters = 'No parameters required.'
                    if len(source['p'])>0:
                        parameters = ''
                        for i in range(0, len(source['p'])):
                            parameters += '**'+source['p'][i]+'**\n'
                    embed = discord.Embed(title='Command help for '+str(source['n'])+':', description='**Function: **'+str(source['f'])+'\n**Parameters:** \n'+str(parameters), colour=discord.Colour.from_rgb(201, 160, 112))
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def vote(self, ctx):
        embed = discord.Embed(title='Support by Voting us at top.gg!', description='Sure thing, mate! [Vote us at top.gg by clicking me!](https://top.gg/bot/'+str(Config.id)+'/vote)', colour=discord.Colour.from_rgb(201, 160, 112))
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def github(self, ctx):
        embed = discord.Embed(title="Click me to visit the Bot's github page.", colour=discord.Colour.from_rgb(201, 160, 112), url='https://github.com/vierofernando/username601')
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True, aliases=['inviteme', 'invitelink', 'botinvite', 'invitebot', 'addtoserver', 'addbot'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(
            title='Sure thing! Invite this bot to your server by clicking me.',
            description='[Invite link](https://discord.com/api/oauth2/authorize?client_id='+str(Config.id)+'&permissions=8&scope=bot) | [Support Server]('+str(Config.SupportServer.invite)+')',
            colour=discord.Colour.from_rgb(201, 160, 112)
        )
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True, aliases=['report', 'suggest'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def feedback(self, ctx, *args):
        if len(list(args))==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Where\'s the feedback? :(')
        elif len(list(args))>1000:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | That\'s too long! Please provide a simpler description.')
        elif 'discord.gg/' in ' '.join(list(args)):
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Do NOT send discord invites through feedback! Use the advertising channel in our support server instead!')
        else:
            wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... Transmitting data to owner...')
            bans, banned = [], False
            async for messages in self.client.get_channel(706459051034279956).history():
                if messages.content.startswith('Banned user with ID of: ['): bans.append(messages.content)
            if len(bans)>0:
                for i in bans:
                    if int(ctx.message.author.id)==int(i.split('[')[1].split(']')[0]):
                        await wait.edit(content='', embed=discord.Embed(title='You are banned', description='Sorry! you are banned from using the `'+prefix+'feedback` command. Reason:```'+i.split('REASON:"')[1].split('"')[0]+'```', colour=discord.Colour.from_rgb(201, 160, 112)))
                        banned = True
                        break
            if not banned:
                try:
                    fb = ' '.join(list(args))
                    feedbackCh = self.client.get_channel(Config.SupportServer.feedback)
                    await feedbackCh.send('<@Config.owner.id>, User with ID: '+str(ctx.message.author.id)+' sent a feedback: **"'+str(fb)+'"**')
                    embed = discord.Embed(title='Feedback Successful', description=str(client.get_emoji(BotEmotes.success)) + '** | Success!**\nThanks for the feedback!\n**We will DM you as the response. **If you are unsatisfied, [Join our support server and give us more details.]('+str(Config.SupportServer.invite)+')',colour=discord.Colour.from_rgb(201, 160, 112))
                    await wait.edit(content='', embed=embed)
                except:
                    await wait.edit(content=str(self.client.get_emoji(BotEmotes.error)) + ' | Error: There was an error while sending your feedback. Sorry! :(')
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        ping = str(round(self.client.latency*1000))
        embed = discord.Embed(title=f'Pong!', description=f'**Discord\'s Latency:** {ping} ms.\n**Bot\'s Latency:** {str(round(int((t.now()-ctx.message.created_at).microseconds)/1000))} ms.', colour=discord.Colour.from_rgb(201, 160, 112))
        embed.set_thumbnail(url='https://i.pinimg.com/originals/21/02/a1/2102a19ea556e1d1c54f40a3eda0d775.gif')
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def uptime(self, ctx):
        embed = discord.Embed(title='My uptime: {}'.format(str(myself.terminal('uptime -p'))[3:]), color=discord.Colour.from_rgb(201, 160, 112))
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def about(self, ctx):
        if str(self.client.get_guild(Config.SupportServer.id).get_member(Config.owner.id).status)=='offline': devstatus = 'Offline'
        else: devstatus = 'Online'
        embed = discord.Embed(title = 'About '+str(ctx.message.guild.get_member(Config.id).display_name), colour = discord.Colour.from_rgb(201, 160, 112))
        embed.description = 'NOTE: Bot is currently on reconstruction. The only functioning commands now are 75% from all commands. The dev will fix/add as fast as he can. Sorry!'
        embed.add_field(name='Bot general Info', value='**Bot name: ** Username601\n**Library: **Discord.py\n**Default Config.prefix: ** 1', inline='True')
        embed.add_field(name='Programmer info', value='**Programmed by: **'+Config.owner.name+'. ('+self.client.get_user(Config.owner.id).name+'#'+str(self.client.get_user(Config.owner.id).discriminator)+')\n**Current Discord Status:** '+devstatus, inline='True')
        embed.add_field(name='Version Info', value='**Bot version: ** '+Config.Version.number+'\n**Changelog: **'+Config.Version.changelog)#+'\n'+str(osinfo))
        embed.add_field(name='Links', value='[Invite this bot to your server!](http://vierofernando.github.io/programs/username601)\n[The support server!]('+str(Config.SupportServer.invite)+')\n[Vote us on top.gg](https://top.gg/bot/'+str(Config.id)+'/vote)\n[Official Website](https://vierofernando.github.io/username601)', inline='False')
        embed.set_thumbnail(url='https://raw.githubusercontent.com/vierofernando/username601/master/assets/pics/pfp.png')
        embed.set_footer(text='© Viero Fernando Programming, 2018-2020. All rights reserved.')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(bothelp(client))
