import discord
from discord.ext import commands
import sys
sys.path.append('/home/runner/hosting601/modules')
import username601 as myself
import splashes as src
from decorators import command, cooldown
import random
import canvas as Painter
from username601 import *
import pokebase as pb
import discordgames as Games
from database import Economy
import asyncio

class games(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @command()
    @cooldown(3)
    async def gdlevel(self, ctx, *args):
        if len(list(args))==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Please enter a level ID!')
        else:
            if not args[0].isnumeric():
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | That is not a level ID!')
            else:
                try:
                    levelid = str(args[0])
                    toEdit = await ctx.send(str(self.client.get_emoji(BotEmotes.loading))+" | Retrieving Data...")
                    data = myself.api("https://gdbrowser.com/api/level/"+str(levelid))
                    image = 'https://gdbrowser.com/icon/'+data["author"]
                    embed = discord.Embed(
                        title = data["name"]+' ('+str(data["id"])+')',
                        description = data["description"],
                        colour = discord.Colour.from_rgb(201, 160, 112)
                    )
                    embed.set_author(name=data["author"], icon_url=image)
                    embed.add_field(name='Difficulty', value=data["difficulty"])
                    gesture = ':+1:'
                    if data['disliked']: gesture = ':-1:'
                    embed.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
                    embed.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
                    await toEdit.edit(content='', embed=embed)
                except Exception as e:
                    await toEdit.edit(content=f'```{e}```')
    @command()
    @cooldown(3)
    async def gdsearch(self, ctx, *args):
        if len(list(args))==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Please input a query!')
        else:
            try:
                query = myself.urlify(' '.join(list(args)))
                data = myself.api('https://gdbrowser.com/api/search/'+str(query))
                levels, count = '', 0
                for i in range(0, len(data)):
                    if data[count]['disliked']: like = ':-1:'
                    else: like = ':+1:'
                    levels += str(count+1)+'. **'+data[count]['name']+'** by '+data[count]['author']+' (`'+data[count]['id']+'`)\n:arrow_down: '+data[count]['downloads']+' | '+like+' '+data[count]['likes']+'\n'
                    count += 1
                embedy = discord.Embed(title='Geometry Dash Level searches for "'+str(' '.join(list(args)))+'":', description=levels, colour=discord.Colour.from_rgb(201, 160, 112))
                await ctx.send(embed=embedy)
            except:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) + ' | Error: Not Found. :four::zero::four:')

    @command()
    @cooldown(3)
    async def gdprofile(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Gimme some ARGS!')
        else:
            try:
                url = myself.urlify(str(' '.join(list(args))))
                data = myself.api("https://gdbrowser.com/api/profile/"+url)
                embed = discord.Embed(
                    title = data["username"],
                    description = 'Displays user data for '+data["username"]+'.',
                    colour = discord.Colour.orange()
                )
                if data["rank"]=="0": rank = "Not yet defined :("
                else: rank = str(data["rank"])
                if data["cp"]=="0": cp = "This user don't have Creator Points :("
                else: cp = data["cp"]
                embed.add_field(name='ID Stuff', value='Player ID: '+str(data["playerID"])+'\nAccount ID: '+str(data["accountID"]), inline='True')
                embed.add_field(name='Rank', value=rank, inline='True')
                embed.add_field(name='Stats', value=str(data["stars"])+" Stars"+"\n"+str(data["diamonds"])+" Diamonds\n"+str(data["coins"])+" Secret Coins\n"+str(data["userCoins"])+" User Coins\n"+str(data["demons"])+" Demons beaten", inline='False')
                embed.add_field(name='Creator Points', value=cp)
                embed.set_author(name='Display User Information', icon_url="https://gdbrowser.com/icon/"+url)
                await ctx.send(embed=embed)
            except:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Error, user not found.')
    
    @command()
    @cooldown(3)
    async def gdlogo(self, ctx, *args):
        if len(list(args))==0:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Please input a text!')
        else:
            async with ctx.message.channel.typing():
                text = myself.urlify(' '.join(list(args)))
                url='https://gdcolon.com/tools/gdlogo/img/'+str(text)
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'gdlogo.png'))
    
    @command()
    @cooldown(3)
    async def gdbox(self, ctx, *args):
        if len(list(args))==0: await ctx.send(str(self.client.get_emoji(BotEmotes.error))+' | Please input a text!')
        else:
            async with ctx.message.channel.typing():
                text, av = myself.urlify(str(' '.join(list(args)))), ctx.message.author.avatar_url
                if len(text)>100: await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | the text is too long!')
                else:
                    if not ctx.message.author.guild_permissions.manage_guild: color = 'brown'
                    else: color = 'blue'
                    url='https://gdcolon.com/tools/gdtextbox/img/'+str(text)+'?color='+color+'&name='+str(ctx.message.author.name)+'&url='+str(av).replace('webp', 'png')+'&resize=1'
                    await ctx.send(file=discord.File(Painter.urltoimage(url), 'gdbox.png'))
   
    @command()
    @cooldown(3)
    async def gdcomment(self, ctx, *args):
        async with ctx.message.channel.typing():
            try:
                byI = str(' '.join(list(args))).split(' | ')
                text = myself.urlify(byI[0])
                num = int(byI[2])
                if num>9999: num = 601
                elif num<-9999: num = -601
                gdprof = myself.urlify(byI[1])
                if ctx.message.author.guild_permissions.manage_guild: url='https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(gdprof)+'&likes='+str(num)+'&mod=mod&days=1-second'
                else: url='https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(gdprof)+'&likes='+str(num)+'&days=1-second'
                await ctx.send(file=discord.File(Painter.urltoimage(url), 'gdcomment.png'))
            except Exception as e:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +f' | Invalid!\nThe flow is this: `{Config.prefix}gdcomment text | name | like count`\nExample: `{prefix}gdcomment I am cool | RobTop | 601`.\n\nFor developers: ```{e}```')

    @command('gdweekly')
    @cooldown(2)
    async def gddaily(self, ctx):
        toEdit = await ctx.send(str(self.client.get_emoji(BotEmotes.loading))+" | Retrieving Data...")
        if 'daily' in ctx.message.content: name = 'daily'
        else: name = 'weekly'
        data = myself.api("https://gdbrowser.com/api/level/"+name)
        image = 'https://gdbrowser.com/icon/'+data["author"]
        embed = discord.Embed(
            title = data["name"]+' ('+str(data["id"])+')',
            description = data["description"],
            colour = discord.Colour.from_rgb(201, 160, 112)
        )
        embed.set_author(name=data["author"], icon_url=image)
        embed.add_field(name='Uploaded at', value=data["uploaded"], inline='True')
        embed.add_field(name='Updated at', value=data["updated"]+" (Version "+data["version"]+")", inline='True')
        embed.add_field(name='Difficulty', value=data["difficulty"])
        gesture = ':+1:'
        if data['disliked']: gesture = ':-1:'
        embed.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
        embed.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
        await toEdit.edit(content='', embed=embed)

    @command('rockpaperscissors')
    @cooldown(5)
    async def rps(self, ctx):
        main = await ctx.send(embed=discord.Embed(title='Rock Paper Scissors game.', description='Click the reaction below. And game will begin.', colour=discord.Colour.from_rgb(201, 160, 112)))
        exp = ['✊', '🖐️', '✌']
        for i in range(0, len(exp)):
            await main.add_reaction(exp[i])
        def check(reaction, user):
            return user == ctx.message.author
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await main.add_reaction('😔')
        emojiArray, ran, given, beginGame = None, None, None, False
        if str(reaction.emoji) in exp:
            emotes = ["fist", "hand_splayed", "v"]
            num = myself.findNum(str(reaction.emoji), exp)
            beginGame = True
            res = Games.rps(emotes[num])
            given = emotes[num]
            msgId = res[0]
            emojiArray = emotes
            ran = res[1]
        messages = ["Congratulations! "+str(ctx.message.author.name)+" WINS!", "It's a draw.", "Oops, "+str(ctx.message.author.name)+" lost!"]
        colors = [discord.Colour.from_rgb(201, 160, 112), discord.Colour.orange(), discord.Colour.from_rgb(201, 160, 112)]
        if beginGame:
            embed = discord.Embed(
                title = messages[msgId],
                colour = colors[msgId]
            )
            embed.set_footer(text='Playin\' rock paper scissors w/ '+str(ctx.message.author.name))
            embed.set_author(name="Playing Rock Paper Scissors with "+str(ctx.message.author.name))
            embed.add_field(name=str(ctx.message.author.name), value=':'+given+':', inline="True")
            embed.add_field(name='Username601', value=':'+str(emojiArray[ran])+':', inline="True")
            await main.edit(embed=embed)
            if msgId==1 and Economy.get(ctx.message.author.id)!=None:
                reward = random.randint(5, 100)
                Economy.addbal(ctx.message.author.id, reward)
                await ctx.send('thank you for playing! you earned '+str(reward)+' as a prize!')

    @command('dice,flipcoin,flipdice,coinflip,diceflip,rolldice')
    @cooldown(3)
    async def coin(self, ctx, *args):
        if 'coin' in ctx.message.content:
            res = random.choice(['***heads!***', '***tails!***'])
            await ctx.send(res)
            if len(list(args))>0 and args[0].lower()==res.replace('*', '').replace('!', '') and Economy.get(ctx.message.author.id)!=None:
                prize = random.randint(50, 200)
                Economy.addbal(ctx.message.author.id, prize) ; await ctx.send('your bet was right! you get '+str(prize)+' diamonds.')
        else:
            res = random.randint(1, 6)
            await ctx.send(':'+src.num2word(res)+':')
            if len(list(args))>0 and args[0]==str(res) and Economy.get(ctx.message.author.id)!=None:
                prize = random.randint(50, 100)
                Economy.addbal(ctx.message.author.id, prize) ; await ctx.send('your bet was right! you get '+str(prize)+' diamonds.')

    @command('guessav,avatarguess,avguess,avatargame,avgame')
    @cooldown(30)
    async def guessavatar(self, ctx):
        if len(ctx.message.guild.members)>500:
            await ctx.send('Sorry, to protect some people\'s privacy, this command is not available for Large servers. (over 500 members)')
        else:
            wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... generating question...\nThis process may take longer if your server has more members.')
            avatarAll, nameAll = [], []
            for ppl in ctx.guild.members:
                if ctx.guild.get_member(int(ppl.id)).status.name!='offline':
                    avatarAll.append(str(ppl.avatar_url).replace('webp', 'png'))
                    nameAll.append(ppl.display_name)
            if len(avatarAll)<=4:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | Need more online members! :x:')
            else:
                numCorrect = random.randint(0, len(avatarAll)-1)
                corr_avatar, corr_name = avatarAll[numCorrect], nameAll[numCorrect]
                nameAll.remove(corr_name)
                wrongArr = []
                for i in range(0, 3):
                    wrongArr.append(random.choice(nameAll))
                abcs, emots = list('🇦🇧🇨🇩'), list('🇦🇧🇨🇩')
                randomInt = random.randint(0, 3)
                corr_order = random.choice(abcs[randomInt])
                abcs[randomInt] = '0'
                question, chooseCount = '', 0
                for assign in abcs:
                    if assign!='0':
                        question += '**'+ str(assign) + '.** '+str(wrongArr[chooseCount])+ '\n'
                        chooseCount += 1
                    else:
                        question += '**'+ str(corr_order) + '.** '+str(corr_name)+ '\n'
                embed = discord.Embed(title='What does the avatar below belongs to?', description=':eyes: Click the reactions! **You have 20 seconds.**\n\n'+str(question), colour=discord.Colour.from_rgb(201, 160, 112))
                embed.set_footer(text='For privacy reasons, the people displayed above are online users.')
                embed.set_image(url=corr_avatar)
                main = await ctx.send(embed=embed)
                for i in emots: await main.add_reaction(i)
                def is_correct(reaction, user):
                    return user == ctx.message.author
                try:
                    reaction, user = await self.client.wait_for('reaction_add', check=is_correct, timeout=20.0)
                except asyncio.TimeoutError:
                    return await ctx.send(':pensive: No one? Okay then, the answer is: '+str(corr_order)+'. '+str(corr_name))
                if str(reaction.emoji)==str(corr_order):
                    await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | <@'+str(ctx.message.author.id)+'>, You are correct! :tada:')
                    if Economy.get(ctx.message.author.id)!=None:
                        reward = random.randint(5, 100)
                        Economy.addbal(ctx.message.author.id, reward)
                        await ctx.send('thanks for playing! You received '+str(reward)+' extra diamonds!')
                else:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | <@'+str(ctx.message.author.id)+'>, Incorrect. The answer is '+str(corr_order)+'. '+str(corr_name))

    @command()
    @cooldown(30)
    async def geoquiz(self, ctx):
        wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... generating question...')
        data, topic = myself.api("https://restcountries.eu/rest/v2/"), random.choice(src.getGeoQuiz())
        chosen_nation_num = random.randint(0, len(data))
        chosen_nation, wrongs = data[chosen_nation_num], []
        data.remove(data[chosen_nation_num])
        correct = str(chosen_nation[topic])
        for i in range(0, 4):
            integer = random.randint(0, len(data))
            wrongs.append(str(data[integer][str(topic)]))
            data.remove(data[integer])
        emot, static_emot, corr_order_num = list('🇦🇧🇨🇩'), list('🇦🇧🇨🇩'), random.randint(0, 3)
        corr_order = emot[corr_order_num]
        emot[corr_order_num], question, guy = '0', '', ctx.message.author
        for emote in emot:
            if emote!='0':
                added = random.choice(wrongs)
                question += emote + ' ' + added + '\n'
                wrongs.remove(added)
            else:
                question += corr_order + ' ' + correct + '\n'
        embed = discord.Embed(title='Geography: '+str(topic)+' quiz!', description=':nerd: Click on the reaction! **You have 20 seconds.**\n\nWhich '+str(topic)+' belongs to '+str(chosen_nation['name'])+'?\n'+str(question), colour=discord.Colour.from_rgb(201, 160, 112))
        await wait.edit(content='', embed=embed)
        for i in range(0, len(static_emot)):
            await wait.add_reaction(static_emot[i])
        def check(reaction, user):
            return user == guy
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=20.0, check=check)
        except asyncio.TimeoutError:
            await main.add_reaction('😔')
        if str(reaction.emoji)==str(corr_order):
            await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | <@'+str(guy.id)+'>, Congrats! You are correct. :partying_face:')
            if Economy.get(ctx.message.author.id)!=None:
                reward = random.randint(5, 150)
                Economy.addbal(ctx.message.author.id, reward)
                await ctx.send('thanks for playing! You obtained '+str(reward)+' diamonds in total!')
        else:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | <@'+str(guy.id)+'>, You are incorrect. The answer is '+str(corr_order)+'.')

    @command()
    @cooldown(15)
    async def mathquiz(self, ctx):
        arrayId, num1, num2, symArray = random.randint(0, 4), random.randint(1, 100), random.randint(1, 100), ['+', '-', 'x', ':', '^']
        ansArray = [num1+num2, num1-num2, num1*num2, num1/num2, num1**num2]
        sym = symArray[arrayId]
        await ctx.send('**MATH QUIZ (15 seconds)**\n'+str(num1)+' '+str(sym)+' '+str(num2)+' = ???')
        def is_correct(m):
            return m.author == ctx.message.author
        answer = round(ansArray[arrayId])
        try:
            trying = await self.client.wait_for('message', check=is_correct, timeout=15.0)
        except asyncio.TimeoutError:
            return await ctx.send(':pensive: No one? Okay then, the answer is: {}.'.format(answer))
        if str(trying.content)==str(answer):
            await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | <@'+str(ctx.message.author.id)+'>, You are correct! :tada:')
            if Economy.get(ctx.message.author.id)!=None:
                reward = random.randint(5, 50)
                Economy.addbal(ctx.message.author.id, reward)
                await ctx.send('thanks for playing! we added an extra '+str(reward)+' diamonds to your profile.')
        else:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | <@'+str(ctx.message.author.id)+'>, Incorrect. The answer is {}.'.format(answer))

    @command()
    @cooldown(60)
    async def hangman(self, ctx):
        wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... generating...')
        the_word = myself.api("https://random-word-api.herokuapp.com/word?number=1")
        main_guess_cor, main_guess_hid = list(the_word[0]), []
        server_id, wrong_guesses = ctx.message.guild.id, ''
        for i in range(0, len(main_guess_cor)):
            main_guess_hid.append('\_ ')
        guessed, gameplay, playing_with, playing_with_id, level = [], True, ctx.message.author, int(ctx.message.author.id), 0
        while gameplay:
            if ctx.message.content==Config.prefix+'hangman' and ctx.message.author.id!=int(playing_with_id) and ctx.message.guild.id==server_id:
                await ctx.send('<@'+str(ctx.message.author.id)+'>, cannot play hangman when a game is currently playing!')
            newembed = discord.Embed(title=''.join(main_guess_hid), description='Wrong guesses: '+str(wrong_guesses), colour=discord.Colour.from_rgb(201, 160, 112))
            newembed.set_image(url=f'https://raw.githubusercontent.com/vierofernando/username601/master/assets/pics/hangman_{str(level)}.png')
            newembed.set_footer(text='Type "showanswer" to show the answer and end the game.')
            await ctx.send(embed=newembed)
            if '\_ ' not in ''.join(main_guess_hid):
                await ctx.send(f'Congratulations! <@{str(playing_with_id)}> win! :tada:\nThe answer is "'+str(''.join(main_guess_cor))+'".')
                if Economy.get(ctx.message.author.id)!=None:
                    reward = random.randint(5, 500)
                    Economy.addbal(ctx.message.author.id, reward)
                    await ctx.send('thanks for playing! you get an extra '+str(reward)+' diamonds!')
                gameplay = False ; break
            if level>7:
                await ctx.send(f'<@{str(playing_with_id)}> lost! :(\nThe answer is actually "'+str(''.join(main_guess_cor))+'".')
                gameplay = False ; break
            def is_not_stranger(m):
                return m.author == playing_with
            try:
                trying = await self.client.wait_for('message', check=is_not_stranger, timeout=20.0)
            except asyncio.TimeoutError:
                await ctx.send(f'<@{str(playing_with_id)}> did not response in 20 seconds so i ended the game. Keep un-AFK!\nOh and btw, the answer is '+str(''.join(main_guess_cor))+'. :smirk:')
                gameplay = False ; break
            if str(trying.content).lower()=='showanswer':
                await ctx.send('The answer is actually '+str(''.join(main_guess_cor)+'.'))
                gameplay = False ; break
            elif len(str(trying.content))>1:
                await ctx.send('One word at a time. Game ended!')
                gameplay = False ; break
            elif str(trying.content).lower() in guessed:
                await ctx.send(f'<@{str(playing_with_id)}>, You have guessed that letter!')
                level = int(level)+1
            elif str(trying.content).lower() in ''.join(main_guess_cor).lower():
                guessed.append(str(trying.content).lower())
                for i in range(0, len(main_guess_cor)):
                    if main_guess_cor[i].lower()==str(trying.content).lower():
                        main_guess_hid[i] = str(trying.content).lower()
            else:
                level = int(level) + 1
                wrong_guesses = wrong_guesses + str(trying.content).lower() + ', '

    @command()
    @cooldown(2)
    async def slot(self, ctx):
        win, jackpot, slots = False, False, []
        for i in range(0, 3):
            newslot = Games.slot()
            if newslot[1]==newslot[2] and newslot[1]==newslot[3] and newslot[2]==newslot[3]:
                win = True
                if newslot[1]==':flushed:':
                    jackpot = True
            slots.append(Games.slotify(newslot))
        if win:
            msgslot = 'You win!'
            col = discord.Colour.from_rgb(201, 160, 112)
            if jackpot:
                msgslot = 'JACKPOT!'
                col = discord.Colour.from_rgb(201, 160, 112)
            if Economy.get(ctx.message.author.id)!=None:
                reward = random.randint(500, 1000)
                Economy.addbal(ctx.message.author.id, reward)
                await ctx.send('thanks for playing! you received a whopping '+str(reward)+' diamonds!')
        else:
            msgslot = 'You lose... Try again!'
            col = discord.Colour.from_rgb(201, 160, 112)
        embed = discord.Embed(title=msgslot, description=slots[0]+'\n\n'+slots[1]+'\n\n'+slots[2], colour=col)
        await ctx.send(embed=embed)

    @command('defuse,boom')
    @cooldown(7)
    async def bomb(self, ctx):
        def embedType(a):
            if a==1: return discord.Embed(title='The bomb exploded!', description='Game OVER!', colour=discord.Colour(000))
            elif a==2: return discord.Embed(title='The bomb defused!', description='Congratulations! :grinning:', colour=discord.Colour.from_rgb(201, 160, 112))
        embed = discord.Embed(title='DEFUSE THE BOMB!', description='**Cut the correct wire!\nThe bomb will explode in 15 seconds!**', colour=discord.Colour.from_rgb(201, 160, 112))
        main = await ctx.send(embed=embed)
        buttons = ['🔴', '🟡', '🔵', '🟢']
        for i in range(0, len(buttons)):
            await main.add_reaction(buttons[i])
        correct = random.choice(buttons)
        def check(reaction, user):
            return user == ctx.message.author
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await main.edit(content='', embed=embedType(1))
        if str(reaction.emoji)!=correct:
            await main.edit(content='', embed=embedType(1))
        else:
            await main.edit(content='', embed=embedType(2))

    @command('gn,guessnumber')
    @cooldown(30)
    async def guessnum(self, ctx):
        num = random.randint(5, 100)
        username = ctx.message.author.display_name
        user_class = ctx.message.author
        embed = discord.Embed(title='Starting the game!', description='You have to guess a *secret* number between 5 and 100!\n\nYou have 20 attempts, and 20 second timer in each attempt!\n\n**G O O D  L U C K**', colour=discord.Colour.from_rgb(201, 160, 112))
        await ctx.send(embed=embed)
        gameplay = True
        attempts = 20
        while gameplay==True:
            if attempts<1:
                await ctx.send('Time is up! The answer is **'+str(num)+'.**')
                gameplay = False
                break
            def check_not_stranger(m):
                return m.author == user_class
            try:
                trying = await self.client.wait_for('message', check=check_not_stranger, timeout=20.0)
            except asyncio.TimeoutError:
                await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | You did not respond for the next 20 seconds!\nGame ended.')
                gameplay = False
                break
            if trying.content.isnumeric()==False:
                await ctx.send('That is not a number!')
                attempts = int(attempts) - 1
            else:
                if int(trying.content)<num:
                    await ctx.send('Higher!')
                    attempts = int(attempts) - 1
                if int(trying.content)>num:
                    await ctx.send('Lower!')
                    attempts = int(attempts) - 1
                if int(trying.content)==num:
                    await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | You are correct!\n**The answer is '+str(num)+'!**')
                    if Economy.get(ctx.message.author.id)!=None:
                        reward = random.randint(5, 50)
                        Economy.addbal(ctx.message.author.id, reward)
                        await ctx.send('thanks for playing! You get an extra '+str(reward)+' diamonds!')
                    gameplay = False
                    break

    @command()
    @cooldown(25)
    async def pokequiz(self, ctx):
        wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... Generating quiz...')
        num = random.randint(1, 800)
        try:
            corr = pb.pokemon(str(num)).name
        except Exception as e:
            await wait.edit(content=str(self.client.get_emoji(BotEmotes.error)) + f' | An error occured! ```{e}```')
        hint = 2
        attempt = 10
        gameplay = True
        guy = ctx.message.author
        while gameplay==True:
            newembed = discord.Embed(title='Pokemon Quiz!', description=f'Guess the pokemon\'s name!\nTimeout: 45 seconds.\nHint left: **{str(hint)}** | Attempts left: **{str(attempt)}**', colour=discord.Colour.from_rgb(201, 160, 112))
            newembed.set_image(url=f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{str(num)}.png')
            newembed.set_footer(text='Type "hint" to give.. uh... the HINT! :D')
            newembed.set_thumbnail(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{str(num)}.png')
            await wait.edit(content='', embed=newembed)
            if int(attempt)<1:
                await ctx.send('You lose! The pokemon is **'+str(corr)+'**!')
                gameplay = False
                break
            def checking(m):
                return m.author == guy
            try:
                guessing = await self.client.wait_for('message', check=checking, timeout=45.0)
            except asyncio.TimeoutError:
                await ctx.send('Too late! Game ended... :pensive:')
                gameplay = False ; break
            if str(guessing.content).lower()==corr:
                currentmsg = guessing
                await currentmsg.add_reaction('✅')
                await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | You are correct! The pokemon is **'+str(corr)+'**')
                if Economy.get(ctx.message.author.id)!=None:
                    reward = random.randint(50, 250)
                    Economy.addbal(ctx.message.author.id, reward)
                    await ctx.send('thanks for playing! You get also a '+str(reward)+' diamonds as a prize!')
                gameplay = False
                break
            elif str(guessing.content).lower()=='hint':
                currentmsg = guessing
                if hint<1:
                    await currentmsg.add_reaction('❌')
                    attempt -= - 1
                else:
                    await currentmsg.add_reaction('✅')
                    thehint = random.choice([myself.hintify(corr), 'Pokemon name starts with "'+str(list(corr)[0])+'"', 'Pokemon name has '+str(len(corr))+' letters!', 'Pokemon name ends with "'+str(list(corr)[len(corr)-1])+'"'])
                    await ctx.send('Hint: '+thehint+'!')
                    hint -= 1 ; attempt -= 1
            else:
                if attempt!=0:
                    await guessing.add_reaction('❌')
                    attempt -= 1
                else:
                    await guessing.add_reaction('❌')
                    await ctx.send('You lose! The pokemon is **'+str(corr)+'**!')
                    gameplay = False ; break

    @command()
    @cooldown(30)
    async def trivia(self, ctx):
        al = None
        try:
            wait = await ctx.send(str(self.client.get_emoji(BotEmotes.loading)) + ' | Please wait... generating quiz...')
            auth = ctx.message.author
            data = myself.api('https://wiki-quiz.herokuapp.com/v1/quiz?topics=Science')
            q = random.choice(data['quiz'])
            choices = ''
            for i in range(0, len(q['options'])):
                al = list('🇦🇧🇨🇩')
                if q['answer']==q['options'][i]:
                    corr = al[i]
                choices = choices + al[i] +' '+ q['options'][i]+'\n'
            embed = discord.Embed(title='Trivia!', description='**'+q['question']+'**\n'+choices, colour=discord.Colour.from_rgb(201, 160, 112))
            embed.set_footer(text='Answer by clicking the reaction! You have 60 seconds.')
            await wait.edit(content='', embed=embed)
            for i in range(0, len(al)):
                await wait.add_reaction(al[i])
        except Exception as e:
            await wait.edit(content=str(self.client.get_emoji(BotEmotes.error)) + f' | An error occured!\nReport this using {prefix}feedback.\n```{e}```')
        guy = ctx.message.author
        def check(reaction, user):
            return user == guy
        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await main.add_reaction('😔')
        if str(reaction.emoji)==str(corr):
            await ctx.send(str(self.client.get_emoji(BotEmotes.success)) +' | <@'+str(guy.id)+'>, Congrats! You are correct. :partying_face:')
            if Economy.get(ctx.author.id)!=None:
                reward = random.randint(250, 400)
                Economy.addbal(ctx.message.author.id, reward)
                await ctx.send('thanks for playing! You get also a '+str(reward)+' diamonds as a prize!')
        else:
            await ctx.send(str(self.client.get_emoji(BotEmotes.error)) +' | <@'+str(guy.id)+'>, You are incorrect. The answer is '+str(corr)+'.')

def setup(client):
    client.add_cog(games(client))