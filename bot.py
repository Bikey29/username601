import username601 as myself
from username601 import *
import discordgames
import splashes

print('Please wait...')
import json
import pokebase as pb
from discord.ext import commands
from discord.ext.commands import Bot
import datetime
latest_update = datetime.datetime.now()
import os
import discord
import wikipediaapi
import urllib
import random
import sys
import imdb
import asyncio
import math
import requests
from googletrans import Translator, LANGUAGES
gtr = Translator()
client = discord.Client()
ia = imdb.IMDb()

@client.event
async def on_ready():
    print('Bot is online.\n=== USERNAME601 CONSOLE ===\nBuilt using Python by Viero Fernando (c) 2020.\n\n'.format(client))
    while True:
        await asyncio.sleep(10)
        myAct = discord.Activity(name=str(len(client.users))+' strangers in '+str(len(client.guilds))+' cults.', type=discord.ActivityType.watching)
        await client.change_presence(activity=myAct)
@client.event
async def on_message(message):
    if '<@!696973408000409626>' in message.content or '<@696973408000409626>' in message.content:
        await message.channel.send('The prefix is `'+str(prefix)+'`.\n**Commands: **`'+prefix+'help`')
    if message.content==prefix+"ping":
        wait = await message.channel.send('Pinging... :thinking:')
        ping = str(round(client.latency*1000))
        if int(ping)<100:
            embed = discord.Embed(title=f'Pong! {ping} ms.', colour=discord.Colour.red())
        else:
            embed = discord.Embed(title=f'Pong! {ping} ms.', description='Ping time may be slower due to;\n1. People kept spamming me\n2. My hosting system is slow\n3. I am in too many servers\n4. Discord\'s servers are currectly down\n5. I am snail :snail:', colour=discord.Colour.red())
        embed.set_thumbnail(url='https://i.pinimg.com/originals/21/02/a1/2102a19ea556e1d1c54f40a3eda0d775.gif')
        embed.set_footer(text='Ping and embed sent time may differ.')
        await wait.edit(content='', embed=embed)
    sayTag = splashes.getTag()
    msgAuthor = str(message.author)[:-5]
    authorTag = message.author.id
    msg = message.content.lower()
    null = " "
    splitted = message.content.split()
    i_dont_know_what_this_means_but_i_am_declaring_it_anyway = 0
    if '<@!696973408000409626>' in msg and msg.startswith(prefix):
        i_dont_know_what_this_means_but_i_am_declaring_it_anyway = 1
        await message.channel.send(random.choice(sayTag))
    elif msg.startswith(prefix) and i_dont_know_what_this_means_but_i_am_declaring_it_anyway==0 and client.get_user(int(authorTag)).bot==False and len(splitted[0])!=1:
        if msg.startswith(prefix+'say'):
            await message.channel.send(msg[5:])
        if msg.startswith(prefix+'hack'):
            if len(splitted)==1:
                await message.channel.send(f'Please tag someone!\nExample: {prefix}hack <@'+str(authorTag)+'>')
            else:
                tohack = message.mentions[0]
                console = 'C:\\Users\\Anonymous601>'
                if splitted[1].startswith('<@'):
                    flow = [
                        '0hack.exe -u '+str(tohack.name)+' -a',
                        '0\n[hack.exe] Opening hack prompt...',
                        '0\n[hack.exe] Opening http://discord.com/hack/'+myself.randomhash(),
                        '1\n[hack.exe] USER DETECTED: '+tohack.name+'. HACKING USER... ',
                        '1done',
                        '1\n[hack.exe] RETRIEVING IP ADDRESS... ',
                        '1done. IP: 99.238.'+str(tohack.discriminator)+'.1729.10',
                        '1\n[hack.exe] ACCESSING DEVICE FROM DISCORD... ',
                        '1done.',
                        '1\n[DEVICE ID:'+str(tohack.discriminator)+'] ACCESS GRANTED',
                        '1\n[hack.exe] GETTING FACECAM...',
                        '2success.',
                        '2\n[hack.exe] SPREADING FACECAM TO DARK WEB...',
                        '2done.',
                        '1\n[hack.exe] GETTING EMAIL INFO...',
                        '1done.',
                        '4\nEMAIL: '+splashes.email(tohack.name)+'@hacked.com\nPASSWORD: "'+splashes.password(tohack.name)+'"',
                        '1\n[hack.exe] SPREADING INFO TO '+myself.randomhash()+'.onion...',
                        '1done.',
                        '1\n[hack.exe] GETTING SENSITIVE PERSONAL INFORMATION...',
                        '4done.\nLAST MESSAGE: "'+splashes.lastmsg(tohack.name)+'"\nLAST BROWSING HISTORY: "'+splashes.history(tohack.name)+'"\n[hack.exe] DISTRIBUTING INFO TO FBI AND NSA...',
                        '3done.',
                        '0\n[hack.exe] HACK COMPLETE.',
                        '0\n\nC:\\Users\\Anonymous601>'
                    ]
                    main = await message.channel.send('Opening Console...')
                    for i in range(0, len(flow)):
                        console = console + flow[i][1:]
                        newembed = discord.Embed(title='Anonymous601 Hacking Console', description=f'```{console}```',colour=discord.Colour.green())
                        if flow[i].startswith('1'):
                            newembed.set_thumbnail(url='https://i.imgur.com/msmvE09.gif')
                        elif flow[i].startswith('2'):
                            newembed.set_thumbnail(url=tohack.avatar_url)
                        elif flow[i].startswith('3'):
                            newembed.set_thumbnail(url='https://seeklogo.com/images/F/FBI_SHIELD-logo-2D02BDDAC8-seeklogo.com.png')
                        elif flow[i].startswith('4'):
                            newembed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/ByHvJcnlhVe42B9bjwf9umFHeEA5pk1oebLdxeWYY0g/%3Fv%3D1/https/cdn.discordapp.com/emojis/704242063725559868.png')
                        else:
                            newembed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/5/50/Black_colour.jpg')
                        await main.edit(content='', embed=newembed)
                        await asyncio.sleep(random.randint(2, 4))
                else:
                    console = console + 'hack.exe -u '+str(msgAuthor)+'\nERROR: INVALID TAG.\nACCESS DENIED.\n\nHash encoded base64 cipher code:\n'+myself.bin(msgAuthor)+ '\n' + console
                    embed = discord.Embed(title='Anonymous601 Hacking Console', description=f'```{console}```',colour=discord.Colour.green())
                    await message.channel.send(embed=embed)
        if msg.startswith(prefix+'base64'):
            if len(splitted)==1:
                await message.channel.send(f'Please input something to encode! Like `{prefix}base64 discord.py is better than discord.js`')
            else:
                toencode = message.content[int(len(splitted[0])+1):]
                await message.channel.send(f'```{myself.encodeb64(toencode)}```')
        if msg.startswith(prefix+'ufo'):
            num = str(random.randint(50, 100))
            data = json.loads(urllib.request.urlopen('http://ufo-api.herokuapp.com/api/sightings/search?limit='+num).read())
            if data['status']!='OK':
                await message.channel.send('There was a problem on retrieving the info.\nThe server said: "'+str(data['status'])+'" :eyes:')
            else:
                ufo = random.choice(data['sightings'])
                embed = discord.Embed(title='UFO Sighting in '+str(ufo['city'])+', '+str(ufo['state']), description='**Summary:** '+str(ufo['summary'])+'\n\n**Shape:** '+str(ufo['shape'])+'\n**Sighting Date: **'+str(ufo['date'])[:-8].replace('T', ' ')+'\n**Duration: **'+str(ufo['duration'])+'\n\n[Article Source]('+str(ufo['url'])+')', colour=discord.Colour.green())
                embed.set_footer(text='Username601 raided Area 51 and found this!')
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'embed'):
            if '(title:' not in msg or '(desc:' not in msg:
                await message.channel.send('An embed requires title and description.\nFor example: `'+prefix+'embed (title:this is a title) (desc:this is a description)`\n\nOptional; `footer, auth, hex`')
            else:
                try:
                    title_e = msg.split('(title:')[1].split(')')[0]
                    desc_e = msg.split('(desc:')[1].split(')')[0]
                    if '(footer:' in msg:
                        foot = msg.split('(footer:')[1].split(')')[0]
                        embed.set_footer(text=foot)
                    if '(auth:' in msg:
                        auth = msg.split('(auth:')[1].split(')')[0]
                        embed.set_author(name=auth)
                    if '(hex:' not in msg:
                        embed = discord.Embed(title=title_e, description=desc_e, colour=discord.Colour.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
                    else:
                        if msg.split('(hex:')[1].split(')')[0].startswith('#'):
                            hexer = msg.split('(hex:')[1].split(')')[0][1:]
                        else:
                            hexer = msg.split('(hex:')[1].split(')')[0]
                        arr = myself.convertrgb(hexer, '0')
                        embed = discord.Embed(title=title_e, description=desc_e, colour=discord.Colour.from_rgb(arr[0], arr[1], arr[2]))
                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f'An error occurd. For programmers: ```{e}```')
        if msg.startswith(prefix+'pokequiz'):
            wait = await message.channel.send('Please wait... Generating quiz...')
            num = random.randint(1, 800)
            try:
                corr = pb.pokemon(str(num)).name
            except Exception as e:
                await wait.edit(content=f'An error occured! ```{e}```')
            hint = 2
            attempt = 10
            gameplay = True
            guy = message.author
            while gameplay==True:
                newembed = discord.Embed(title='Pokemon Quiz!', description=f'Guess the pokemon\'s name!\nTimeout: 45 seconds.\nHint left: **{str(hint)}** | Attempts left: **{str(attempt)}**', colour=discord.Colour.green())
                newembed.set_image(url=f'https://assets.pokemon.com/assets/cms2/img/pokedex/full/{str(num)}.png')
                newembed.set_footer(text='Type "hint" to give.. uh... the HINT! :D')
                newembed.set_thumbnail(url=f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{str(num)}.png')
                await wait.edit(content='', embed=newembed)
                if int(attempt)<1:
                    await message.channel.send('You lose! The pokemon is **'+str(corr)+'**!')
                    gameplay = False
                    break
                def checking(m):
                    return m.author == guy
                try:
                    guessing = await client.wait_for('message', check=checking, timeout=45.0)
                except asyncio.TimeoutError:
                    attempt = int(attempt) - 1
                    await message.channel.send('Too late! Game ended... :pensive:')
                    gameplay = False
                    break
                if str(guessing.content).lower()==corr:
                    currentmsg = guessing
                    await currentmsg.add_reaction('✅')
                    await message.channel.send('You are correct! The pokemon is **'+str(corr)+'**')
                    gameplay = False
                    break
                elif str(guessing.content).lower()=='hint':
                    currentmsg = guessing
                    if hint<1:
                        await currentmsg.add_reaction('❌')
                        attempt = int(attempt) - 1
                    else:
                        await currentmsg.add_reaction('✅')
                        thehint = random.choice([myself.hintify(corr), 'Pokemon name starts with "'+str(list(corr)[0])+'"', 'Pokemon name has '+str(len(corr))+' letters!', 'Pokemon name ends with "'+str(list(corr)[len(corr)-1])+'"'])
                        await message.channel.send('Hint: '+thehint+'!')
                        hint = int(hint) - 1
                        attempt = int(attempt) - 1
                else:
                    if attempt!=0:
                        await guessing.add_reaction('❌')
                        attempt = int(attempt) - 1
                    else:
                        await guessing.add_reaction('❌')
                        await message.channel.send('You lose! The pokemon is **'+str(corr)+'**!')
                        gameplay = False
                        break
        if msg.startswith(prefix+'ss'):
            if len(splitted)>1:
                if splitted[1]=='--help':
                    embed = discord.Embed(title='Special say command help', description='**REQUIRES `MANAGE CHANNELS` PERMISSION**\nThis is a special say command that has the following:\n1. @someone | Tags random people in the server. [On April fools 2018, Discord made this feature, but removed the day after.](https://www.youtube.com/watch?v=BeG5FqTpl9U) (Please use wisely.)\n2. @owner | Tags the server owner. Please don\'t spam this feature.\n3. --ch #{channelname} | Sends a message on a specific channel.', colour=discord.Colour.green())
                    await message.channel.send(embed=embed)
                else:
                    if message.guild.get_member(int(authorTag)).guild_permissions.manage_channels==False:
                        await message.channel.send('You need to have the `Manage channels` permission. :x:')
                    else:
                        randomppl = random.choice(message.guild.members).id
                        if splitted[1]=='--ch':
                            # ummm
                            try:
                                ch = client.get_channel(int(splitted[2][2:][:-1]))
                                await ch.send(msg[int(len(splitted[0])+len(splitted[1])+len(splitted[2])+3):].replace('@someone', '<@'+str(randomppl)+'>').replace('@owner', '<@'+str(message.guild.owner.id)+'>'))
                            except:
                                await message.channel.send('An error occured! :x:')
                        else:
                            await message.channel.send(msg[int(len(splitted[0])+1):].replace('@someone', f'<@{str(randomppl)}>').replace('@owner', '<@'+str(message.guild.owner.id)+'>'))
        if msg.startswith(prefix+'inspectservers'):
            if int(authorTag)==661200758510977084:
                ee = ''
                for i in range(0, len(client.guilds)):
                    ee = ee + '**' + client.guilds[i].name + '** ('+str(len(client.guilds[i].members))+' Members)\n'
                embed = discord.Embed(title='Heya, here are all the servers i am in.', description=ee, colour=discord.Colour.blue())
                await message.author.send(embed=embed)
                await message.channel.send('...k')
            else:
                await message.channe.send('...')
        if msg.startswith(prefix+'hangman'):
            wait = await message.channel.send('Please wait... generating... :flushed:')
            response = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?number=1")
            the_word = json.loads(response.read())[0]
            main_guess_cor = list(the_word)
            main_guess_hid = []
            server_id = message.guild.id
            wrong_guesses = ''
            for i in range(0, len(main_guess_cor)):
                main_guess_hid.append('\_ ')
            gameplay = True
            guessed = []
            level = 0
            playing_with = message.author
            playing_with_id = int(authorTag)
            while gameplay==True:
                if message.content==prefix+'hangman' and message.author.id!=int(playing_with_id) and message.guild.id==server_id:
                    await message.channel.send('<@'+str(authorTag)+'>, cannot play hangman when a game is currently playing!')
                newembed = discord.Embed(title=''.join(main_guess_hid), description='Wrong guesses: '+str(wrong_guesses), colour=discord.Colour.red())
                newembed.set_image(url=f'https://raw.githubusercontent.com/vierofernando/username601/master/assets/hangman_{str(level)}.png')
                newembed.set_footer(text='Type "showanswer" to show the answer and end the game.')
                await message.channel.send(embed=newembed)
                if '\_ ' not in ''.join(main_guess_hid):
                    await message.channel.send(f'Congratulations! <@{str(playing_with_id)}> win! :tada:\nThe answer is "'+str(''.join(main_guess_cor))+'".')
                    gameplay = False
                    break
                if level>7:
                    await message.channel.send(f'<@{str(playing_with_id)}> lost! :(\nThe answer is actually "'+str(''.join(main_guess_cor))+'".')
                    gameplay = False
                    break
                def is_not_stranger(m):
                    return m.author == playing_with
                try:
                    trying = await client.wait_for('message', check=is_not_stranger, timeout=20.0)
                except asyncio.TimeoutError:
                    await message.channel.send(f'<@{str(playing_with_id)}> did not response in 20 seconds so i ended the game. Keep un-AFK!\nOh and btw, the answer is '+str(''.join(main_guess_cor))+'. :smirk:')
                    gameplay = False
                    break
                if str(trying.content).lower()=='showanswer':
                    await message.channel.send('The answer is actually '+str(''.join(main_guess_cor)+'.'))
                    gameplay = False
                    break
                elif len(str(trying.content))>1:
                    await message.channel.send('One word at a time. Game ended :rage:')
                    gameplay = False
                    break
                elif str(trying.content).lower() in guessed:
                    await message.channel.send(f'<@{str(playing_with_id)}>, You have guessed that letter!')
                    level = int(level)+1
                elif str(trying.content).lower() in ''.join(main_guess_cor).lower():
                    guessed.append(str(trying.content).lower())
                    for i in range(0, len(main_guess_cor)):
                        if main_guess_cor[i].lower()==str(trying.content).lower():
                            main_guess_hid[i] = str(trying.content).lower()
                else:
                    level = int(level) + 1
                    wrong_guesses = wrong_guesses + str(trying.content).lower() + ', '
        if msg.startswith(prefix+'tictactoe'):
            box_nums = list('123456789')
            can_used = list('123456789')
            box = f' {box_nums[0]} | {box_nums[1]} | {box_nums[2]}\n===========\n {box_nums[3]} | {box_nums[4]} | {box_nums[5]}\n===========\n {box_nums[6]} | {box_nums[7]} | {box_nums[8]}\n'
            if len(splitted)==1:
                embed = discord.Embed(title='TicTacToe™ wtih '+str(splashes.getTicTacToeHeader()), description=f'Plays tic-tac-toe with the BOT. Very simple.\n\n**To start playing, type;**\n`{prefix}tictactoe X` (To play tictactoe as X)\n`{prefix}tictactoe O` (To play tictactoe as O)', colour=discord.Colour.red())
                embed.set_image(url='https://raw.githubusercontent.com/vierofernando/username601/master/assets/tictactoe.png')
                await message.channel.send(embed=embed)
            else:
                if splitted[1].lower() not in list('xo'):
                    await message.channel.send('Must be X or O!')
                else:
                    if splitted[1].lower()=='x':
                        user_sym = 'X'
                        bot_sym = 'O'
                    else:
                        user_sym = 'O'
                        bot_sym = 'X'
                    playing_with = message.author
                    user_id = int(authorTag)
                    user_name = message.guild.get_member(user_id).display_name
                    gameplay = True
                    usedByUser = []
                    usedByBot = []
                    embed = discord.Embed(title='Playing Tictactoe with '+str(user_name), description=f'Viero Fernando ({user_sym}) | Username601 ({bot_sym})\nType the numbers to fill out the boxes.```{box}```', colour=discord.Colour.green())
                    embed.set_footer(text='Type "endgame" to well, end the game. Or wait for 20 seconds and the game will kill itself! ;)')
                    gameview = await message.channel.send(embed=embed)
                    while gameplay==True:
                        if discordgames.checkWinner(box_nums, user_sym, bot_sym)=='userwin':
                            await message.channel.send(f'Congrats <@{user_id}>! You won against me! :tada:')
                            gameplay = False
                            break
                        elif discordgames.checkWinner(box_nums, user_sym, bot_sym)=='botwin':
                            await message.channel.send(f'LOL, i win the tic tac toe! :tada:\nYou lose! :pensive:')
                            gameplay = False
                            break
                        elif discordgames.checkEndGame(can_used)==True:
                            await message.channel.send('Nobody wins? OK... :neutral_face:')
                            gameplay = False
                            break
                        def is_not_stranger(m):
                            return m.author == playing_with
                        try:
                            trying = await client.wait_for('message', check=is_not_stranger, timeout=20.0)
                        except asyncio.TimeoutError:
                            await message.channel.send(f'<@{user_id}> did not response in 20 seconds so i ended the game. Keep un-AFK!')
                            gameplay = False
                            break
                        if str(trying.content) in can_used:
                            for i in range(0, len(box_nums)):
                                if box_nums[i]==trying.content:
                                    usedByUser.append(box_nums[i])
                                    box_nums[i] = user_sym
                                    for j in range(0, len(can_used)):
                                        if j==box_nums[i]:
                                            del can_used[j]
                                            break
                                    break
                            # BOT ACTION
                            bot_select = ''
                            while bot_select=='' and len(can_used)>1:
                                bot_select = random.choice(can_used)
                            print('I SELECT: '+bot_select)
                            for i in range(0, len(can_used)):
                                if can_used[i]==bot_select:
                                    for j in range(0, len(box_nums)):
                                        if box_nums[j]==can_used[i]:
                                            box_nums[j] = bot_sym
                                            break
                                    usedByBot.append(can_used[i])
                                    del can_used[i]
                                    break
                            box = f' {box_nums[0]} | {box_nums[1]} | {box_nums[2]}\n===========\n {box_nums[3]} | {box_nums[4]} | {box_nums[5]}\n===========\n {box_nums[6]} | {box_nums[7]} | {box_nums[8]}\n'
                            newembed = discord.Embed(title='Playing Tictactoe with '+str(user_name), description=f'Viero Fernando ({user_sym}) | Username601 ({bot_sym})\nType the numbers to fill out the boxes.```{box}```', colour=discord.Colour.green())
                            newembed.set_footer(text='Type "endgame" to well, end the game. Or wait for 20 seconds and the game will kill itself! ;)')
                            await message.channel.send(embed=newembed)
                        elif str(trying.content).lower()=='endgame':
                            await message.channel.send('Game ended.')
                            gameplay = False
                            break
        if msg.startswith(prefix+'randomavatar'):
            gibb_name = ''
            for i in range(0, random.randint(5, 10)):
                gibb_name = gibb_name + random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_image(url=f'https://api.adorable.io/avatars/285/{gibb_name}.png')
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'mathquiz'):
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            symArray = ['+', '-', 'x', ':', '^']
            ansArray = [num1+num2, num1-num2, num1*num2, num1/num2, num1**num2]
            arrayId = random.randint(0, 4)
            sym = symArray[arrayId]
            await message.channel.send('**MATH QUIZ (15 seconds)**\n'+str(num1)+' '+str(sym)+' '+str(num2)+' = ???')
            def is_correct(m):
                return m.author == message.author
            answer = int(ansArray[arrayId])
            try:
                trying = await client.wait_for('message', check=is_correct, timeout=15.0)
            except asyncio.TimeoutError:
                return await message.channel.send(':pensive: No one? Okay then, the answer is: {}.'.format(answer))
            if str(trying.content)==str(answer):
                await message.channel.send('<@'+str(authorTag)+'>, You are correct! :tada:')
            else:
                await message.channel.send('<@'+str(authorTag)+'>, Incorrect. The answer is {}.'.format(answer))
        if msg.startswith(prefix+'guessavatar'):
            if len(message.guild.members)>500:
                await message.channel.send('Sorry, to protect some people\'s privacy, this command is not available for Large servers. (over 500 members)')
            else: #getting data from guild
                wait = await message.channel.send('Please wait... generating question...\nThis process may take longer if your server has more members.')
                avatarAll = []
                nameAll = []
                for ppl in message.guild.members:
                    if message.guild.get_member(int(ppl.id)).status.name!='offline':
                        avatarAll.append(str(ppl.avatar_url).replace('webp', 'png'))
                        nameAll.append(ppl.display_name)
                if len(avatarAll)<=4:
                    await message.channel.send('Too less online members! :x:')
                else:
                    # randomization time!
                    numCorrect = random.randint(0, len(avatarAll)-1)
                    corr_avatar = avatarAll[numCorrect] # avatar to be shown on question
                    corr_name = nameAll[numCorrect] # correct answer
                    nameAll.remove(corr_name) # remove correct answer from array
                    wrongArr = []
                    for i in range(0, 3): # randomly select random name as wrong answers
                        wrongArr.append(random.choice(nameAll))
                    # sub-question/before creating the embed
                    abcs = list('ABCD')
                    randomInt = random.randint(0, 3)
                    corr_order = random.choice(abcs[randomInt])
                    abcs[randomInt] = '0'
                    question = '' # the actual choose
                    chooseCount = 0
                    for assign in abcs:
                        if assign!='0':
                            question = question + '**'+ str(assign) + '.** '+str(wrongArr[chooseCount])+ '\n'
                            chooseCount = int(chooseCount) + 1
                        else:
                            question = question + '**'+ str(corr_order) + '.** '+str(corr_name)+ '\n'
                    embed = discord.Embed(title='What does the avatar below belongs to?', description=':eyes: Reply with `a`, `b`, `c`, or `d`! **You have 20 seconds.**\n\n'+str(question), colour=discord.Colour.green())
                    embed.set_footer(text='For privacy reasons, the people displayed above are online users.')
                    embed.set_image(url=corr_avatar)
                    await wait.edit(content='', embed=embed)
                    # begin ticking
                    def is_correct(m):
                        return m.author == message.author
                    try:
                        tryin = await client.wait_for('message', check=is_correct, timeout=20.0)
                        trying = str(tryin.content).lower()
                    except asyncio.TimeoutError:
                        return await message.channel.send(':pensive: No one? Okay then, the answer is: '+str(corr_order)+'. '+str(corr_name))
                    if trying==str(corr_order).lower():
                        await message.channel.send('<@'+str(authorTag)+'>, You are correct! :tada:')
                    else:
                        await message.channel.send('<@'+str(authorTag)+'>, Incorrect. The answer is '+str(corr_order)+'. '+str(corr_name))
        if msg.startswith(prefix+'geoquiz'):
            wait = await message.channel.send('Please wait... generating question...')
            response = urllib.request.urlopen("https://restcountries.eu/rest/v2/")
            data = json.loads(response.read())
            topic = random.choice(splashes.getGeoQuiz())
            chosen_nation_num = random.randint(0, len(data))
            chosen_nation = data[chosen_nation_num]
            data.remove(data[chosen_nation_num])
            wrongs = []
            correct = str(chosen_nation[topic])
            for i in range(0, 4):
                integer = random.randint(0, len(data))
                wrongs.append(str(data[integer][str(topic)]))
                data.remove(data[integer])
            abcs = list('ABCD')
            corr_order_num = random.randint(0, 3)
            corr_order = abcs[corr_order_num]
            abcs[corr_order_num] = '0'
            question = ''
            for alph in abcs:
                if alph!='0':
                    added = random.choice(wrongs)
                    question = question + '**' + alph + '.** ' + added + '\n'
                    wrongs.remove(added)
                else:
                    question = question + '**' + corr_order + '.** ' + correct + '\n'
            embed = discord.Embed(title='Geography: '+str(topic)+' quiz!', description=':nerd: Reply with `a`, `b`, `c`, or `d`! **You have 17 seconds.**\n\nWhich '+str(topic)+' belongs to '+str(chosen_nation['name'])+'?\n'+str(question), colour=discord.Colour.blue())
            await wait.edit(content='', embed=embed)
            def is_correct(m):
                return m.author == message.author
            try:
                tryin = await client.wait_for('message', check=is_correct, timeout=17.0)
                trying = str(tryin.content).lower()
            except asyncio.TimeoutError:
                return await message.channel.send(':thinking: No one? Okay then, the answer is: '+str(corr_order)+'. '+str(correct))
            if trying==str(corr_order).lower():
                await message.channel.send('<@'+str(authorTag)+'>, You are correct! :tada:')
            else:
                await message.channel.send('<@'+str(authorTag)+'>, :rage: Go to detention. The correct answer is '+str(corr_order)+'. '+str(correct)+'.')
        if msg.startswith(prefix+'emojiimg'):
            if len(splitted)==1:
                await message.channel.send('Please send a custom emoji!')
            elif len(splitted)==2:
                emoji = splitted[1].split(':')
                try:
                    emoji_id = emoji[2][:-1]
                except IndexError:
                    accept = False
                    await message.channel.send(':x: For some reason, we cannot proccess default emojis. Sorry!')
                try:
                    if client.get_emoji(int(emoji_id)).animated==False:
                        link = 'https://cdn.discordapp.com/emojis/'+str(emoji_id)+'.png?v=1'
                        accept = True
                    else:
                        await message.channel.send(':x: Error processing it.')
                        accept = False
                except:
                    await message.channel.send(':x: Oops! There are an error *for some reason.*')
                if accept==True:
                    embed = discord.Embed(title='Emoji pic for ID of '+str(emoji_id), colour=discord.Colour.red())
                    embed.set_image(url=link)
                    await message.channel.send(embed=embed)
            else:
                await message.channel.send('Invalid parameters.')
        if msg.startswith(prefix+'ban'):
            begin = True
            if len(splitted)<2:
                await message.channel.send(':rage: Please mention someone!')
                begin = False
            else:
                perms = message.guild.get_member(int(authorTag)).guild_permissions.ban_members
                if perms==False:
                    begin = False
                    await message.channel.send(f'<@{str(authorTag)}>, you don\'t have the `Ban Members` permission! :rage:')
                else:
                    try:
                        if splitted[1].startswith('<@!'):
                            criminal = message.guild.get_member(int(splitted[1][3:][:-1]))
                        else:
                            criminal = message.guild.get_member(int(splitted[1][2:][:-1]))
                        if criminal.id==authorTag:
                            await message.channel.send(':rage: What a weirdo. Banning yourself.')
                            begin = False
                    except:
                        await message.channel.send(':rage: Invalid mention.')
                    if criminal.guild_permissions.administrator==True or criminal.guild_permissions.manage_guild==True or criminal.guild_permissions.manage_channels==True or criminal.guild_permissions.manage_permissions==True:
                        await message.channel.send(':rage: You want me to ban a **MODERATOR/ADMIN?!**')
                        begin = False
                    if begin==True:
                        if len(splitted)<3:
                            reas = 'Unspecified'
                        else:
                            reas = msg[int(len(splitted[1])+len(splitted[0])+2):]
                        try:
                            await message.guild.ban(criminal, reason=reas)
                            msgs = [
                                "It is time. "+criminal.name+".",
                                criminal.name+", Get. OUT.",
                                "[BOT] Successfully executed kill"+criminal.name+"().",
                                'It was fun, now is time for '+criminal.name+' to leave.',
                                'We don\'t even need '+criminal.name+' anymore.',
                                'Bye bye, '+criminal.name+'.'
                            ]
                            await message.channel.send(random.choice(msgs))
                        except:
                            await message.channel.send(':thinking: There was an error on banning '+criminal.name+'.')
        if msg.startswith(prefix+'feedback'):
            if len(splitted)<2:
                await message.channel.send('Where\'s the feedback? :(')
            elif len(list(splitted))>1000:
                await message.channel.send('That\'s too long! Please provide a simpler description.')
            else:
                try:
                    fb = msg[int(len(splitted[0])+1):]
                    feedbackCh = client.get_channel(706459051034279956)
                    await feedbackCh.send(str(message.author)+' (ID: '+str(message.author.id)+') sent a feedback: **"'+str(fb)+'"**')
                    embed = discord.Embed(title='Feedback Successful', description='Thanks for the feedback!\nIf issue still continue, [Please join our support server](https://discord.gg/HhAPkD8) and give us more details.',colour=discord.Colour.green())
                    await message.channel.send(embed=embed)
                except:
                    await message.channel.send('Error: There was an error while sending your feedback. Sorry! :(')
        if msg.startswith(prefix+'gdlevel'):
            if len(splitted)<2:
                await message.channel.send(':x: Please enter a level ID!')
            else:
                if splitted[1].isnumeric()==False:
                    await message.channel.send(':x: That is not a level ID!')
                else:
                    try:
                        levelid = str(splitted[1])
                        toEdit = await message.channel.send("Retrieving Data...")
                        response = urllib.request.urlopen("https://gdbrowser.com/api/level/"+str(levelid))
                        data = json.loads(response.read())
                        responseLeaderboard = urllib.request.urlopen("https://gdbrowser.com/api/leaderboardLevel/"+str(data["id"]))
                        leader = json.loads(responseLeaderboard.read())
                        image = 'https://gdbrowser.com/icon/'+data["author"]
                        embed = discord.Embed(
                            title = data["name"]+' ('+data["id"]+')',
                            description = data["description"],
                            colour = discord.Colour.blue()
                        )
                        embed.set_author(name=data["author"], icon_url=image)
                        embed.add_field(name='Difficulty', value=data["difficulty"])
                        gesture = ':+1:'
                        if data['disliked']==True:
                            gesture = ':-1:'
                        embed.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
                        embed.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
                        embed.add_field(name='Leaderboard', value="**Rank #1: "+str(leader[1]["username"])+"** "+str(leader[1]["percent"])+"% | "+str(leader[1]["date"])+"\n**Rank #2: "+str(leader[2]["username"])+"** "+str(leader[2]["percent"])+"% | "+str(leader[2]["date"])+"\n**Rank #3: "+str(leader[3]["username"])+"** "+str(leader[3]["percent"])+"% | "+str(leader[3]["date"]))
                        await toEdit.edit(content='', embed=embed)
                    except:
                        embedTemp = discord.Embed(
                            title = data["name"]+' ('+data["id"]+')',
                            description = data["description"],
                            colour = discord.Colour.blue()
                        )
                        embedTemp.set_author(name=data["author"], icon_url=image)
                        embedTemp.add_field(name='Difficulty', value=data["difficulty"])
                        gesture = ':+1:'
                        if data['disliked']==True:
                            gesture = ':-1:'
                        embedTemp.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
                        embedTemp.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
                        embedTemp.set_footer(text='Info given is less because the level has less.. info.')
                        await toEdit.edit(content='', embed=embedTemp)
        if msg.startswith(prefix+'gdsearch'):
            if len(splitted)<2:
                await message.channel.send(':x: Please input a query!')
            else:
                try:
                    query = msg[int(len(splitted[0])+1):].replace(' ', '%20')
                    data = json.loads((urllib.request.urlopen('https://gdbrowser.com/api/search/'+str(query))).read())
                    levels = ''
                    count = 0
                    for i in range(0, len(data)):
                        if data[count]['disliked']==True:
                            like = ':-1:'
                        else:
                            like = ':+1:'
                        levels = levels + str(count+1)+'. **'+data[count]['name']+'** by '+data[count]['author']+' (`'+data[count]['id']+'`)\n:arrow_down: '+data[count]['downloads']+' | '+like+' '+data[count]['likes']+'\n'
                        count = int(count) + 1
                    embedy = discord.Embed(title='Geometry Dash Level searches for "'+str(query).replace('%20', ' ')+'":', description=levels, colour=discord.Colour.blue())
                    await message.channel.send(embed=embedy)
                except:
                    await message.channel.send(':x: Error: Not Found. :four::zero::four:')
        if msg.startswith(prefix+'emojiinfo'):
            test = 0
            if test==0:
                try:
                    erry = False
                    emojiid = int(splitted[1].split(':')[2][:-1])
                    data = client.get_emoji(emojiid)
                except:
                    erry = True
                    await message.channel.send(':x: For some reason, we cannot process your emoji ;(')
                if erry==False:
                    if data.animated==True:
                        anim = 'This emoji is an animated emoji. **Only nitro users can use it.**'
                    else:
                        anim = 'This emoji is a static emoji. **Everyone can use it (except if limited by role)**'
                    embedy = discord.Embed(title='Emoji info for :'+str(data.name)+':', description='**Emoji name:** '+str(data.name)+'\n**Emoji ID: **'+str(data.id)+'\n'+anim+'\n**Emoji\'s server ID: **'+str(data.guild_id)+'\n**Emoji creation time: **'+str(data.created_at)[:-7]+' UTC.', colour=discord.Colour.magenta())
                    embedy.set_thumbnail(url='https://cdn.discordapp.com/emojis/'+str(data.id)+'.png?v=1')
                    await message.channel.send(embed=embedy)
        if msg.startswith(prefix+'clear') or msg.startswith(prefix+'purge'):
            checky = message.guild.get_member(int(authorTag)).guild_permissions.manage_messages
            if checky==False:
                await message.channel.send(':x: You don\'t have the permission `Manage Messages` to do this command \>:(')
            else:
                contin = True
                try:
                    count = int(splitted[1])+1
                    if count>500:
                        await message.channel.send('That\'s **TOO MANY** messages to be deleted!\nJust clone the channel and delete the old one.\neasy peasy.')
                        contin = False
                except:
                    await message.channel.send('That is NOT a number!')
                    contin = False
                if contin==True:
                    try:
                        await message.channel.purge(limit=count)
                    except:
                        await message.channel.send(':x: An error occured during purging.')
        if splitted[0]==prefix+'s':
            await message.delete()
            member = message.guild.get_member(int(authorTag))
            if member.guild_permissions.administrator==True or int(authorTag)==661200758510977084:
                accept = True
            else:
                await message.channel.send(':x: <@'+str(authorTag)+'>, To do this command, you need to have `Administrator` permission,\nOr be the bot owner.')
                accept = False
            if accept==True:
                await message.channel.send(msg[3:])
        if msg.startswith(prefix+'addrole') or splitted[0]==prefix+'ar':
            if message.guild.get_member(int(authorTag)).guild_permissions.manage_roles==False:
                await message.channel.send(f'<@{str(authorTag)}>, you don\'t have the `Manage Roles` permission!')
            else:
                try:
                    if splitted[1].startswith('<@!'):
                        permId = int(splitted[1][3:][:-1])
                    else:
                        permId = int(splitted[1][2:][:-1])
                except ValueError:
                    await message.channel.send('Error: Invalid tag!')
                aruser = message.guild.get_member(int(permId))
                try:
                    toadd = message.guild.get_role(int(splitted[2][3:][:-1]))
                    await aruser.add_roles(toadd)
                    await message.channel.send('Congratulations, '+aruser.name+', you now have the '+toadd.name+' role! :tada:')
                except Exception as e:
                    await message.channel.send(f'An error occured. :x:```{e}```')
        if msg.startswith(prefix+'xpbox'):
            results = []
            buttons = []
            ques = [
                'Please input the box title.',
                'Please input the message to display.',
                'How many buttons shall be in the message box?'
            ]
            auth = message.author
            accept = True
            for i in range(0, 3):
                await message.channel.send(ques[i])
                def check(m):
                    return m.author == auth
                try:
                    trying = await client.wait_for('message', check=check, timeout=30.0)
                except:
                    await message.channel.send('Command canceled. No response after 30 seconds.')
                if '/' in str(trying.content) or '?' in str(trying.content) or '&' in str(trying.content):
                    await message.channel.send('Your request contain an invalid symbol. Please try again.')
                    accept = False
                    break
                else:
                    results.append(str(trying.content))
                    if len(results)>2:
                        for i in range(1, results[3]+1):
                            nds = ['st', 'nd', 'rd']
                            await message.channel.send('Please input the '+str(i)+str(nds[i-1])+' button.')
                            def checkingagain(m):
                                return m.author == auth
                            try:
                                buttonInput = await client.wait_for('message', check=checkingagain, timeout=30.0)
                            except:
                                await message.channel.send('Command canceled. No response after 30 seconds.')
                                accept = False
                                break
                            buttons.append(str(trying.content))
            if accept==True:
                embed = discord.Embed(title='Error!', colour=discord.Colour.red())
                embed.set_image(url='http://atom.smasher.org/error/xp.png.php?icon=Error3&style=xp&title='+str(results[0]).replace(' ', '+')+'&text='+str(results[1]).replace(' ', '+')+'&b1='+str(results[2]).replace(' ', '+'))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'removerole') or splitted[0]==prefix+'rr':
            if message.guild.get_member(int(authorTag)).guild_permissions.manage_roles==False:
                await message.channel.send(f'<@{str(authorTag)}>, you don\'t have the `Manage Roles` permission!')
            else:
                try:
                    if splitted[1].startswith('<@!'):
                        permId = int(splitted[1][3:][:-1])
                    else:
                        permId = int(splitted[1][2:][:-1])
                except ValueError:
                    await message.channel.send('Error: Invalid tag!')
                aruser = message.guild.get_member(int(permId))
                try:
                    toadd = message.guild.get_role(int(splitted[2][3:][:-1]))
                    await aruser.remove_roles(toadd)
                    await message.channel.send(aruser.name+', you lost the '+toadd.name+' role. :pensive:')
                except Exception as e:
                    await message.channel.send(f'An error occured. :x: ```{e}```')
        if msg.startswith(prefix+'permission') or msg.startswith('perms'):
            if len(splitted)!=2:
                await message.channel.send('Please mention someone!\nExample:\n'+prefix+'permissions <@'+str(authorTag)+'>')
            else:
                member = message.mentions[0]
                perm = ''
                permCheck = [member.guild_permissions.manage_guild, member.guild_permissions.kick_members, member.guild_permissions.ban_members, member.guild_permissions.administrator, member.guild_permissions.change_nickname, member.guild_permissions.manage_nicknames, member.guild_permissions.manage_channels, member.guild_permissions.view_audit_log, member.guild_permissions.manage_messages]
                permString = ['Manage Server', 'Kick Members', 'Ban Members', 'Admin', 'Change their Nickname', 'Manage member\'s nicknames', 'Manage Channels', 'View Audit Log', 'Manage Messages']
                for i in range(0, int(len(permString))):
                    if permCheck[i]==True:
                        perm = perm + ':white_check_mark: '+str(permString[i])+'\n'
                    else:
                        perm = perm + ':x: '+str(permString[i])+'\n'
                try:
                    permissionsEmbed = discord.Embed(title='User permissions for '+str(client.get_user(permId).name)+';', description=str(perm), colour=discord.Colour.blue())
                    await message.channel.send(embed=permissionsEmbed)
                except Exception as e:
                    await message.channel.send('elol. we have an elol here:```'+e+'```')
        if msg.startswith(prefix+'makechannel'):
            if message.guild.get_member(int(authorTag)).guild_permissions.manage_channels==False:
                await message.channel.send('You don\'t have the permission `Manage Channel`. Which is required.')
                acceptId = 1
            else:
                acceptId = 0
            if acceptId==0:
                trashCrap = ['text', 'voice']
                if len(splitted)<3:
                    await message.channel.send('Invalid arguments.')
                elif splitted[1] not in trashCrap:
                    await message.channel.send('Invalid type. Please add `text` or `voice`.')
                elif splitted[1]=='text':
                    try:
                        await message.guild.create_text_channel(msg[int(len(splitted[0])+len(splitted[1])+2):].replace(' ', '-'))
                        await message.channel.send(':white_check_mark: Done! Created a text channel: '+str(msg[int(len(splitted[0])+len(splitted[1])+2):]))
                    except:
                        await message.channel.send(':x: Oops! It seemed that we have a problem creating a text channel. :(')
                elif splitted[1]=='voice':
                    await message.guild.create_voice_channel(msg[int(len(splitted[0])+len(splitted[1])+2):])
                    await message.channel.send(':white_check_mark: Done! Created a voice channel: '+str(msg[int(len(splitted[0])+len(splitted[1])+2):]))
                else:
                    await message.channel.send('error. (not 404)')
        if msg.startswith(prefix+'kick'):
            if len(splitted)<2:
                await message.channel.send('Please mention someone!!1!11')
            else:
                if splitted[1].startswith('<@!'):
                    idiot = message.guild.get_member(int(splitted[1][3:][:-1]))
                else:
                    idiot = message.guild.get_member(int(splitted[1][2:][:-1]))
                misterKicker = message.guild.get_member(int(authorTag))
                if misterKicker.guild_permissions.kick_members==False:
                    await message.channel.send('You cannot kick '+str(idiot.name)+', because you don\'t even have the `Kick Members` permission!')
                    acceptId = 1
                elif idiot.guild_permissions.administrator==True or idiot.guild_permissions.manage_guild==True:
                    await message.channel.send('**You want me to kick an mod/admin?!**\nCome on, you gotta be kidding me.')
                    acceptId = 1
                elif idiot.id==authorTag:
                    await message.channel.send('Don\'t be a weirdo, kicking urself. If you want, just leave the server! That\'s easy! :grinning:')
                    acceptId = 1
                else:
                    acceptId = 0
                if acceptId==0:
                    msgs = [
                        'Sayonara, '+idiot.name,
                        'Mr.Kicker kicked '+idiot.name+'!',
                        'F\'s in the chat for '+idiot.name+', because he got kicked.',
                        'Heh, bye-bye '+idiot.name+'! lul',
                        'Game over, '+idiot.name+'.',
                        'It\'s time to stop, '+idiot.name+'.'
                    ]
                    if len(splitted)==2:
                        reas = 'Unspecified by kicker.'
                    else:
                        reas = msg[int(len(splitted[1])+len(splitted[0])+2):]
                    await message.guild.kick(idiot, reason=str(reas)) #BYE BYE IDIOT!!!
                    await message.channel.send(random.choice(msgs))
                else:
                    await message.channel.send(':x: Kick declined by Username601.')
        if msg.startswith(prefix+'nick'):
            acceptId = 0
            if len(splitted)<2:
                await message.channel.send('Where\'s da paramaters!?!')
                acceptId = 1
            else:
                if splitted[1].startswith('<@') and splitted[1].endswith('>'):
                    try:
                        if splitted[1].startswith('<@!'):
                            changethem = message.guild.get_member(int(splitted[1][3:][:-1]))
                        else:
                            changethem = message.guild.get_member(int(splitted[1][2:][:-1]))
                    except ValueError:
                        await message.channel.send('Error with the tag. :x: :(')
                        acceptId = 1
                    finally:
                        if message.guild.get_member(int(authorTag)).guild_permissions.manage_nicknames==False:
                            await message.channel.send('You need the `Manage Nicknames` permissions to do this command.')
                            acceptId = 1
                else:
                    changethem = message.guild.get_member(int(authorTag))
                    if changethem.guild_permissions.change_nickname==False:
                        acceptId = 1
                        await message.channel.send('You need the `Change Nickname` permission to change your, nickname, DUH')
                if acceptId==0:
                    newnick = message.content[int(len(splitted[1])+len(splitted[0])+2):]
                    try:
                        await changethem.edit(nick=newnick)
                        await message.channel.send('Change the '+changethem.name+'\'s nickname to `'+str(newnick)+'`. Nice name!')
                    except:
                        await message.channel.send('So umm, i wanted to change their nickname and...\nDiscord says: `Missing Permissions`\nMe and '+str(msgAuthor)+': :neutral_face:')
        if msg.startswith(prefix+'imdb'):
            wait = await message.channel.send('Please wait...')
            if len(splitted)==1 or splitted[1]=='help' or splitted[1]=='--help':
                embed = discord.Embed(title='IMDb command help', description='Searches through the IMDb Movie database.\n{} are Parameters that is **REQUIRED** to get the info.\n\n', colour=discord.Colour.red())
                embed.add_field(name='Commands', value=prefix+'imdb --top {NUMBER}\n'+prefix+'imdb --search {TYPE} {QUERY}\n'+prefix+'imdb help\n'+prefix+'imdb --movie {MOVIE_ID or MOVIE_NAME}', inline='False')
                embed.add_field(name='Help', value='*{TYPE} could be "movie", "person", or "company".\n{QUERY} is the movie/person/company name.\n{MOVIE_ID} can be got from the search. Example: `'+prefix+'imdb --search movie Inception`.', inline='False')
                await wait.edit(content='', embed=embed)
            if splitted[1]=='--top':
                if len(splitted)==2:
                    await wait.edit(content='Please type the number!\nex: --top 5, --top 10, etc.')
                else:
                    num = splitted[2]
                    try:
                        if int(num)>30:
                            await wait.edit(content='That\'s too many movies to be listed!')
                        else:
                            arr = ia.get_top250_movies()
                            total = ''
                            for i in range(0, int(num)):
                                total = total + str(int(i)+1) + '. '+str(arr[i]['title'])+' (`'+str(arr[i].movieID)+'`)\n'
                            embed = discord.Embed(title='IMDb Top '+str(num)+':', description=str(total), colour=discord.Colour.red())
                            await wait.edit(content='', embed=embed)
                    except ValueError:
                        await wait.edit(content='Is the top thing you inputted REALLY a number?\nlike, Not top TEN, but top 10.\nGET IT?')
            if splitted[1]=='--movie':
                if splitted[1]=='--movie' and len(splitted)==2:
                    await wait.edit(content='Where\'s the ID?!?!?!')
                else:
                    if splitted[2].isnumeric()==True:
                        movieId = splitted[2]
                        theID = str(movieId)
                    else:
                        movieId = ia.search_movie(msg[int(len(splitted[0])+len(splitted[1])+2):])[0].movieID
                        theID = str(movieId)
                    data = ia.get_movie(str(movieId))
                try:
                    embed = discord.Embed(title=data['title'], colour=discord.Colour.red())
                    await wait.edit(content='Please wait... Retrieving data...')
                    emoteStar = ''
                    for i in range(0, round(int(ia.get_movie_main(theID)['data']['rating']))):
                        emoteStar = emoteStar + ' :star:'
                    upload_date = ia.get_movie_release_info(str(theID))['data']['raw release dates'][0]['date']
                    imdb_url = ia.get_imdbURL(data)
                    await wait.edit(content='Please wait... Creating result...')
                    embed.add_field(name='General Information', value=f'**IMDb URL: **{imdb_url}\n**Upload date: **{upload_date}\n**Written by: **'+ia.get_movie_main(str(theID))['data']['writer'][0]['name']+'\n**Directed by: **'+ia.get_movie_main(str(theID))['data']['director'][0]['name'])
                    embed.add_field(name='Ratings', value=emoteStar+'\n**Overall rating: **'+str(ia.get_movie_main(str(theID))['data']['rating'])+'\n**Rated by '+str(ia.get_movie_main(str(theID))['data']['votes'])+' people**')
                    embed.set_image(url=ia.get_movie_main(str(theID))['data']['cover url'])
                    await wait.edit(content='', embed=embed)
                except KeyError:
                    await wait.edit(content='An error occured!\n**Good news, we *may* fix it.**')
                    errorQuick = discord.Embed(title=data['title'], colour=discord.Colour.red())
                    errorQuick.add_field(name='General Information', value=f'**IMDb URL: **{imdb_url}\n**Upload date: **{upload_date}')
                    errorQuick.add_field(name='Ratings', value=emoteStar+'\n**Overall rating: **'+str(ia.get_movie_main(str(theID))['data']['rating'])+'\n**Rated by '+str(ia.get_movie_main(str(theID))['data']['votes'])+' people**')
                    errorQuick.set_footer(text='Information given is limited due to Errors and... stuff.')
                    await wait.edit(content='', embed=errorQuick)
            if splitted[1]=='--search':
                query = len(splitted[0])+len(splitted[1])+len(splitted[2])+3
                query = msg[query:]
                lists = ''
                if splitted[2].startswith('movie') or splitted[2].startswith('film'):
                    main_name = 'MOVIE'
                    movies = ia.search_movie(query)
                    for i in range(0, int(len(movies))):
                        if len(lists)>1950:
                            break
                        lists = lists + str(int(i)+1) +'. '+ str(movies[i]['title'])+ ' (`'+str(movies[i].movieID)+'`)\n'
                elif splitted[2].startswith('company'):
                    main_name = 'COMPANY'
                    companies = ia.search_company(query)
                    for i in range(0, int(len(companies))):
                        if len(lists)>1950:
                            break
                        lists = lists + str(int(i)+1) + '. '+str(companies[i]['name']) + ' (`'+str(companies[i].companyID)+'`)\n'
                elif splitted[2].startswith('person'):
                    main_name = 'PERSON'
                    persons = ia.search_person(query)
                    for i in range(0, int(len(persons))):
                        if len(lists)>1950:
                            break
                        lists = lists + str(int(i)+1) + '. '+str(persons[i]['name']) + ' (`'+str(persons[i].personID)+'`)\n'
                embed = discord.Embed(title=main_name.lower()+' search for "'+str(query)+'":', description=str(lists), colour=discord.Colour.red())
                if main_name=='MOVIE':
                    embed.set_footer(text='Type '+prefix+'imdb --'+str(main_name.lower())+' {'+main_name+'_ID} to show each info.')
                await wait.edit(content='', embed=embed)
        if msg.startswith(prefix+'dogfact'):
            fact = json.loads((urllib.request.urlopen('https://dog-api.kinduff.com/api/facts')).read())
            if fact['success']!=True:
                desc = 'Error getting the fact.'
            else:
                desc = fact['facts'][0]
            embed = discord.Embed(title='Did you know?',description=str(desc))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'roleinfo'):
            acceptId = 0
            if acceptId==0:
                await message.delete()
                data = message.guild.get_role(int(splitted[1][3:][:-1]))
                if data.permissions.administrator==True:
                    perm = ':white_check_mark: Server Administrator'
                else:
                    perm = ':x: Server Administrator'
                if data.mentionable==True:
                    men = ':warning: You can mention this role and they can get pinged.'
                else:
                    men = ':v: You can mention this role and they will not get pinged! ;)'
                embedrole = discord.Embed(title='Role info for role: '+str(data.name), description='**Role ID: **'+str(data.id)+'\n**Role created at: **'+str(data.created_at)[:-7]+' UTC\n**Role position: **'+str(data.position)+'\n**Members having this role: **'+str(len(data.members))+'\n'+str(men)+'\nPermissions Value: '+str(data.permissions.value)+'\n'+str(perm), colour=data.colour)
                await message.channel.send(embed=embedrole)
        if msg.startswith(prefix+'wallpaper'):  
            width = ['100', '200', '300', '400', '500', '600', '700', '800', '900', '1000']
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url='https://picsum.photos/'+str(random.choice(width)))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'coffee'):
            embed = discord.Embed(colour=discord.Colour.blue())
            link = 'https://coffee.alexflipnote.dev/random'
            embed.set_image(url=link)
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'fox'):
            img = requests.get('https://randomfox.ca/floof/?ref=apilist.fun').text.split('"image":"')[1].split('"')[0].replace('\/', '/')
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_image(url=img)
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'newemote'):
            data = requests.get('https://discordemoji.com/')
            byEmote = data.text.split('<div class="float-right"><a href="')
            del byEmote[0]
            alls = []
            for i in range(0, len(byEmote)):
                if byEmote[i].startswith('http'):
                    alls.append(byEmote[i].split('"')[0])
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url=random.choice(alls))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'steam'):
            getprof = msg[7:].replace(' ', '%20')
            data = requests.get('https://api.alexflipnote.dev/steam/user/'+str(getprof))
            if '<title>404 Not Found</title>' in data.text:
                await message.channel.send('Error **404**! `not found...`')
            else:
                steam_id = data.text.split('"steamid64":')[1].split(',')[0][1:]
                custom_url = data.text.split('"customurl":')[1].split('},')[0][1:]
                avatar = data.text.split('"avatarfull": "')[1].split('"')[0]
                username = data.text.split('"username": "')[1].split('"')[0]
                url = data.text.split('"url": "')[1].split('"')[0]
                state = data.text.split('"state": "')[1].split('"')[0]
                privacy = data.text.split('"privacy": "')[1].split('"')[0]
                if state=='Offline':
                    embedColor = discord.Colour.dark_blue()
                else:
                    embedColor = discord.Colour.red()
                embed = discord.Embed(title=username, description='**Profile Link: **'+str(url)+'\n**Current state: **'+str(state)+'\n**Privacy: **'+str(privacy)+'\n**Profile pic: **'+str(avatar), colour = embedColor)
                embed.set_thumbnail(url=avatar)
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'salty'):
            if len(splitted)!=2:
                await message.channel.send('Error! Invalid args.')
            else:
                for user in message.mentions:
                    av = user.avatar_url
                    break
                embed = discord.Embed(colour=discord.Colour.magenta())
                embed.set_image(url='https://api.alexflipnote.dev/salty?image='+str(av))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'woosh') or msg.startswith(prefix+'wooosh') or msg.startswith(prefix+'woooosh'):
            if len(splitted)!=2:
                await message.channel.send('Error! Invalid args.')
            else:
                for user in message.mentions:
                    av = user.avatar_url
                    break
                embed = discord.Embed(colour=discord.Colour.magenta())
                embed.set_image(url='https://api.alexflipnote.dev/jokeoverhead?image='+str(av))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'funfact'):
            wait = await message.channel.send('Please wait...')
            data = requests.get('https://bestlifeonline.com/random-fun-facts/')
            byFact = data.text.split('<div class="title ">')
            accepted = False
            facts = []
            for a in byFact:
                if a.split('</div')[0].startswith('Superman'):
                    accepted = True
                if accepted==True:
                    facts.append(a.split('</div>')[0])
                else:
                    continue
            await wait.edit(content='Did you know?\n**'+str(random.choice(facts))+'**')
        if msg.startswith(prefix+'supreme'):
            text = msg[9:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.magenta())
            embed.set_image(url='https://api.alexflipnote.dev/supreme?text='+str(text))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'googledoodle'):
            wait = await message.channel.send('Please wait... This may take a few moments...')
            data = requests.get('https://google.com/doodles')
            byLatest = data.text.split('<li class="latest-doodle ">')
            del byLatest[0]
            byTag = ''.join(byLatest).split('<')
            doodle_link = 'https://google.com'+str(byTag[3][8:].split('"\n')[0])
            doodle_img = 'https:'+str(byTag[4][9:].split('" alt="')[0])
            doodle_name = doodle_link[27:].replace('-', ' ')
            embed = discord.Embed(title=doodle_name, description=doodle_link, colour=discord.Colour.blue())
            embed.set_image(url=doodle_img)
            await wait.edit(content='', embed=embed)
        if msg.startswith(prefix+'createbot'):
            if len(splitted)<2:
                tutorials = f'{prefix}createbot --started `Getting started, preparing stuff.`\n{prefix}createbot --say `Say command help.`\n{prefix}createbot --ping `Ping command help. (Client latency).`\n{prefix}createbot --coin `Flip coin game`\n{prefix}createbot --embed `Creating embeds`\n{prefix}createbot --avatar `Avatar commands help.`'
                embed = discord.Embed(title='Createbot; the discord.py bot tutorial', description=f'This is a tutorial on how to create a discord bot.\nEvery thing other than `--started` needs to have the same module or string.\nEach are splitted on different categories.\n\n{tutorials}', colour=discord.Colour.red())
                await message.channel.send(embed=embed)
            elif splitted[1]=='--avatar':
                await message.channel.send('```py\nif msg.startswith(\f\'{prefix}avatar\'):\n\tembed = discord.Embed(colour=discord.Colour.magenta())\n\tembed.set_image(url=message.guild.get_member(int(msg.split()[1][2:][:-1])).avatar_url)\n\tawait message.channel.send(embed=embed)```')
            elif splitted[1]=='--embed':
                await message.channel.send('Embed example: ```py\nif message.channel.send(f\'{prefix}embedthing\'):\n\tembed = discord.Embed(\n\t\ttitle = \'My embed title\',\n\t\tdescription = \'The embed description and stuff. Lorem ipsum asdf\',\n\t\tcolour = discord.Colour.blue()\n\tembed.add_field(name=\'Field name\', value=\'embed field value is here\', inline=\'True\')\n\tembed.set_footer(text=\'this is a footer\')\n\tawait message.channel.send(embed=embed)```')
            elif splitted[1]=='--coin':
                await message.channel.send('Requires: `Random module`\nType the following at the first line of your code;```py\nimport random```Then type the if statement:```py\nif msg.startswith(f\'{prefix}coinflip\'):\n\tawait message.channel.send(random.choice([\'HEADS!\', \'TAILS!\']))```')
            elif splitted[1]=='--ping':
                await message.channel.send('```py\nif msg.startswith(f\'{prefix}ping\'):\n\tawait message.channel.send(\'**Pong!**\\n\'+str(round(client.latency*1000))+\' ms.\')```')
            elif splitted[1]=='--say':
                await message.channel.send('```py\nif msg.startswith(f\'{prefix}say\'):\n\tawait message.channel.send(msg[int(len(msg.split()[0])+1):])```')
            elif splitted[1]=='--started':
                embed = discord.Embed(
                    title='How to create a discord BOT with Discord.py',
                    description='This is how you make a BOT using Discord.py\nAccording to the dev! ;)',
                    colour = discord.Colour.dark_blue()
                )
                code = 'import discord\ntoken = \'YOUR TOKEN\'\nclient = discord.Client()\n@client.event\nasync def on_ready():\n\tprint(\'Bot is ready!\')\n@client.event\nasync def on_message(message):\n\tmsg = message.content.lower()\n\tprefix = \'your prefix\'\n\tif msg.startswith(prefix+\'command thing\'):\n\t\tawait message.channel.send(\'Message your bot responds with\')\nclient.run(token)'
                embed.add_field(name='A. Preparing stuff', value='1. Install python through http://python.org/downloads \n2. Learn Python programming language first\n3. Open your console, and type \'pip install discord.py\'\n4.Have some text editor (notepad++/VScode/Sublime Text)', inline='False')
                embed.add_field(name='B. Bot Setup', value='1. Go to http://discordapp.com/developers \n2. Click on \'New Application.\'\n3. Type your bot name and click \'Create\'.\n4. Click on \'bot\' tab, and Click \'Add bot.\'\n5. Click \'Yes, do it!\'\n6. If your name is not approved, please change the bot name in the \'General Information Tab.\' Else, congrats!', inline='False')
                embed.add_field(name='C. Invite the bot to your server', value='1. On the \'Oauth2\' Tab, scroll down and on the scopes list, check \'Bot\'.\n2. Check the bot permissions first.\n3. Click on COPY.\n4. Open that link on your browser.\n5. Authorize the bot to your server.\n6. Boom! Your bot joined your server!', inline='False')
                embed.add_field(name='D. Coding time!', value='1. Create a folder.\n2. Open that folder and create a file named \'bot.py\' in .py extension.\n3. Open that file with a text editor.\n4. Code the following above.\n', inline='False')
                embed.add_field(name='E. How to get the Token?', value='1. Open the http://discordapp.com/developers, and click on your bot.\n2. Open the \'Bot\' tab.\n3. On token, click \'Copy\'.\n4. Change the \'YOUR TOKEN\' above by pasting your token.\n5. DON\'T SHARE YOUR TOKEN WITH ANYBODY.', inline='False')
                embed.add_field(name='F. Discord API?', value='https://discordpy.readthedocs.io/en/latest/api.html', inline='False')
                embed.set_footer(text='Enjoy your BOT! ;)')
                await message.channel.send(embed=embed, content='```py\n'+str(code)+'```')
        if msg.startswith(prefix+'channels'):
            channels = ''
            warning = 'No errors found.'
            for i in range(0, int(len(message.guild.text_channels))):
                if len(channels)>2048:
                    warning = 'Error: Too many channels, some channels may be not listed.'
                channels = channels +'<#'+ str(message.guild.text_channels[i].id) + '> \n'
            embed = discord.Embed(title=message.guild.name+'\'s Text channels:', description=str(channels), inline='True')
            embed.set_footer(text=str(warning))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'isprime'):
            if int(splitted[1])<999999:
                numsArray = range(2, int(splitted[1]))
                id = 0
                canBeDividedBy = []
                for k in range(0, int(len(numsArray))):
                    if int(splitted[1])%numsArray[k]==0:
                        id = 1
                        canBeDividedBy.append(str(numsArray[k]))
                if id==0:
                    await message.channel.send("YES. "+str(splitted[1])+" is a prime number.")
                else:
                    await message.channel.send("NO. "+str(splitted[1])+" can be divided by "+str(canBeDividedBy)+".")
            else:
                await message.channel.send('OverloadInputError: Beyond the limit of 999999') #https://api.alexflipnote.dev/drake?top=text&bottom=text
        if msg.startswith(prefix+'jpeg') or msg.startswith(prefix+'invert') or msg.startswith(prefix+'magik')or msg.startswith(prefix+'pixelate')or msg.startswith(prefix+'b&w'):
            if splitted[0][1:]=='jpeg':
                com = 'jpegify'
            elif splitted[0][1:]=='invert':
                com = 'invert'
            elif splitted[0][1:]=='magik':
                com = 'magik'
            elif splitted[0][1:]=='pixelate':
                com = 'pixelate'
            elif splitted[0][1:]=='b&w':
                com = 'b&w'
            if len(splitted)!=2:
                await message.channel.send('Please tag someone!')
            else:
                for user in message.mentions:
                    av = user.avatar_url
                    break
                embed = discord.Embed(colour=discord.Colour.magenta())
                embed.set_image(url='https://api.alexflipnote.dev/filter/'+str(com)+'?image='+str(av).replace('webp', 'png'))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'drake'):
            if splitted[1]=='help':
                embed = discord.Embed(
                    title='Drake meme helper help',
                    description='Type the following:\n`'+str(prefix)+'drake [text1] [text2]`\n\nFor example:\n`'+str(prefix)+'drake [doing it yourself] [getting the help]`'
                )
                embed.set_image(url='https://api.alexflipnote.dev/drake?top=doing%20it%20yourself&bottom=getting%20the%20help')
                await message.channel.send(embed=embed)
            else:
                txt1 = msg[5:].split('[')[1][:-2].replace(' ', '%20')
                txt2 = msg[5:].split('[')[2][:-1].replace(' ', '%20')
                embed = discord.Embed(colour=discord.Colour.blue())
                embed.set_image(url='https://api.alexflipnote.dev/drake?top='+str(txt1)+'&bottom='+str(txt2))
                print('https://api.alexflipnote.dev/drake?top='+str(txt1)+'&bottom='+str(txt2))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'ascii'):
            if len(splitted)<2:
                await message.channel.send('Invalid. Please send a word or something.')
            else:
                if '--randomfont' not in msg:
                    query = str(msg[int(len(splitted[0])+1):]).replace(' ', '%20')
                    word = requests.get("http://artii.herokuapp.com/make?text="+query.replace('--randomfont', '')).text
                else:
                    fonts = splashes.getAsciiFonts()
                    query = str(msg[int(len(splitted[0])+1):]).replace(' ', '%20')
                    query = query.replace('--randomfont ', '')
                    word = requests.get("http://artii.herokuapp.com/make?text="+query.replace('--randomfont', '')+'&font='+random.choice(fonts)).text
                if len(word)>1900:
                    await message.channel.send('The word is too long to be displayed!')
                else:
                    embed = discord.Embed(
                        description=f'```{word}```',
                        colour=discord.Colour.red()
                    )
                    embed.set_footer(text='Type --randomfont for umm.. random font to be generated.')
                    await message.channel.send(embed=embed)
        if msg.startswith(prefix+'userinfo'):
            acceptId = 0
            if acceptId==0:
                if len(splitted)==1:
                    userid = int(authorTag)
                    user = client.get_user(int(authorTag))
                elif len(splitted)==2:
                    if splitted[1].startswith('<@!'):
                        userid = int(splitted[1][3:][:-1])
                        user = client.get_user(int(splitted[1][3:][:-1]))
                    else:
                        userid = int(splitted[1][2:][:-1])
                        user = client.get_user(int(splitted[1][2:][:-1]))
                guy = message.guild.get_member(int(userid))
                if guy.status.name=='dnd':
                    status = 'do not disturb'
                else:
                    status = guy.status.name
                percentage = round(int(len(guy.roles))/int(len(message.guild.roles))*100)
                userrole = ''
                for i in range(0, int(len(guy.roles))):
                    if len(userrole)>899:
                        break
                    userrole = userrole + '<@&'+str(guy.roles[i].id)+'> '
                if user.bot==True:
                    thing = 'Bot'
                else:
                    thing = 'User'
                embed = discord.Embed(
                    title=user.name,
                    colour = guy.colour
                )
                joinServer = guy.joined_at
                embed.add_field(name='General info.', value='**'+thing+' name: **'+str(user.name)+'\n**'+thing+' ID: **'+str(user.id)+'\n**Discriminator: **'+str(user.discriminator)+'\n**'+thing+' creation: **'+str(user.created_at)[:-7]+'\n**Status:** '+str(status), inline='True')
                embed.add_field(name='Server specific', value='**'+thing+' nickname: **'+str(guy.display_name)+'\n**'+thing+' roles: **'+str(userrole)+'\nThis user owns '+str(percentage)+'% of all roles in this server.\n**Joined this server at: **'+str(joinServer)[:-7])
                embed.set_thumbnail(url=user.avatar_url)
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'wikipedia'):
            wait = await message.channel.send('Please wait...')
            if len(splitted)<2:
                await wait.edit(content='Please input a page name!')
            else:
                wikipedia = wikipediaapi.Wikipedia('en')
                page = wikipedia.page(msg[11:])
                if page.exists()==False:
                    await wait.edit(content='That page does not exist!\n40404040404040404040404')
                else:
                    if ' may refer to:' in page.text:
                        byCategory = page.text.split('\n\n')
                        del byCategory[0]
                        temp = ''
                        totalCount = 0
                        for b in byCategory:
                            if b.startswith('See also') or len(temp)>950:
                                break
                            totalCount = int(totalCount)+1
                            temp = temp + str(totalCount)+'. ' + str(b) + '\n\n'
                        explain = temp
                        pageTitle = 'The page you may be refering to may be;'
                    else:
                        pageTitle = page.title
                        explain = ''
                        count = 0
                        limit = random.choice(list(range(2, 4)))
                        for i in range(0, len(page.summary)):
                            if count==limit or len(explain)>900:
                                break
                            explain = explain + str(list(page.summary)[i])
                            if list(page.summary)[i]=='.':
                                count = int(count) + 1
                    embed = discord.Embed(title=pageTitle, description=str(explain), colour=discord.Colour.blue())
                    embed.set_footer(text='Get more info at '+str(page.fullurl))
                    await wait.edit(content='', embed=embed)
        if msg.startswith(prefix+'getinvite'):
            if message.guild.get_member(int(authorTag)).guild_permissions.create_invite==False:
                await message.channel.send(':x: You need to have the permission `Create Invite` to continue!')
            else:
                serverinvite = await message.channel.create_invite(reason='Requested by '+str(msgAuthor))
                await message.channel.send('New invite created! Link: **'+str(serverinvite)+'**')
        if msg.startswith(prefix+'avatar'):
            try:
                if len(splitted)==1:
                    user = client.get_user(int(authorTag))
                elif len(splitted)==2:
                    if splitted[1].startswith('<@!'):
                        user = client.get_user(int(splitted[1][3:][:-1]))
                    else:
                        user = client.get_user(int(splitted[1][2:][:-1]))
                embed = discord.Embed(title=user.name+'\'s avatar', colour = discord.Colour.dark_blue())
                embed.set_image(url=user.avatar_url)
                await message.channel.send(embed=embed)
            except:
                await message.channel.send('Invalid avatar. :rage:')
        if msg.startswith(prefix+'ph'):
            if splitted[1]=='help':
                embed = discord.Embed(title='ph command help', description='Type the following:\n'+prefix+'ph [txt1] [txt2]\n\nFor example:\n'+prefix+'ph [Git] [Hub]', colour=discord.Colour.red())
                embed.set_image(url='https://api.alexflipnote.dev/pornhub?text=Git&text2=Hub')
                await message.channel.send(embed=embed)
            elif '[' in msg:
                txt1 = msg.split('[')[1][:-2].replace(' ', '%20')
                txt2 = msg.split('[')[2][:-1].replace(' ', '%20')
                embed = discord.Embed(colour=discord.Colour.red())
                embed.set_image(url='https://api.alexflipnote.dev/pornhub?text='+str(txt1)+'&text2='+str(txt2))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'translate'):
            wait = await message.channel.send('Please wait...')
            if len(splitted)>1:
                if splitted[1]=='--list':
                    lang = ''
                    for bahasa in LANGUAGES:
                        lang = lang+str(bahasa)+' ('+str(LANGUAGES[bahasa])+')\n'
                    embed = discord.Embed(title='List of supported languages', description=str(lang), colour=discord.Colour.blue())
                    await wait.edit(content='', embed=embed)
                elif len(splitted)>2:
                    destination = splitted[1]
                    toTrans = msg[int(len(splitted[1])+len(splitted[0])+2):]
                    try:
                        trans = gtr.translate(toTrans, dest=splitted[1])
                        embed = discord.Embed(title=f'Translation', description=f'**{trans.text}**', colour=discord.Colour.blue())
                        embed.set_footer(text=f'Translated {LANGUAGES[trans.src]} to {LANGUAGES[trans.dest]}')
                        await wait.edit(content='', embed=embed)
                    except:
                        await wait.edit(content='An error occured!')
                else:
                    await wait.edit(content=f'Please add a language! To have the list and their id, type\n`{prefix}translate --list`.')
            else:
                await wait.edit(content=f'Please add translations or\nType `{prefix}translate --list` for supported languages.')
        if msg.startswith(prefix+'catfact'):
            catWait = await message.channel.send('Please wait...')
            response = urllib.request.urlopen("https://catfact.ninja/fact")
            data = json.loads(response.read())
            embed = discord.Embed(
                title = 'Did you know;',
                description = data["fact"],
                color = 0x333333
            )
            await catWait.edit(content='', embed=embed)
        if msg.startswith(prefix+'trash'):
            if len(splitted)!=2:
                await message.channel.send('Please mention someone!\nExample: `'+prefix+'trash <@'+authorTag+'>`')
            else:
                for user in message.guild.members:
                    if user.id==authorTag:
                        av = user.avatar_url
                        break
                for user in message.mentions:
                    toTrash = user.avatar_url
                    break
                embed = discord.Embed(colour=discord.Colour.magenta())
                embed.set_image(url='https://api.alexflipnote.dev/trash?face='+str(av).replace('webp', 'png')+'&trash='+str(toTrash).replace('webp', 'png'))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'bird') or msg.startswith(prefix+'sadcat'):
            if msg.startswith(prefix+'bird'):
                getreq = 'birb'
            else:
                getreq = 'sadcat'
            image_url = requests.get('https://api.alexflipnote.dev/'+str(getreq)).text.split('"file": "')[1].split('"')[0]
            embed = discord.Embed(colour=discord.Colour.magenta())
            embed.set_image(url=image_url)
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'ytthumbnail'):
            if splitted[1].startswith('https://youtu.be/'):
                videoid = splitted[1][17:]
            elif splitted[1].startswith('http://youtu.be/'):
                videoid = splitted[1][16:]
            elif splitted[1].startswith('https://youtube.com/watch?v='):
                videoid = splitted[1][28:]
            elif splitted[1].startswith('https://www.youtube.com/watch?v='):
                videoid = splitted[1][32:]
            else:
                videoid = 'dQw4w9WgXcQ'
            await message.delete()
            embed = discord.Embed(title='Thumbnail for '+str(splitted[1]), color=0xff0000)
            embed.set_image(url='https://img.youtube.com/vi/'+str(videoid)+'/mqdefault.jpg')
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'captcha'):
            capt = msg[9:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url='https://api.alexflipnote.dev/captcha?text='+str(capt))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'tts'):
            if len(splitted)==1:
                await message.channel.send('Invalid :flushed:.')
            else:
                await message.channel.send(content=msg[int(splitted[0]+1):], tts=True)
        if msg.startswith(prefix+'scroll'):
            scrolltxt = msg[8:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_image(url='https://api.alexflipnote.dev/scroll?text='+str(scrolltxt))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'ship') and len(splitted)==1:
            member = []
            av = []
            for i in range(0, int(len(message.guild.members))):
                if message.guild.members[i].name!=msgAuthor:
                    member.append(message.guild.members[i].name)
                    av.append(message.guild.members[i].avatar_url)
            num = random.randint(0, len(av))
            ship = member[num]
            avd = av[num]
            embed = discord.Embed(title=msgAuthor+', i ship you with **'+str(ship)+'**!', colour=discord.Colour.magenta())
            embed.set_image(url='https://api.alexflipnote.dev/ship?user='+str(message.guild.get_member(int(authorTag)).avatar_url).replace('webp', 'png')+'&user2='+str(avd).replace('webp', 'png'))
            embed.set_footer(text=f'Type {prefix}ship [tag1] [tag2] for cooler ones instead of just random!')
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'ghiblifilms'):
            wait = await message.channel.send('Please wait... Getting data...')
            response = urllib.request.urlopen('https://ghibliapi.herokuapp.com/films')
            data = json.loads(response.read())
            if len(splitted)==1:
                films = ""
                for i in range(0, int(len(data))):
                    films = films+'('+str(int(i)+1)+') '+str(data[i]['title']+' ('+str(data[i]['release_date'])+')\n')
                embed = discord.Embed(
                    title = 'List of Ghibli Films',
                    description = str(films),
                    color = 0x00ff00
                )
                embed.set_footer(text='Type `'+str(prefix)+'ghiblifilms <number>` to get each movie info.')
                await wait.edit(content='', embed=embed)
            else:
                num = int(splitted[1])-1
                embed = discord.Embed(
                    title = data[num]['title'] + ' ('+str(data[num]['release_date'])+')',
                    description = '**Rotten Tomatoes Rating: '+str(data[num]['rt_score'])+'%**\n'+data[num]['description'],
                    color = 0x00ff00
                )
                embed.add_field(name='Directed by', value=data[num]['director'], inline='True')
                embed.add_field(name='Produced by', value=data[num]['producer'], inline='True')
                await wait.edit(content='', embed=embed)
        if msg.startswith(prefix+'servericon'):
            if message.guild.is_icon_animated()==True:
                link = 'https://cdn.discordapp.com/icons/'+str(message.guild.id)+'/'+str(message.guild.icon)+'.gif?size=1024'
            else:
                link = 'https://cdn.discordapp.com/icons/'+str(message.guild.id)+'/'+str(message.guild.icon)+'.png?size=1024'
            theEm = discord.Embed(title=message.guild.name+'\'s Icon', colour=discord.Colour.blue())
            theEm.set_image(url=link)
            await message.channel.send(embed=theEm)
        if msg.startswith(prefix+'slowmode'):
            if len(splitted)!=2:
                await message.channel.send('Invalid setup.')
            else:
                if message.guild.get_member(int(authorTag)).guild_permissions.manage_channels==False:
                    await message.channel.send(':x: <@'+str(authorTag)+'> you need the `Manage channels` permission.')
                else:
                    try:
                        global delay
                        delay = int(splitted[1])
                    except ValueError:
                        await message.channel.send('Invalid number!')
                    if delay>21600:
                        await message.channel.send('That\'s too long! You must be an insane admin to do this :flushed:')
                    elif delay<0:
                        await message.channel.send(f'Nope, you expect me to minus slowmode?\n\n**To disable slowmode, type {prefix}slowmode 0 instead.**')
                    else:
                        await message.channel.edit(slowmode_delay=delay)
                        if delay==0:
                            await message.channel.send('Successfully disabled slowmode.')
                        else:
                            await message.channel.send('Successfully changed the slowmode delay of this channel to '+str(delay)+' seconds.')
        if msg.startswith(prefix+'inviteme') or msg.startswith(prefix+'invite'):
            embed = discord.Embed(
                title='Sure thing! Invite this bot to your server using the link below.',
                description='[Invite link](https://top.gg/bot/696973408000409626) | [Support Server](http://discord.gg/HhAPkD8)',
                colour=discord.Colour.green()
            )
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'serverinfo'):
            acceptId = 0
            o_web = 0
            o_desk = 0
            o_pho = 0
            botcount = 0
            online = 0
            idle = 0
            dnd = 0
            offline = 0
            if acceptId==0:
                for i in range(0, int(len(message.guild.members))):
                    if message.guild.get_member(int(message.guild.members[i].id)).desktop_status.name!='offline':
                        o_desk = int(o_desk)+1
                    elif message.guild.get_member(int(message.guild.members[i].id)).mobile_status.name!='offline':
                        o_pho = int(o_pho)+1
                    elif message.guild.get_member(int(message.guild.members[i].id)).web_status.name!='offline':
                        o_web = int(o_web)+1
                    if message.guild.members[i].bot==True:
                        botcount = int(botcount)+1
                    memstat = message.guild.get_member(int(message.guild.members[i].id)).status.name
                    if memstat=='online':
                        online = online + 1
                    elif memstat=='idle':
                        idle = idle + 1
                    elif memstat=='dnd':
                        dnd = dnd + 1
                    else:
                        offline = int(offline) + 1
                total_on = online + idle + dnd
                onperc = round(total_on/len(message.guild.members)*100)
                humans = int(len(message.guild.members))-int(botcount)
                embed = discord.Embed(
                    title=str(message.guild.name),
                    description='Shows the information about '+str(message.guild.name),
                    color=0x000000
                )
                embed.add_field(name='General Info', value='**Region:** '+str(message.guild.region)+'\n**Server ID: **'+str(message.guild.id)+'\n**Server Icon ID: **'+str(message.guild.icon)+'\n**Verification Level: **'+str(message.guild.verification_level)+'\n**Notification level:  **'+str(message.guild.default_notifications)[18:].replace("_", " ")+'\n**Explicit Content Filter:**'+str(message.guild.explicit_content_filter)+'\n**AFK timeout: **'+str(message.guild.afk_timeout)+' seconds\n**Description: **"'+str(message.guild.description)+'"', inline='True')
                embed.add_field(name='Channel Info', value='**Text Channels: **'+str(len(message.guild.text_channels))+'\n**Voice channels: **'+str(len(message.guild.voice_channels))+'\n**Channel categories: **'+str(len(message.guild.categories))+'\n**AFK Channel: **'+str(message.guild.afk_channel), inline='True')
                embed.add_field(name='Members Info', value='**Server owner: **'+str(message.guild.owner)[:-5]+'\n**Members count: **'+str(len(message.guild.members))+'\n**Server Boosters: **'+str(len(message.guild.premium_subscribers))+'\n**Role Count: **'+str(len(message.guild.roles))+'\n**Bot accounts: **'+str(botcount)+'\n**Human accounts: **'+str(humans), inline='True')
                embed.add_field(name='Member Status', value=':green_circle: '+str(online)+' :orange_circle: '+str(idle)+' :red_circle: '+str(dnd)+' :black_circle: '+str(offline)+'\n:grinning: '+str(total_on)+' ('+str(onperc)+'%) | :sleeping: '+str(offline)+' ('+str(100-int(onperc))+'%)\n:iphone: '+str(o_pho)+' | :computer: '+str(o_desk)+' | :globe_with_meridians: '+str(o_web))
                serverurl = 'https://discordapp.com/channels/'+str(message.guild.id)
                if message.guild.is_icon_animated()==False:
                    servericonurl = str('https://cdn.discordapp.com/icons/'+str(message.guild.id)+'/'+str(message.guild.icon)+'.png?size=1024')
                else:
                    servericonurl = str('https://cdn.discordapp.com/icons/'+str(message.guild.id)+'/'+str(message.guild.icon)+'.gif?size=1024')
                embed.add_field(name='URL stuff', value=f'[Server URL]({serverurl}) | [Server Icon URL]({servericonurl})')
                embed.set_thumbnail(url=str('https://cdn.discordapp.com/icons/'+str(message.guild.id)+'/'+str(message.guild.icon)+'.png?size=1024'))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'factor'):
            if int(splitted[1])<999999:
                numList = range(1, int(splitted[1]))
                factor = []
                for i in range(0, int(len(numList))):
                    if int(splitted[1])%int(numList[i])==0:
                        factor.append(numList[i])
                factor.append(int(splitted[1]))
                await message.channel.send(str(factor))
            else:
                await message.channel.send('OverloadInputError: Beyond the limit of 999999.')
        if msg.startswith(prefix+'multiplication'):
            arr = []
            for i in range(1, 15):
                arr.append(int(splitted[1])*i)
            await message.channel.send(str(arr))
        if msg.startswith(prefix+'gdcomment'):
            try:
                # >gdcomment yoo i suck | vierofernando | 999
                byI = message.content[int(len(splitted[0])+1):].split(' | ')
                text = byI[0].replace('/', '').replace(' ', '%20')
                num = int(byI[2])
                if num>9999:
                    num = 601
                elif num<-9999:
                    num = -601
                gdprof = byI[1].replace(' ', '%20').replace('/', '')
                embed = discord.Embed(colour=discord.Colour.green())
                if message.guild.get_member(int(authorTag)).guild_permissions.manage_guild==True:
                    embed.set_image(url='https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(gdprof)+'&likes='+str(num)+'&mod=mod&days=1-second')
                else:
                    embed.set_image(url='https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(gdprof)+'&likes='+str(num)+'&days=1-second')
                await message.channel.send(embed=embed)
            except Exception as e:
                print('https://gdcolon.com/tools/gdcomment/img/'+str(text)+'?name='+str(gdprof)+'&likes='+str(num)+'&days=1-second')
                await message.channel.send(f'Invalid!\nThe flow is this: `{prefix}gdcomment text | name | like count`\nExample: `{prefix}gdcomment I am cool | RobTop | 601`.\n\nFor developers: ```{e}```')
        if msg.startswith(prefix+'gdbox'):
            if len(splitted)==1:
                await message.channel.send('Please input a text!')
            else:
                wait = await message.channel.send('Please wait...')
                text = message.content[int(len(splitted[0])+1):].replace(' ', '%20').replace('/', '')
                av = message.guild.get_member(int(authorTag)).avatar_url
                if len(text)>100:
                    await message.channel.send('the text is too long!')
                else:
                    if message.guild.get_member(int(authorTag)).guild_permissions.manage_guild==False:
                        color = 'brown'
                    else:
                        color = 'blue'
                    embed = discord.Embed(colour=discord.Colour.green())
                    embed.set_image(url='https://gdcolon.com/tools/gdtextbox/img/'+str(text)+'?color='+color+'&name='+str(msgAuthor)+'&url='+str(av).replace('webp', 'png')+'&resize=1')
                    await wait.edit(content='', embed=embed)
        if msg.startswith(prefix+'serveremojis'):
            acceptId = 0
            if acceptId==0:
                if len(splitted)==2 and splitted[1]=='--short':
                    all = ''
                    for i in range(0, len(message.guild.emojis)):
                        if len(all)>1960:
                            break
                        if message.guild.emojis[i].animated==True:
                            all = all + ' <a:'+str(message.guild.emojis[i].name)+':'+str(message.guild.emojis[i].id)+'> '
                        else:
                            all = all + ' <:'+str(message.guild.emojis[i].name)+':'+str(message.guild.emojis[i].id)+'> '
                    await message.channel.send(str(all))
                else:
                    staticemo = ""
                    animateemo = ""
                    staticcount = 0
                    animatecount = 0
                    warning = 'No errors found.'
                    for i in range(0, int(len(message.guild.emojis))):
                        if message.guild.emojis[i].animated==True:
                            animatecount = int(animatecount) + 1
                        else:
                            staticcount = int(staticcount) + 1
                        if len(staticemo)>950 or len(animateemo)>950:
                            warning = 'Error: Too many emojis, some emojis may remain unlisted above.\nInstead type '+str(prefix+'serveremojis --short')
                            break
                        if message.guild.emojis[i].animated==True:
                            animateemo = animateemo + '<a:'+str(message.guild.emojis[i].name)+':'+str(message.guild.emojis[i].id)+'> ('+str(message.guild.emojis[i].name)+') \n'
                        else:
                            staticemo = staticemo + '<:'+str(message.guild.emojis[i].name)+':'+str(message.guild.emojis[i].id)+'> ('+str(message.guild.emojis[i].name)+') \n'
                    embed = discord.Embed(
                        title = message.guild.name+'\'s emojis',
                        colour = discord.Colour.red()
                    )
                    if staticemo=="":
                        staticemo = 'No emojis found :('
                    if animateemo=="":
                        animateemo = 'No emojis found :('
                    embed.add_field(name='Static Emojis ('+str(staticcount)+')', value=str(staticemo), inline='False')
                    embed.add_field(name='Animated Emojis ('+str(animatecount)+')', value=str(animateemo), inline='False')
                    embed.set_footer(text=str(warning))
                    await message.channel.send(embed=embed)
        if msg.startswith(prefix+'id'):
            var = splitted[1][:-1]
            if (splitted[1].startswith('<#')):
                var = var[2:]
            elif (splitted[1].startswith('<@!')):
                var = var[3:]
            await message.channel.send(str(var))
        if msg.startswith(prefix+'robohash'):
            if len(splitted)<2:
                gib = ''
                for i in range(0, random.randint(5, 10)):
                    gib = gib + random.choice(list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))
            else:
                gib = msg[int(len(splitted[0])+1):]
            embed = discord.Embed(title='Here is some robohash for you.', colour=discord.Colour.magenta())
            embed.set_image(url='https://robohash.org/'+str(gib))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'gdlogo'):
            if len(splitted)==1:
                await message.channel.send('Please input a text!')
            else:
                text = msg[int(len(splitted[0])+1):].replace(' ', '%20')
                embed = discord.Embed(colour=discord.Colour.green())
                embed.set_image(url='https://gdcolon.com/tools/gdlogo/img/'+str(text))
                await message.channel.send(embed=embed)
        # gdbox is supposed to be here :c
        if msg.startswith(prefix+'lockdown'):
            if len(splitted)!=2:
                await message.channel.send(f'Invalid parameters. Correct Example: `{prefix}lockdown [seconds]`\nMinimum: 10, Maximum: 900')
            else:
                if splitted[1].isnumeric()==False:
                    await message.channel.send('Invalid time.')
                elif int(splitted[1])<10 or int(splitted[1])>900:
                    await message.channel.send('Invalid: off-limits.')
                elif message.guild.get_member(int(authorTag)).guild_permissions.administrator==False:
                    await message.channel.send(':x: You need the administrator permission to do this!')
                else:
                    try:
                        await message.channel.send('Everyone, <#'+str(message.channel.id)+'> is on lockdown for '+str(splitted[1])+' seconds! No one except administrators can chat! :x:')
                        await message.channel.set_permissions(message.guild.default_role, send_messages=False)
                        await asyncio.sleep(int(splitted[1]))
                        await message.channel.set_permissions(message.guild.default_role, send_messages=True)
                        await message.channel.send('Lockdown ended.')
                    except:
                        await message.channel.send('For some reason, i cannot lock this channel :(')
        if splitted[0]==prefix+"math":
            if int(len(splitted))>4:
                await message.channel.send("OverloadEquationError: So far this bot only accept one equation.")
            else:
                try:
                    num1 = int(splitted[1])
                    num2 = int(splitted[3])
                    inputtedSym = str(splitted[2])
                except IndexError:
                    print('meh.')
                finally:
                    if inputtedSym=="+":
                        sym = "+"
                    elif inputtedSym=="-":
                        sym = "-"
                    elif inputtedSym=="*" or inputtedSym=="x" or inputtedSym=="×":
                        sym = "*"
                    elif inputtedSym=="/" or inputtedSym==":" or inputtedSym=="÷":
                        sym = "/"
                    elif inputtedSym=="^" or inputtedSym=="**":
                        sym = "**"
                    else:
                        await message.channel.send("InvalidSymbolError: Invalid symbol for equation.\nSupported symbol: `+ - * x × / : ÷ ^ **`")
                    if sym=="+":
                        result = int(num1)+int(num2)
                        symId = 0
                    elif sym=="-":
                        result = int(num1)-int(num2)
                        symId = 0
                    elif sym=="*":
                        symId = 0
                        result = int(num1)*int(num2)
                    elif sym=="/":
                        symId = 1
                        result = int(num1)/int(num2)
                        rounded = round(int(result))
                    elif sym=="**":
                        symId = 0
                        result = int(num1)**int(num2)
                    if symId==0:
                        await message.channel.send(str(num1)+" "+str(sym)+" "+str(num2)+" = "+str(result))
                    elif symId==1:
                        await message.channel.send(str(num1)+" "+str(sym)+" "+str(num2)+" = "+str(result)+"\nRound number: "+str(rounded))
        if msg.startswith(prefix+"rng") or msg.startswith(prefix+"randomnumber") or msg.startswith(prefix+"randint"):
            beginning = int(splitted[1])
            ending = int(splitted[2])
            ran = random.randint(int(beginning), int(ending))
            await message.channel.send(str(ran))
        if msg.startswith(prefix+"flipdice") or msg.startswith(prefix+"dice"):
            arr = ["one", "two", "three", "four", "five", "six"]
            ran = random.randint(0, 5)
            await message.channel.send(":"+arr[ran]+":")
        if msg.startswith(prefix+"flipcoin") or msg.startswith(prefix+"coin"):
            ran = random.randint(0, 1)
            if (ran==0):
                await message.channel.send("HEADS")
            elif (ran==1):
                await message.channel.send("TAILS")
        if msg.startswith(prefix+'ship') and len(splitted)>1:
            if len(splitted)<3:
                await message.channel.send(':x: Please tag 2 people!')
            elif len(splitted)==3:
                if splitted[1].startswith('<@!'):
                    av1 = message.guild.get_member(message.mentions[0].id).avatar_url
                else:
                    av1 = message.guild.get_member(message.mentions[0].id).avatar_url
                if splitted[2].startswith('<@!'):
                    av2 = message.guild.get_member(message.mentions[1].id).avatar_url
                else:
                    av2 = message.guild.get_member(message.mentions[1].id).avatar_url
                embed = discord.Embed(colour=discord.Colour.magenta())
                embed.set_image(url='https://api.alexflipnote.dev/ship?user='+str(av1).replace('webp', 'png')+'&user2='+str(av2).replace('webp', 'png'))
                await message.channel.send(embed=embed)
        if msg==prefix+"dog":
            link = "https://random.dog/woof.json"
            response = urllib.request.urlopen(link)
            data = json.loads(response.read())
            img = data['url']
            embed = discord.Embed(colour=discord.Colour.magenta())
            embed.set_image(url=img)
            await message.channel.send(embed=embed)
        if msg==prefix+"cat" or msg.startswith(prefix+"cats"):
            response = urllib.request.urlopen("https://aws.random.cat/meow")
            data = json.loads(response.read())
            embed = discord.Embed(colour=discord.Colour.magenta())
            embed.set_image(url=data['file'])
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'roles'):
            acceptId = 0
            if acceptId==0:
                serverroles = ""
                warning = "No warnings available."
                for i in range(1, int(len(message.guild.roles))):
                    num = int(len(message.guild.roles))-int(i)
                    if len(serverroles)>1990:
                        warning = 'Roles pass the limit of discord Description. This means that some roles are not listed above.'
                        break
                    serverroles = serverroles + str(message.guild.roles[num].name)+'\n'
                embed = discord.Embed(
                    title = 'Server roles of '+message.guild.name+' (From top to bottom.)',
                    description = str(serverroles),
                    color = discord.Colour.dark_blue()
                )
                embed.set_footer(text=str(warning))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+"gddaily"):
            toEdit = await message.channel.send("Retrieving Data...")
            response = urllib.request.urlopen("https://gdbrowser.com/api/level/daily")
            data = json.loads(response.read())
            responseLeaderboard = urllib.request.urlopen("https://gdbrowser.com/api/leaderboardLevel/"+str(data["id"]))
            leader = json.loads(responseLeaderboard.read())
            image = 'https://gdbrowser.com/icon/'+data["author"]
            embed = discord.Embed(
                title = data["name"]+' ('+data["id"]+')',
                description = data["description"],
                colour = discord.Colour.blue()
            )
            embed.set_author(name=data["author"], icon_url=image)
            embed.add_field(name='Uploaded at', value=data["uploaded"], inline='True')
            embed.add_field(name='Updated at', value=data["updated"]+" (Version "+data["version"]+")", inline='True')
            embed.add_field(name='Difficulty', value=data["difficulty"])
            gesture = ':+1:'
            if data['disliked']==True:
                gesture = ':-1:'
            embed.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
            embed.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
            embed.add_field(name='Leaderboard', value="**Rank #1: "+str(leader[1]["username"])+"** "+str(leader[1]["percent"])+"% | "+str(leader[1]["date"])+"\n**Rank #2: "+str(leader[2]["username"])+"** "+str(leader[2]["percent"])+"% | "+str(leader[2]["date"])+"\n**Rank #3: "+str(leader[3]["username"])+"** "+str(leader[3]["percent"])+"% | "+str(leader[3]["date"]))
            await toEdit.edit(content='', embed=embed)
        if msg.startswith(prefix+'botmembers'):
            botmembers = ""
            warning = 'No errors found. Congrats! ^_^'
            for i in range(0, int(len(message.guild.members))):
                if len(botmembers)>2048:
                    warning = 'Error: Too many bots, some bot are not listed above.'
                if message.guild.members[i].bot==True:
                    botmembers = botmembers + message.guild.members[i].name + '\n'
            embed = discord.Embed(
                title = 'Bot members of '+message.guild.name+':',
                description = str(botmembers),
                colour = discord.Colour.dark_blue()
            )
            embed.set_footer(text=warning)
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+"gdweekly"):
            toEdit = await message.channel.send("Retrieving Data...")
            response = urllib.request.urlopen("https://gdbrowser.com/api/level/weekly")
            data = json.loads(response.read())
            responseLeaderboard = urllib.request.urlopen("https://gdbrowser.com/api/leaderboardLevel/"+str(data["id"]))
            leader = json.loads(responseLeaderboard.read())
            image = 'https://gdbrowser.com/icon/'+data["author"]
            embed = discord.Embed(
                title = data["name"]+' ('+data["id"]+')',
                description = data["description"],
                colour = discord.Colour.red()
            )
            embed.set_author(name=data["author"], icon_url=image)
            embed.add_field(name='Uploaded at', value=data["uploaded"], inline='True')
            embed.add_field(name='Updated at', value=data["updated"]+" (Version "+data["version"]+")", inline='True')
            embed.add_field(name='Difficulty', value=data["difficulty"])
            gesture = ':+1:'
            if data['disliked']==True:
                gesture = ':-1:'
            embed.add_field(name='Level Stats', value=str(data["likes"])+' '+gesture+'\n'+str(data["downloads"])+" :arrow_down:", inline='False')
            embed.add_field(name='Level Rewards', value=str(data["stars"])+" :star:\n"+str(data["orbs"])+" orbs\n"+str(data["diamonds"])+" :gem:")
            embed.add_field(name='Leaderboard', value="**Rank #1: "+str(leader[1]["username"])+"** "+str(leader[1]["percent"])+"% | "+str(leader[1]["date"])+"\n**Rank #2: "+str(leader[2]["username"])+"** "+str(leader[2]["percent"])+"% | "+str(leader[2]["date"])+"\n**Rank #3: "+str(leader[3]["username"])+"** "+str(leader[3]["percent"])+"% | "+str(leader[3]["date"]))
            await toEdit.edit(content='', embed=embed)
        if msg.startswith(prefix+'facts'):
            embed = discord.Embed(colour=discord.Colour.magenta())
            embed.set_image(url='https://api.alexflipnote.dev/facts?text='+str(msg[7:].replace(' ', '%20')))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+"gdprofile"):
            url = msg[11:].replace(" ", "%20")
            response = urllib.request.urlopen("https://gdbrowser.com/api/profile/"+url)
            data = json.loads(response.read())
            embed = discord.Embed(
                title = data["username"],
                description = 'Displays user data for '+data["username"]+'.',
                colour = discord.Colour.orange()
            )
            if data["rank"]=="0":
                rank = "Not yet defined :("
            else:
                rank = str(data["rank"])
            if data["cp"]=="0":
                cp = "This user don't have Creator Points :("
            else:
                cp = data["cp"]
            embed.add_field(name='ID Stuff', value='Player ID: '+str(data["playerID"])+'\nAccount ID: '+str(data["accountID"]), inline='True')
            embed.add_field(name='Rank', value=rank, inline='True')
            embed.add_field(name='Stats', value=str(data["stars"])+" Stars"+"\n"+str(data["diamonds"])+" Diamonds\n"+str(data["coins"])+" Secret Coins\n"+str(data["userCoins"])+" User Coins\n"+str(data["demons"])+" Demons beaten", inline='False')
            embed.add_field(name='Creator Points', value=cp)
            embed.set_author(name='Display User Information', icon_url="https://gdbrowser.com/icon/"+url)
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+"rock") or msg.startswith(prefix+"paper") or msg.startswith(prefix+"scissor") or msg.startswith(prefix+"scissors"):
            if msg.startswith(prefix+"rock"):
                given = "fist"
            elif msg.startswith(prefix+"paper"):
                given = "hand_splayed"
            elif msg.startswith(prefix+"scissor") or msg.startswith(prefix+"scissors"):
                given = "v"
            messages = ["Congratulations! "+str(msgAuthor)+" WIN!", "It's a draw.", "Oops, "+str(msgAuthor)+" lost!"]
            emojiArray = ["fist", "hand_splayed", "v"]
            ran = random.randint(0, 2)
            if ran==0:
                if given=="fist":
                    msgId = 1
                elif given=="hand_splayed":
                    msgId = 0
                elif given=="v":
                    msgId = 2
            elif ran==1:
                if given=="fist":
                    msgId = 2
                elif given=="hand_splayed":
                    msgId = 1
                elif given=="v":
                    msgId = 0
            elif ran==2:
                if given=="fist":
                    msgId = 0
                elif given=="hand_splayed":
                    msgId = 2
                elif given=="v":
                    msgId = 1
            colors = [discord.Colour.green(), discord.Colour.orange(), discord.Colour.red()]
            embed = discord.Embed(
                title = messages[msgId],
                colour = colors[msgId]
            )
            embed.set_footer(text='Playin\' rock paper scissors w/ '+str(msgAuthor))
            embed.set_author(name="Playing Rock Paper Scissors with "+str(msgAuthor))
            embed.add_field(name=str(msgAuthor), value=':'+given+':', inline="True")
            embed.add_field(name='Username601', value=':'+str(emojiArray[ran])+':', inline="True")
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+"randomcase"):
            statement = []
            for i in range(1, int(len(splitted))):
                statement.append(splitted[i])
                thing = null.join(statement)
            result = []
            letterArr = list(thing)
            for i in range(0, len(thing)):
                ran = random.randint(0, 1)
                if ran==0:
                    result.append(letterArr[i].upper())
                elif ran==1:
                    result.append(letterArr[i].lower())
            await message.channel.send("".join(result))
        if msg.startswith(prefix+'guessnum') or msg.startswith(prefix+'gn'):
            num = random.randint(5, 100)
            username = message.guild.get_member(int(authorTag)).display_name
            user_class = message.author
            embed = discord.Embed(title='Starting the game!', description='You have to guess a *secret* number between 5 and 100!\n\nYou have 20 attempts, and 20 second timer in each attempt!\n\n**G O O D  L U C K**', colour=discord.Colour.green())
            await message.channel.send(embed=embed)
            gameplay = True
            attempts = 20
            while gameplay==True:
                if attempts<1:
                    await message.channel.send('Time is up! The answer is **'+str(num)+'.**')
                    gameplay = False
                    break
                def check_not_stranger(m):
                    return m.author == user_class
                try:
                    trying = await client.wait_for('message', check=check_not_stranger, timeout=20.0)
                except asyncio.TimeoutError:
                    await message.channel.send('You did not respond for the next 20 seconds!\nGame ended.')
                    gameplay = False
                    break
                if trying.content.isnumeric()==False:
                    await message.channel.send('That is not a number!')
                    attempts = int(attempts) - 1
                else:
                    if int(trying.content)<num:
                        await message.channel.send('Higher!')
                        attempts = int(attempts) - 1
                    if int(trying.content)>num:
                        await message.channel.send('Lower!')
                        attempts = int(attempts) - 1
                    if int(trying.content)==num:
                        await message.channel.send('You are correct!\n**The answer is '+str(num)+'!**')
                        gameplay = False
                        break
        if msg.startswith(prefix+"randomcolor") or msg.startswith(prefix+'colorinfo') or msg.startswith(prefix+'colourinfo'):
            continuing = False
            if msg.startswith(prefix+'randomcolor'):
                listHex = list('0123456789ABCDEF')
                hexCode = ''
                for i in range(0, 6):
                    ran = random.choice(listHex)
                    hexCode = hexCode + ran
                continuing = True
            else:
                if len(splitted)!=2:
                    await message.channel.send('Invalid arguments.')
                elif splitted[1].startswith('#'):
                    await message.channel.send('For hex, please input one WITHOUT `#`!')
                elif len(splitted[1])!=6:
                    await message.channel.send('We only accept `HEX CODES` as inputs!')
                else:
                    hexCode = splitted[1]
                    continuing = True
            if continuing==True:
                #CONVERT TO DECIMAL
                rgb = myself.convertrgb(hexCode, '0')
                percentageRgb = myself.convertrgb(hexCode, '1')
                colorInt = int(hexCode, 16)
                embed = discord.Embed(title='#'+str(hexCode), description="**Integer: **`"+str(colorInt)+"`\n**Red:** "+str(rgb[0])+" ("+str(percentageRgb[0])+"%)\n**Green:** "+str(rgb[1])+" ("+str(percentageRgb[1])+"%)\n**Blue:** "+str(rgb[2])+" ("+str(percentageRgb[2])+"%)\n\nPreview is shown on thumbnail. Other similar gradients are shown below.", colour=discord.Colour.from_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2])))
                embed.set_thumbnail(url='https://api.alexflipnote.dev/colour/image/'+str(hexCode))
                embed.set_image(url='https://api.alexflipnote.dev/colour/image/gradient/'+str(hexCode))
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'call'):
            call = msg[6:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url='https://api.alexflipnote.dev/calling?text='+str(call))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'achieve'):
            txt = msg[9:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url='https://api.alexflipnote.dev/achievement?text='+str(txt))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+"country"):
            country = msg[9:].replace(" ", "%20")
            link = "https://restcountries.eu/rest/v2/name/"+str(country.lower())
            print(link)
            response = urllib.request.urlopen(link)
            c = json.loads(response.read())
            embed = discord.Embed(
                title = c[0]['nativeName'],
                description = '**Capital:** '+str(c[0]['capital'])+'\n**Region: **'+str(c[0]['region'])+'\n**Sub Region: **'+str(c[0]['subregion'])+"\n**Population: **"+str(c[0]['population'])+"\n**Area: **"+str(c[0]['area'])+' km²\n**Time Zones:** '+str(c[0]['timezones'])+'\n**Borders: **'+str(c[0]['borders']),
                colour = 0xffffff
            )
            embed.set_author(name=c[0]['name'])
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'commands') or msg.startswith(prefix+'help'):
            #commands sucks.
            if len(splitted)==1:
                commandos = ''
                for i in range(0, len(cmdtypes)):
                    commandos = commandos + f'{str(i+1)}. `{prefix}help {cmdtypes[i]}`\n'
                commandos = commandos + f'\n\nFor a much detailed description about **the bot itself**, type `{prefix}about`\nTo see the bot\'s latency, type `{prefix}ping`.'
                embed = discord.Embed(
                    title='Username601\'s commands ('+str(totalLength)+')',
                    description='[Join the support server](https://discord.gg/HhAPkD8) | [Vote us on top.gg](https://top.gg/bot/696973408000409626/vote)\n\nOur bot has a variety of commands. Please type the following for each category;\n'+commandos,
                    colour=discord.Colour.dark_blue()
                )
                await message.channel.send(embed=embed)
            else:
                listnums = list(range(0, len(ordertypes)-1))
                for i in range(0, len(cmdtypes)):
                    if cmdtypes[i].lower()==msg[int(len(splitted[0])+1):].lower():
                        embedo = discord.Embed(title='Bot commands for category: '+ordertypes[i].split(' (')[0][2:], description=ordertypes[i], colour=discord.Colour.blue())
                        await message.channel.send(embed=embedo)
                        break
        if msg.startswith(prefix+'about'):
            messageRandom = splashes.getAbout()
            embed = discord.Embed(
                title = 'About this seemingly normal bot.',
                description = random.choice(messageRandom),
                colour = 0xff0000
            )
            embed.add_field(name='Bot general Info', value='**Bot name: ** Username601\n**Programmed in: **Discord.py (Python)\n**Created in: **6 April 2020.\n**Successor of: **somebot56.\n**Default prefix: **'+prefix, inline='True')
            embed.add_field(name='Programmer info', value='**Programmed by: **Viero Fernando.\n**Best languages: **~~HTML, CSS,~~ VB .NET, JavaScript, Python\n**Social links:**\n[Discord Server](http://discord.gg/HhAPkD8)\n[GitHub](http://github.com/vierofernando)\n[Top.gg](https://top.gg/user/661200758510977084)\n[SoloLearn](https://www.sololearn.com/Profile/17267145)\n[Brainly (Indonesia)](http://bit.ly/vierofernandobrainly)\n[Geometry Dash](https://gdbrowser.com/profile/knowncreator56)', inline='True')
            embed.add_field(name='Version Info', value='**Bot version: ** '+bot_ver+'\n**Update time: **'+str(latest_update)[:-7]+' UTC\n**Changelog: **'+bot_changelog+'\n**Uptime: **'+str(datetime.datetime.now()-latest_update)[:-7]+'\n\n**Discord.py version: **'+str(discord.__version__)+'\n**Python version: **'+str(sys.version).split(' (default')[0]+'\n**C Compiler Version:** '+str(sys.version).split('[GCC ')[1][:-1])
            embed.add_field(name='Links', value='[Invite this bot to your server!](http://vierofernando.github.io/programs/username601) | [Source code](http://github.com/vierofernando/username601) | [The support server!](http://discord.gg/HhAPkD8) | [Vote us on top.gg](https://top.gg/bot/696973408000409626/vote)', inline='False')
            embed.set_thumbnail(url='https://raw.githubusercontent.com/vierofernando/username601/master/username601.png')
            embed.set_footer(text='© Viero Fernando Programming, 2018-2020. All rights reserved.')
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'vote'):
            embed = discord.Embed(title='Support by Voting us at top.gg!', description='Umm, ya like this bot? err... sure thing dude! [Vote us at top.gg by clicking me!](https://top.gg/bot/696973408000409626/vote)', colour=discord.Colour.blue())
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'time') or msg.startswith(prefix+'utc'):
            response = urllib.request.urlopen("http://worldtimeapi.org/api/timezone/africa/accra")
            data = json.loads(response.read())
            year = str(data["utc_datetime"])[:-28]
            time = str(data["utc_datetime"])[:-22]
            date = str(data["utc_datetime"])[:-13]
            date = str(date)[11:]
            if int(year)%4==0:
                yearType = 'It is a leap year.'
                yearLength = 366
            else:
                yearType = 'It is not a leap year yet.'
                yearLength = 365
            progressDayYear = round(int(data["day_of_year"])/int(yearLength)*100)
            progressDayWeek = round(int(data["day_of_week"])/7*100)
            embed = discord.Embed(
                title = str(date)+' | '+str(time),
                description = 'The current time showed is on UTC.\n**Unix Time:** '+str(data["unixtime"])+'\n**Day of the year: **'+str(data["day_of_year"])+' ('+str(progressDayYear)+'%)\n**Day of the week: **'+str(data["day_of_week"])+' ('+str(progressDayWeek)+'%)\n'+str(yearType),
                colour = discord.Colour.green()
            )
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'joke') or msg.startswith(prefix+'jokes'):
            response = urllib.request.urlopen("https://official-joke-api.appspot.com/jokes/general/random")
            data = json.loads(response.read())
            embed = discord.Embed(
                title = str(data[0]["setup"]),
                description = '||'+str(data[0]["punchline"])+'||',
                colour = discord.Colour.blue()
            )
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'qr'):
            content = msg[4:].replace(" ", "%20")
            link = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data="+str(content.lower())
            embed = discord.Embed(
                colour = 0xffffff
            )
            embed.set_author(name="Image not appearing? Try using this link.", url=str(link))
            embed.set_image(url=str(link))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'didyoumean'):
            if splitted[1]=='help':
                embed = discord.Embed(title='didyoumean command help', description='Type like the following\n'+prefix+'didyoumean [text1] [text2]\n\nFor example:\n'+prefix+'didyoumean [i am gay] [i am guy]', colour=discord.Colour.blue())
                embed.set_image(url='https://api.alexflipnote.dev/didyoumean?top=i%20am%20gay&bottom=i%20am%20guy')
            else:
                txt1 = msg.split('[')[1][:-2].replace(' ', '%20')
                txt2 = msg.split('[')[2][:-1].replace(' ', '%20')
                embed = discord.Embed(colour=discord.Colour.blue())
                embed.set_image(url='https://api.alexflipnote.dev/didyoumean?top='+str(txt1)+'&bottom='+str(txt2))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'challenge'):
            txt = msg[11:].replace(' ', '%20')
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url='https://api.alexflipnote.dev/challenge?text='+str(txt))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'median') or msg.startswith(prefix+'mean'):
            numArray = []
            i = 1
            try:
                while splitted[i]!="":
                    numArray.append(splitted[i])
                    i = int(i)+1
            except IndexError:
                print("Reached the limit.")
            if msg.startswith(prefix+'median'):
                if len(numArray)%2==0:
                    first = int(len(numArray))/2
                    second = int(first) # 1 2 3 4
                    first = int(first)-1
                    result = int(int(numArray[first])+int(numArray[second]))/2
                else:
                    resultPosition = int(len(numArray))-int(((len(numArray))-1)/2)
                    result = numArray[int(resultPosition)-1]
            if msg.startswith(prefix+'mean'):
                temp = 0
                for i in range(0, int(len(numArray))):
                    temp = int(temp)+int(numArray[i])
                result = int(temp)/int(len(numArray))
            await message.channel.send(str(result))
        if msg.startswith(prefix+"sqrt"):
            num = int(splitted[1])
            await message.channel.send(str(math.sqrt(int(num))))
        if msg.startswith(prefix+'reactnum'):
            emojiArr = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
            begin = int(splitted[1])
            end = int(splitted[2])+1
            errorLevel = 0
            if int(splitted[1])>10 or int(splitted[1])<0 or int(splitted[2])>10 or int(splitted[2])<0:
                errorLevel = 1
            if errorLevel==0:
                for i in range(int(begin), int(end)):
                    await message.add_reaction(emojiArr[i])
            elif errorLevel==1:
                await message.channel.send('Error: Invalid Integer.')
        if msg.startswith(prefix+'slap'):
            gifArr = ["https://tenor.com/vEDn.gif ", "https://tenor.com/QZpI.gif", "https://tenor.com/6i12.gif", "https://tenor.com/RTqL.gif", "https://tenor.com/rhrz.gif", "https://giphy.com/gifs/mary-steenburgen-vxvNnIYFcYqEE", "https://giphy.com/gifs/sweet-penguin-penguins-mEtSQlxqBtWWA", "https://giphy.com/gifs/sherlock-snape-gif-kTBjwh6IWbLPy", "https://giphy.com/gifs/slap-dog-slapping-lX03hULhgCYQ8", "https://tenor.com/QklT.gif", "https://tenor.com/1jyY.gif", "https://tenor.com/6zwG.gif"]
            msgArr = ["Slapped in the face!", "Lemme slap your face for a bit.", "Come here... **SLAP!**", "One slap for you,", "May i slap you?", "SLAP TIME!", "Press F, cuz we just slapped", "GIMME YOUR SLAPPABLE FACE,", "What time is it? **SLAP TIME!**"]
            await message.channel.send(random.choice(msgArr)+" "+str(splitted[1])+"\n"+random.choice(gifArr))
        if msg.startswith(prefix+'hbd'):
            gifArr = ["https://tenor.com/bcdeQ.gif", "https://tenor.com/4flE.gif", "https://tenor.com/3toj.gif", "https://tenor.com/SZbC.gif", "https://tenor.com/1C6f.gif", "https://tenor.com/rzE6.gif", "https://tenor.com/beutC.gif", "https://tenor.com/z9js.gif", "https://tenor.com/v353.gif", "https://tenor.com/wFWQ.gif", "https://tenor.com/OmS5.gif", "https://tenor.com/6BKT.gif", "https://tenor.com/scB9.gif", "https://tenor.com/bc2rQ.gif", "https://tenor.com/paQT.gif", "https://tenor.com/1C6f.gif", "https://tenor.com/GYmM.gif"]
            await message.channel.send("Happy birthday, "+str(splitted[1])+"!\n"+random.choice(gifArr))
        if msg.startswith(prefix+'choose'):
            array = []
            i = 1
            try:
                while splitted[i]!="":
                    array.append(splitted[i])
                    i = int(i)+1
            except IndexError:
                print("Reached the limit.")
            await message.channel.send(random.choice(array))
        if msg.startswith(prefix+'search'):
            query = msg[8:].replace(" ", "%20")
            embed = discord.Embed(
                title = 'Internet Searches for '+str(msg[8:]),
                color = 0xff0000
            ) # https://en.wikipedia.org/w/index.php?cirrusUserTesting=control&search=adasdssdasasd&title=Special%3ASearch&go=Go&ns0=1
            embed.add_field(name='Google Search', value='http://google.com/search?q='+str(query))
            embed.add_field(name='YouTube results', value='http://youtube.com/results?q='+str(query))
            embed.add_field(name='Wikipedia search', value='https://en.wikipedia.org/w/index.php?cirrusUserTesting=control&search='+str(query)+'&title=Special%3ASearch&go=Go&ns0=1')
            embed.add_field(name='\nInstagram Tag Search', value='https://www.instagram.com/explore/tags/'+str(query)+'/', inline="True")
            embed.add_field(name='Creative Commons Search', value='https://search.creativecommons.org/search?q='+str(query), inline="True")
            embed.add_field(name='WikiHow Search', value='https://www.wikihow.com/wikiHowTo?search='+str(query), inline="True")
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'emojify'):
            emojified = []
            emojiid = 0
            listed = list(msg[9:])
            for i in range(0, int(len(listed))):
                a = listed[i]
                if (a.isalpha()) == True:
                    emojified.append(":regional_indicator_"+str(a)+":")
                else:
                    numArr = [":zero:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:", ":nine:"]
                    if a=="1" or a=="2" or a=="3" or a=="4" or a=="5" or a=="6" or a=="7" or a=="8" or a=="9" or a=="0":
                        emojified.append(numArr[int(a)])
                    elif a=="?":
                        emojified.append(":question:")
                    elif a=="!":
                        emojified.append(":exclamation:")
                    elif a==" ":
                        emojified.append(null)
                    else:
                        emojiid = 1
            total = null.join(emojified)
            if emojiid==0:
                await message.channel.send(total)
            else:
                await message.channel.send('BadSymbolError: Error! You added an invalid symbol\nthat cannot be converted to emojis. Sorry.')
        if splitted[0]==prefix+'reverse':
            word = msg[9:]
            await message.channel.send(word[::-1])
        if msg.startswith(prefix+'leet'):
            array = list(str(msg)[6:])
            alph = list("abcdefghijklmnopqrstuvwxyz")
            total = []
            leeted = ["4", "6", "(", "cl", "3", "I=", "9", "/-/", "1", ")", "|<", "!", "^^", "^/", "0", "I°", "()_", "l^", "5", "-|_", "V", "VV", "><", "=|", "2", " "]
            for i in range(0, int(len(array))):
                for j in range(0, 28):
                    if array[i] in alph:
                        if array[i]==alph[j]:
                            posId = 0
                            chosePosition = int(j)-1
                            break
                    elif array[i]==" ":
                        posId = 1
                        chosePosition = 26
                        break
                if array[i] in alph and posId==0:
                    total.append(leeted[j])
                elif posId==1:
                    total.append(" ")
                else:
                    total.append(array[i])
            await message.channel.send("".join(total))
        if msg.startswith(prefix+'length'):
            word = str(msg)[8:]
            withSpaces = 0
            withoutSpaces = 0
            for i in range(0, len(word)):
                if list(word)[i]==" ":
                    withSpaces = int(withSpaces)+1
                else:
                    withSpaces = int(withSpaces)+1
                    withoutSpaces = int(withoutSpaces)+1
            await message.channel.send("**With Spaces:** "+str(withSpaces)+"\n**Without Spaces:**"+str(withoutSpaces))
        if msg.startswith(prefix+'randomword'):
            toEdit = await message.channel.send('Please wait...')
            response = urllib.request.urlopen("https://random-word-api.herokuapp.com/word?number=1")
            data = json.loads(response.read())
            await toEdit.edit(content=str(data[0]))
        if msg.startswith(prefix+'inspirobot'):
            url = 'https://inspirobot.me/api?generate=true'
            img = requests.get(url)
            embed = discord.Embed(
                colour = 0xff0000
            )
            embed.set_image(url=str(img.text))
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'meme'):
            response = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")
            data = json.loads(response.read())
            embed = discord.Embed(
                colour = 0x00ff00
            )
            embed.set_author(name=data["title"], url=data["postLink"])
            embed.set_image(url=data["url"])
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'binary'):
            if len(splitted)==1:
                await message.channel.send(f'Please send something to encode to binary!\nExample: `{prefix}binary {msgAuthor}`')
            else:
                text = message.content[int(len(splitted[0])+1):]
                if len(myself.bin(text))>4096:
                    await message.channel.send('The binary result is too long... '+myself.bin('lol uwu'))
                else:
                    await message.channel.send(f'```{myself.bin(text)}```')
        if msg.startswith(prefix+'bored'):
            response = urllib.request.urlopen("https://www.boredapi.com/api/activity?participants=1")
            data = json.loads(response.read())
            await message.channel.send('**Feeling bored?**\nWhy don\'t you '+str(data['activity'])+'? :wink::ok_hand:')
        if msg.startswith(prefix+'8ball'):
            response = urllib.request.urlopen("https://yesno.wtf/api")
            data = json.loads(response.read())
            if data['answer']=='no':
                colorhex = discord.Colour.red()
            else:
                colorhex = discord.Colour.blue()
            embed = discord.Embed(title=data['answer'], colour=colorhex)
            embed.set_image(url=data['image'])
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'deathnote'):
            member = []
            in_the_note = ""
            notecount = 0
            membercount = 0
            for i in range(0, int(len(message.guild.members))):
                if message.guild.members[i].name!=msgAuthor:
                    member.append(message.guild.members[i].name)
                    membercount = int(membercount) + 1
            chances = ['ab', 'abc', 'abcd']
            strRandomizer = random.choice(chances)
            for i in range(0, int(membercount)):
                if random.choice(list(strRandomizer))=='b':
                    notecount = int(notecount) + 1
                    in_the_note = in_the_note+str(notecount)+'. '+ str(member[i]) + '\n'
            death = random.choice(member)
            count = random.choice(list(range(0, int(membercount))))
            embed = discord.Embed(
                title=message.guild.name+'\'s death note',
                description=str(in_the_note),
                colour = discord.Colour.from_rgb(255, 255, 0)
            )
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'lovelevel'):
            nums = list(range(0, 100))
            if len(splitted)==1:
                await message.channel.send('Error: Please mention someone you love (lenny)')
            elif len(splitted)==2:
                await message.channel.send('Love level of '+msgAuthor+' with <@!'+str(splitted[1][3:][:-1])+'> is **'+str(random.choice(nums))+'%.**')
        if msg.startswith(prefix+'gaylevel'):
            if len(splitted)==1:
                await message.channel.send('SomeoneError: Say/mention someone!')
            else:
                nums = list(range(0, 101))
                await message.channel.send('The gayness level of '+msg[10:]+' is **'+str(random.choice(nums))+'%.**')
        if msg.startswith(prefix+'secret'):
            member = []
            for i in range(0, int(len(message.guild.members))):
                if message.guild.members[i].name!=msgAuthor and message.guild.members[i].name!=msgAuthor:
                    member.append(message.guild.members[i].name)
            secretlist = splashes.getSecrets()
            await message.author.send('Did you know?\n'+random.choice(member)+str(random.choice(secretlist))+'\nDon\'t tell this to anybody else.')
            await message.channel.send('I shared the secret through DM. don\'t show anyone else! :wink::ok_hand:')
        if msg.startswith(prefix+'reactmsg'):
            messageReact = list(msg[10:])
            used = []
            order = list("abcdefghijklmnopqrstuvwxyz!?0123456789 ")
            validId = 0
            emo = ["🇦", "🇧", "🇨", "🇩", "🇪", "🇫", "🇬", "🇭", "🇮", "🇯", "🇰", "🇱", "🇲", "🇳", "🇴", "🇵", "🇶", "🇷", "🇸", "🇹", "🇺", "🇻", "🇼", "🇽", "🇾", "🇿", "❗", "❓", '0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '▪️']
            if len(messageReact)<20:
                for i in range(0, int(len(messageReact))):
                    if messageReact[i] in used:
                        await message.channel.send('Error: Your message contain multiple characters. Which is not allowed on reactions.')
                        validId = 1
                        break
                    else:
                        if messageReact[i] in order:
                            for j in range(0, int(len(order))):
                                if messageReact[i]==str(order[j]):
                                    used.append(emo[j])
                        else:
                            await message.channel.send('Error: Your message contain invalid symbols.\nValid: Alphabet Number ? ! space')
                            break
            else:
                await message.channel.send('Error! Your message contain more than 20 characters.\nWhich is the react message limit.')
            if validId==0:
                for i in range(0, int(len(used))):
                    await message.add_reaction(used[i])
        if msg.startswith(prefix+'wonka') or msg.startswith(prefix+'avmeme') or msg.startswith(prefix+'buzz') or msg.startswith(prefix+'doge') or msg.startswith(prefix+'fry') or msg.startswith(prefix+'philosoraptor') or msg.startswith(prefix+'money'):
            if msg.startswith(prefix+'avmeme'):
                try:
                    av = message.mentions[0].avatar_url
                    mes = msg[int(len(splitted[0])+len(splitted[1])+1):].replace(' ', '%20')
                    top = mes.split('[')[1].split(']')[0]
                    bott = mes.split('[')[2].split(']')[0]
                    name = 'custom'
                    extr = '?alt='+str(av).replace('webp', 'png')
                    embed = discord.Embed(colour=discord.Colour.green())
                    print('https://memegen.link/'+str(name)+'/'+str(top)+'/'+str(bott)+'.jpg'+str(extr))
                    embed.set_image(url='https://memegen.link/'+str(name)+'/'+str(top)+'/'+str(bott)+'.jpg'+str(extr))
                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f'```{e}```Invalid parameters. Example: `{prefix}avmeme <tag someone> [top text] [bottom text]`')
            else:
                try:
                    mes = msg[int(len(splitted[0])+1):].replace(' ', '%20')
                    top = mes.split('[')[1].split(']')[0]
                    bott = mes.split('[')[2].split(']')[0]
                    name = splitted[0][1:]
                    embed = discord.Embed(colour=discord.Colour.green())
                    embed.set_image(url='https://memegen.link/'+str(name)+'/'+str(top)+'/'+str(bott)+'.jpg?watermark=none')
                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f'```{e}```Invalid parameters.')
        if msg.startswith(prefix+'barcode'):
            if len(splitted)==1:
                await message.channel.send('Please provide a text!')
            else:
                if '/' in msg or '?' in msg:
                    await message.channel.send('Please input one without `/` or `?`!')
                else:
                    embed = discord.Embed(title='Barcode for '+str(msg[int(len(splitted[0])+1):]), colour=discord.Colour.blue())
                    embed.set_image(url='http://www.barcode-generator.org/zint/api.php?bc_number=20&bc_data='+str(msg[int(len(splitted[0])+1):]).replace(' ', '%20'))
                    await message.channel.send(embed=embed)
        if msg.startswith(prefix+'weather'):
            # site: wttr.in/Jakarta.png?m
            if len(splitted)==1:
                await message.channel.send(f'Please send a **City name!**\nExample: `{prefix}weather New York`')
            else:
                embed = discord.Embed(
                    title='Weather Report in '+str(msg[int(len(splitted[0])+1):]),
                    colour=discord.Colour.blue()
                )
                embed.set_image(url='https://wttr.in/'+str(msg[int(len(splitted[0])+1):]).replace(' ', '%20')+'.png?m')
                await message.channel.send(embed=embed)
        if msg.startswith(prefix+'github'):
            git = ''
            for i in range(0, len(github_object['files'])):
                git = git + '**'+github_object['files'][i]['name']+'** = '+github_object['files'][i]['type']+'\n'
            embed = discord.Embed(
                title=splashes.getGitMsg(),
                description='To visit my github, [Click this link.](http://github.com/vierofernando/username601).\nYou as a dev can see *how bad i am at programming, detect codes that i copied from stackoverflow, and probably copy-paste my bot\'s code to your bot :wink:*\n\n'+str(git),
                colour=discord.Colour.red()
            )
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'quote'):
            data = requests.get('https://quotes.herokuapp.com/libraries/math/random').text
            text = data.split(' -- ')[0]
            quoter = data.split(' -- ')[1]
            embed = discord.Embed(title='Quotes', description=text+'\n\n - '+quoter+' - ', colour=discord.Colour.blue())
            await message.channel.send(embed=embed)
        if msg.startswith(prefix+'trivia'):
            try:
                wait = await message.channel.send('Please wait... generating quiz...')
                auth = message.author
                data = json.loads(urllib.request.urlopen('https://wiki-quiz.herokuapp.com/v1/quiz?topics=Science').read())
                q = random.choice(data['quiz'])
                choices = ''
                for i in range(0, len(q['options'])):
                    al = list('ABCD')
                    if q['answer']==q['options'][i]:
                        corr = al[i]
                    choices = choices +'**'+ al[i] +'.** '+ q['options'][i]+'\n'
                embed = discord.Embed(title='Trivia!', description='**'+q['question']+'**\n'+choices, colour=discord.Colour.green())
                embed.set_footer(text='Answer in the letter corresponding to the choices. You have 60 seconds.')
                await wait.edit(content='', embed=embed)
            except Exception as e:
                await wait.edit(content=f'An error occured!\nReport this using {prefix}feedback.\n```{e}```')
            def check(m):
                return m.author == auth and len(m.content)==1
            try:
                trying = await client.wait_for('message', check=check, timeout=60.0)
            except:
                await message.channel.send('You are too late. Trivia ended. The answer is **'+corr+'**.')
            if str(trying.content).lower()==corr:
                await message.channel.send('You are correct! :nerd:')
            else:
                await message.channel.send('Wrong... The answer is **'+corr+'** :x:')
        if msg.startswith(prefix+'rhyme'):
            if len(splitted)==1:
                await message.channel.send('Please input a word! And we will try to find the word that best rhymes with it.')
            else:
                wait = await message.channel.send('Please wait... Searching...')
                data = json.loads(urllib.request.urlopen('https://rhymebrain.com/talk?function=getRhymes&word='+str(msg[int(len(splitted[0])+1):]).replace(' ', '%20')).read())
                words = ''
                if len(data)<1:
                    await wait.edit(content='We did not find any rhyming words corresponding to that letter.')
                else:
                    for i in range(0, len(data)):
                        if data[i]['flags']=='bc':
                            words = words + data[i]['word']+ ', '
                    if len(words)>1950:
                        await wait.edit(content='There seemed to be *so many* words to be listed. Sorry.')
                    else:
                        embed = discord.Embed(title='Words that rhymes with '+msg[int(len(splitted[0])+1):]+':', description=words, colour=discord.Colour.blue())
                        await wait.edit(content='', embed=embed)
print('Logging in to discord...')
client.run(os.environ['DISCORD_TOKEN'])