import requests
def getGeoQuiz():
    return ['capital', 'region', 'subregion', 'population', 'demonym', 'nativeName']
def getBinary(a):
    if a==2:
        arr = ["10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001"]
    else:
        arr = ["00001", "00010", "00011", "00100", "00101", "000110", "00111", "01000", "01001", "01010", "01011", "01100", "01101", "01110", "01111", "10000", "10001", "10010", "10011", "10100", "10101", "10110", "10111", "11000", "11001", "11010"]
    return arr
def getSecrets():
    arr = [
        ' is sleeping.',
        ' is breathing.',
        ' is about to ||do something.||',
        ' likes you.',
        ' hates you.',
        ' wanted to confess something.', 
        ' is the guy behind HowToBasic.',
        ' is the person secretly running the USA government.',
        ' is jeff the killer.',
        ' is the guy behind the development of Username601.',
        ' is hacking the server.',
        ' is hacking discord.',
        ' likes sh||oo||ting people.',
        ' likes p||hoto||graphy.',
        ' likes going to ||git||hub.com to have some fun.',
        ' is cool.',
        ' is smart af.',
        ' is the guy behind you.',
        ' is a nerd.',
        ' likes schools.',
        ' is the guy spying behind you.',
        ' has a secret youtube channel.',
        ' is a cool programmer.',
        ' is a nice guy, not worth telling secrets tho!',
        ' is a discord user :v',
        ' is breathing.',
        ' umm... maybe i shouldn\'t tell his secrets.',
        ' is secretly a bot. yes, selfbot.',
        ' is... umm.. :flushed:',
        ' is the hacker that will RULE the world.'
    ]
    return arr
def getAsciiFonts():
    arr_raw = requests.get("http://artii.herokuapp.com/fonts_list").text
    arr = arr_raw.split('\n')
    return arr
def getTag():
    arr = [
        "ya liek tagz?",
        "we don't accept services with tags, sorry.",
        "tag me? lol NO.",
        'why command me with a tag? that is so unnecessary!',
        'NO TAG, ~~NO~~ YES SERVICE.',
        'MORE TAG, LESS SERVICE.',
        'Everybody gangsta until somebody tagged username601',
        'Taggy taggy tag tag!',
        'Playin\' with tagz, bro?',
        'So uhh i heard u liek tagz',
        'What kind of word is that?',
        'tag me? why not tag everyone lul',
        'you liek tagging me huh uwu',
        'pinging me? why not >ping instead lol',
        'discord pings are not cool!',
        'i am busy, please don\'t ping me. thanks.',
        'bruh, pings? again?',
        'this is like, the 96024th time i am getting pinged.',
        'it seems that commands doesn\'t require for you to ping me...',
        'ping... pong...?',
        'Me: Noo you can\'t ping me!! ;(\nYou: hehe discord go ping ping'
    ]
    return arr
def getAbout():
    arr = [
        'Traceback (most recent call last)',
        'I liek memes',
        '601 in my name means BOT in leetspeak.\n*THE MORE YOU KNOW*',
        'Hello, discordians! It\'s-a-me. Bot. Which may look stupid the fact that\nthere are THOUSANS of discord bots out there, so *let\'s get straight into it.* (no meme intended)',
        'Wha? ME? okay then, here ya go.',
        'Here are some silly lil information.',
        'Beep boop, beep beep?',
        'JavaScript ~~sucks~~ is bad. (i was told to change it lmao)',
        'MEE6 vs Dyno, which is better?',
        'MEEx6=MEEMEEMEEMEEMEEMEE',
        'my token is = \*Slams head on keyboard*',
        'HELP? Please try >help. thanks',
        'Don\'t be a broom. Use discord.',
        'Discard the discord right away!',
        'Garbage bot giving some information here.',
        'look, i have challenge for you. Can you read this without blinking?',
        'Don\'t laugh at me.',
        'Python is for nerds.',
        'Everybody gangsta until username601 become self-aware',
        'Coding is not fun, but it will pay off.',
        'Hehe discord go ping ping',
        'Vote me in top.gg or i will take your pokecord credits',
        'And then you showed up. You dangerous, mute, lunatic.',
        'This bot is available for WhatsApp, Skype, AOL Instant Messenger, even Nokia phones also support me! :D',
        'V53\|2\|V4\|V\|3 BOT',
        'pizza time',
        'r/programmerhumor is my favourite subreddit, ~~cuz i am a nerd~~',
        'MEEP6',
        'Ha ha Username601 go vroom vroom',
        'Botname601',
        'Programmed *ENTIRELY* using Notepad',
        'Wanna be a madlad? Try programming a new language\n*WITHOUT LOOKING AT STACKOVERFLOW.*',
        'Top.gg is the platform where nerds flex their cool bots--\nAnd there is me, lonely :((('
        'I am the BEST programmer. I can do HTML',
        'HTML programmers >>> Java Programmers',
        'Only madlads use Discord.HTML lul',
        'Hello can i code minecraft using HTML pls thx',
        'only epic programmers use HTML',
        'print(\'Hella, World!\')',
        'PyScript or Javathon? :flushed:',
        'You can get to google if you know Machine code language LUL'
    ]
    return arr
def getTicTacToeHeader():
    arr = [
        'my cool banner',
        'mspaint.exe',
        'ew, worst banner 10/1',
        'myself',
        'someone',
        '@everyone',
        'random stranger',
        'a discard user',
        'a skype-hater',
        'a guy',
        'a cool guy',
        'a normal breathing person',
        'the chosen one',
        'impossible',
        'the g4m3r'
    ]
    return arr