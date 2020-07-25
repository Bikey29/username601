import discord
from discord.ext import commands
import sys
sys.path.append('/home/runner/hosting601/modules')
import canvas as Painter
from io import BytesIO
import username601 as myself
from username601 import *
from requests import get
from aiohttp import ClientSession

class memes(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = ClientSession()

    @commands.command(pass_context=True, aliases=['lookatthisgraph'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def graph(self, ctx, *args):
        src = str(ctx.author.avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512') if (len(ctx.message.mentions)==0) else str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512')
        async with ctx.message.channel.typing():
            await ctx.send(file=discord.File(Painter.lookatthisgraph(src), 'lookatthisdudelol.png'))
    
    @commands.command(pass_context=True, aliases=['animegif', 'nj'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def nichijou(self, ctx, *args):
        text = 'LAZY PERSON' if (len(list(args))==0) else ' '.join(list(args))
        if len(text) > 22:
            await ctx.send("{} | Text too long ;w;".format(str(self.client.get_emoji(BotEmotes.error))))
            return
        async with ctx.message.channel.typing():
            async with self.session.get("https://i.ode.bz/auto/nichijou?text={}".format(myself.urlify(text))) as r:
                res = await r.read()
                await ctx.send(file=discord.File(fp=BytesIO(res), filename="nichijou.gif"))
    
    @commands.command(pass_context=True, aliases=['ifunny'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wasted(self, ctx):
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)==0: source = ctx.message.author.avatar_url
            else: source = ctx.message.mentions[0].avatar_url
            if 'wasted' in ctx.message.content: data, filename = Painter.wasted(str(source).replace('.webp?size=1024', '.png?size=512')), 'wasted.png'
            else: data, filename = Painter.ifunny(str(source).replace('.webp?size=1024', '.png?size=512')), 'ifunny.png'
            await ctx.send(file=discord.File(data, filename))
    
    @commands.command(pass_context=True, aliases=['achieve', 'call'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def challenge(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | What is the challenge?')
        else:
            async with ctx.message.channel.typing():
                txt = myself.urlify(' '.join(args))
                if 'challenge' in str(ctx.message.content).split(' ')[0][1:]: url='https://api.alexflipnote.dev/challenge?text='+str(txt)
                elif 'call' in str(ctx.message.content).split(' ')[0][1:]: url='https://api.alexflipnote.dev/calling?text='+str(txt)
                else: url='https://api.alexflipnote.dev/achievement?text='+str(txt)
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'minecraft_notice.png'))
    @commands.command(pass_context=True, aliases=['dym'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def didyoumean(self, ctx, *args):
        if list(args)[0]=='help' or len(list(args))==0:
            embed = discord.Embed(title='didyoumean command help', description='Type like the following\n'+prefix+'didyoumean [text1] [text2]\n\nFor example:\n'+prefix+'didyoumean [i am gay] [i am guy]', colour=discord.Colour.from_rgb(201, 160, 112))
            await ctx.send(embed=embed)
        else:
            try:
                async with ctx.message.channel.typing():
                    txt1, txt2 = myself.urlify(str(ctx.message.content).split('[')[1][:-2]), myself.urlify(str(ctx.message.content).split('[')[2][:-1])
                    url='https://api.alexflipnote.dev/didyoumean?top='+str(txt1)+'&bottom='+str(txt2)
                    await ctx.send(file=discord.File(Painter.urltoimage(url), 'didyoumean.png'))
            except IndexError:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | error! invalid args!')
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def drake(self, ctx, *args):
        unprefixed = ' '.join(list(args))
        if list(args)[0]=='help' or len(list(args))==0:
            embed = discord.Embed(
                title='Drake meme helper help',
                description='Type the following:\n`'+str(Config.prefix)+'drake [text1] [text2]`\n\nFor example:\n`'+str(Config.prefix)+'drake [test1] [test2]`'
            )
            await ctx.send(embed=embed)
        else:
            try:
                async with ctx.message.channel.typing():
                    txt1 = myself.urlify(unprefixed.split('[')[1][:-2])
                    txt2 = myself.urlify(unprefixed.split('[')[2][:-1])
                    url='https://api.alexflipnote.dev/drake?top='+str(txt1)+'&bottom='+str(txt2)
                    data = Painter.urltoimage(url)
                    await ctx.send(file=discord.File(data, 'drake.png'))
            except IndexError:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Please send something like {}drake [test 1] [test2]!".format(Config.prefix))
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def salty(self, ctx, *args):
        if len(list(args))!=1:
            await ctx.send(str(client.get_emoji(BotEmotes.error)) + ' | Error! Invalid args.')
        else:
            async with ctx.message.channel.typing():
                av = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp').replace('.webp', '.png')
                url = 'https://api.alexflipnote.dev/salty?image='+str(av)
                data = Painter.urltoimage(url)
                await ctx.send(file=discord.File(data, 'salty.png'))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ifearnoman(self, ctx):
        if len(ctx.message.mentions)==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Gimme some tag!")
        else:
            async with ctx.message.channel.typing():
                source, by = str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.png?size=512'), str(ctx.message.author.avatar_url).replace('.webp?size=1024', '.png?size=512')
                await ctx.send(file=discord.File(Painter.ifearnoman(by, source), 'i_fear_no_man.png'))

    @commands.command(pass_context=True, aliases=['stonks', 'immaheadout', 'homer', 'monkeypuppet', 'tom', 'surprisedpikachu', 'meandtheboys'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pabloescobar(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Where is the meme's context?")
        else:
            async with ctx.message.channel.typing():
                try:
                    data = Painter.simpleTopMeme(' '.join(list(args)), './assets/pics/'+str(ctx.message.content).split(' ')[0][1:]+'.jpg', 40, 3)
                    await ctx.send(file=discord.File(data, 'top_meme.png'))
                except Exception as e:
                    await ctx.send('Oopsies! There was an error on creating your chosen meme;\n'+str(e))

    @commands.command(pass_context=True, aliases=['presentation'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def firstwords(self, ctx, *args):
        unprefixed = ' '.join(list(args))
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Where is the meme's context?")
        else:
            async with ctx.message.channel.typing():
                try:
                    if 'presentation' in ctx.message.content: data = Painter.presentationMeme(unprefixed, "./assets/pics/presentation.jpg")
                    else: data = Painter.firstwords(unprefixed, "./assets/pics/firstwords.jpg")
                    await ctx.send(file=discord.File(data, 'lol.png'))
                except Exception as e:
                    await ctx.send('Oopsies! There was an error on creating your chosen meme;\n'+str(e))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def triggered(self, ctx, *args):
        increment, accept = None, True
        for i in list(args):
            if i.isnumeric():
                increment = int(i)
                break
        if increment==None: increment = 5
        if increment!=5:
            if increment<1: 
                accept = False
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) + " | Increment to small!")
            elif increment>50:
                accept = False
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) + " | Increment to big!")
        if accept:
            if len(ctx.message.mentions)==0: ava = str(ctx.message.author.avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            else: ava = str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            async with ctx.message.channel.typing():
                data = Painter.gif.triggered(ava, increment)
                await ctx.send(file=discord.File(data, 'triggered.gif'))

    @commands.command(pass_context=True, aliases=['communism', 'ussr', 'soviet', 'cykablyat', 'cyka-blyat', 'blyat'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def communist(self, ctx):
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)==0: comrade = str(ctx.message.author.avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            else: comrade = str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            data = Painter.gif.communist(comrade)
            await ctx.send(file=discord.File(data, 'cyka_blyat.gif'))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trash(self, ctx):
        if len(ctx.message.mentions)==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Please mention someone....')
        else:
            async with ctx.message.channel.typing():
                av = ctx.message.author.avatar_url
                toTrash = ctx.message.mentions[0].avatar_url
                url='https://api.alexflipnote.dev/trash?face='+str(av).replace('webp', 'png')+'&trash='+str(toTrash).replace('webp', 'png')
                data = Painter.urltoimage(url)
                await ctx.send(file=discord.File(data, 'trashed.png'))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def trap(self, ctx):
        if len(ctx.message.mentions)==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | Wrong.\nPlease try the correct like following:\n`{prefix}trap [tag]`')
        else:
            async with ctx.message.channel.typing():
                url='http://nekobot.xyz/api/imagegen?type=trap&name='+myself.urlify(str(ctx.message.mentions[0].name))+'&author='+myself.urlify(str(message.author.name))+'&image='+str(message.mentions[0].avatar_url).replace('.webp?size=1024', '.png')+'&raw=1'
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'trap.png'))

    @commands.command(pass_context=True, aliases=['winorlose'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def whowouldwin(self, ctx):
        if len(ctx.message.mentions)!=2:
            await ctx.send('Please tag TWO people!')
        else:
            async with ctx.message.channel.typing():
                url='http://nekobot.xyz/api/imagegen?type=whowouldwin&raw=1&user1='+str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.png')+'&user2='+str(ctx.message.mentions[1].avatar_url).replace('.webp?size=1024', '.png')
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'whowouldwin.png'))
    # 431, 167, 486, 387, 1088, 720
    @commands.command(pass_context=True, aliases=['tvsquidward', 'squidstv', 'squidtv', 'tvsquid', 'squidward', 'tv'])
    @commands.cooldown(1, 8, commands.BucketType.user)
    async def squidwardstv(self, ctx):
        if len(ctx.message.mentions)==0: source = str(ctx.message.author.avatar_url).replace('.gif', '.webp')
        else: source = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp')
        await ctx.send(file=discord.File(Painter.squidwardstv(str(source).replace('.webp?size=1024', '.png?size=512')), 'squidtv.png'))
    
    @commands.command(pass_context=True, aliases=['mywaifu', 'wf', 'waifuinsult', 'waifu-insult'])
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def waifu(self, ctx):
        if len(ctx.message.mentions)==0: source = str(ctx.message.author.avatar_url).replace('.gif', '.webp')
        else: source = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp')
        await ctx.send(file=discord.File(Painter.waifu(str(source).replace('.webp?size=1024', '.png?size=512')), 'mywaifu.png'))

    @commands.command(pass_context=True, aliases=['wanted', 'chatroulette', 'sacred', 'coffindance', 'frame', 'window', 'art'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ferbtv(self, ctx):
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)<1: ava = str(ctx.message.author.avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            else: ava = str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.jpg?size=512')
            if 'wanted' in ctx.message.content: num1, num2, num3, num4 = 547, 539, 167, 423
            elif 'ferbtv' in ctx.message.content: num1, num2, num3, num4 = 362, 278, 363, 187
            elif 'chatroulette' in ctx.message.content: num1, num2, num3, num4 = 324, 243, 14, 345
            elif 'sacred' in ctx.message.content: num1, num2, num3, num4 = 454, 498, 1210, 986
            elif 'coffindance' in ctx.message.content: num1, num2, num3, num4 = 220, 228, 421, 58
            elif 'frame' in ctx.message.content: num1, num2, num3, num4, ava = 1025, 715, 137, 141, str(ava).replace("=512", "=1024")
            elif 'window' in ctx.message.content: num1, num2, num3, num4 = 219, 199, 4, 21
            if 'art' not in ctx.message.content: image = Painter.putimage(ava, str(ctx.message.content).split()[0][1:], num1, num2, num3, num4)
            else: image = Painter.art(ava)
            await ctx.send(file=discord.File(image, str(ctx.message.content)[1:].replace(' ', '')+'.png'))

    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def scroll(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Error! where is your text?")
        else:
            async with ctx.message.channel.typing():
                scrolltxt = myself.urlify(' '.join(list(args)))
                embed = discord.Embed(colour=discord.Colour.from_rgb(201, 160, 112))
                url='https://api.alexflipnote.dev/scroll?text='+str(scrolltxt)
                data = Painter.urltoimage(url)
                await ctx.send(file=discord.File(data, 'scroll.png'))
    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def imgcaptcha(self, ctx):
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)==0: av, nm = str(ctx.message.author.avatar_url).replace('.webp?size=1024', '.png'), myself.urlify(str(ctx.message.author.name))
            else: av, nm = str(ctx.message.mentions[0].avatar_url).replace('.webp?size=1024', '.png'), myself.urlify(str(ctx.message.mentions[0].name))
            url = 'http://nekobot.xyz/api/imagegen?type=captcha&username='+nm+'&url='+av+'&raw=1'
            data = Painter.urltoimage(url)
            await ctx.send(file=discord.File(data, 'your_captcha.png'))
    
    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def captcha(self, ctx, *args):
        async with ctx.message.channel.typing():
            capt = myself.urlify(' '.join(args))
            data = Painter.urltoimage('https://api.alexflipnote.dev/captcha?text='+str(capt))
            await ctx.send(file=discord.File(data, 'captcha.png'))

    @commands.command(pass_context=True, aliases=['baby', 'clint', 'wolverine', 'disgusting', 'f', 'studying', 'starvstheforcesof'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def door(self, ctx):
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)==0: ava = str(ctx.message.author.avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512')
            else: ava = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512')
            if 'door' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "door", 1000, 479, 496, 483, 247, 9), 'door.png'))
            elif 'studying' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "studying", 563, 999, 290, 315, 85, 160), "studying.png")) 
            elif 'clint' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "clint", 1200, 675, 339, 629, 777, 29), 'clintclint.png'))
            elif 'starvstheforcesof' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "starvstheforcesof", 1920, 1080, 995, 1079, 925, 0), "starvstheforcesof.png")) 
            elif 'wolverine' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "wolverine", 450, 698, 368, 316, 85, 373), 'wolverine.png'))
            elif 'disgusting' in ctx.message.content: await ctx.send(file=discord.File(Painter.put_transparent(ava, "disgusting", 1024, 1080, 614, 407, 179, 24), 'disgusting.png'))
            elif 'f' in ctx.message.content and len(str(ctx.message.content).split(' ')[0])==2: await ctx.send(file=discord.File(Painter.f(ava), 'f.png'))
            else: await ctx.send(file=discord.File(Painter.baby(ava), 'lolmeme.png'))

    @commands.command(pass_context=True, aliases=['changedmymind'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def changemymind(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Error! You need a text...")
        else:
            await ctx.message.add_reaction(self.client.get_emoji(BotEmotes.loading))
            async with ctx.message.channel.typing():
                try:
                    data = Painter.urltoimage('https://nekobot.xyz/api/imagegen?type=changemymind&text='+myself.urlify(' '.join(list(args)))+'&raw=1')
                    await ctx.send(file=discord.File(data, 'changemymind.png'))
                except Exception as e:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error))+" | Oops! There was an error on generating your meme; `"+str(e)+"`")

    @commands.command(pass_context=True, aliases=['gimme', 'memz', 'memey'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        data = myself.api("https://meme-api.herokuapp.com/gimme")
        embed = discord.Embed(colour = discord.Colour.from_rgb(201, 160, 112))
        embed.set_author(name=data["title"], url=data["postLink"])
        if data["nsfw"]:
            embed.set_footer(text='WARNING: IMAGE IS NSFW.')
        else:
            embed.set_image(url=data["url"])
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, aliases=['trumptweet', 'kannagen'])
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def clyde(self, ctx, *args):
        if len(list(args))==0: await ctx.send('Please input a text...')
        else:
            async with ctx.message.channel.typing():
                url='https://nekobot.xyz/api/imagegen?type='+str(ctx.message.content).split(' ')[0][1:]+'&text='+myself.urlify(' '.join(list(args)))+'&raw=1'
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'lawl.png'))

    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def floor(self, ctx, *args):
        if len(list(args))==0: text = 'I forgot to put the arguments, oops'
        else: text = str(' '.join(args))
        auth = str(ctx.message.author.avatar_url).replace('.gif', '.webp').replace('.webp', '.png')
        async with ctx.message.channel.typing():
            if len(ctx.message.mentions)>0:
                auth = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp').replace('.webp', '.png')
                if len(args)>2: text = str(ctx.message.content).split('> ')[1]
                else: text = 'I forgot to put the arguments, oops'
            await ctx.send(file=discord.File(Painter.urltoimage('https://api.alexflipnote.dev/floor?image='+auth+'&text='+myself.urlify(text)), 'floor.png'))

    @commands.command(pass_context=True, aliases=['bad'])
    @commands.cooldown(1, 7, commands.BucketType.user)
    async def amiajoke(self, ctx, *args):
        if len(ctx.message.content)==0: source = str(ctx.message.author.avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512')
        else: source = str(ctx.message.mentions[0].avatar_url).replace('.gif', '.webp').replace('.webp?size=1024', '.png?size=512')
        if 'bad' in ctx.message.content: url = 'https://api.alexflipnote.dev/bad?image='+str(source)
        else: url = 'https://api.alexflipnote.dev/amiajoke?image='+str(source)
        await ctx.send(file=discord.File(Painter.urltoimage(url), 'maymays.png'))

    @commands.command(pass_context=True, aliases=['avmeme', 'philosoraptor', 'money', 'doge', 'fry'])
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def wonka(self, ctx, *args):
        if 'avmeme' in ctx.message.content:
            async with ctx.message.channel.typing():
                try:
                    av = ctx.message.mentions[0].avatar_url
                    mes = ctx.message.content[int(len(args[0])+len(args[1])+1):]
                    top = myself.urlify(str(ctx.message.content).split('[')[1].split(']')[0])
                    bott = myself.urlify(str(ctx.message.content).split('[')[2].split(']')[0])
                    name = 'custom'
                    extr = '?alt='+str(av).replace('webp', 'png')
                    url='https://memegen.link/'+str(name)+'/'+str(top)+'/'+str(bott)+'.jpg'+str(extr)
                    await ctx.send(file=discord.File(Painter.memegen(url), 'avmeme.png'))
                except Exception as e:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | Error!\n```{e}```Invalid parameters. Example: `{prefix}avmeme <tag someone> [top text] [bottom text]`')
        else:
            async with ctx.message.channel.typing():
                try:
                    top = myself.urlify(str(ctx.message.content).split('[')[1].split(']')[0])
                    bott = myself.urlify(str(ctx.message.content).split('[')[2].split(']')[0])
                    name = str(ctx.message.content).split(Config.prefix)[1].split(' ')[0]
                    url='https://memegen.link/'+str(name)+'/'+str(top)+'/'+str(bott)+'.jpg?watermark=none'
                    await ctx.send(file=discord.File(Painter.memegen(url), args[0][1:]+'.png'))
                except Exception as e:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | Error!\n```{e}```Invalid parameters.')
def setup(client):
    client.add_cog(memes(client))
