import discord

LIMIT = 1000000

async def specificangelo(message, word):
    if word == "":
        await message.channel.send("Please provide a string")
        return
    chan = message.channel
    count = 0
    totalmsg = 0
    newmsg = await message.channel.send("Counting...")
    async with message.channel.typing():
        async for msg in chan.history(limit=LIMIT):
            totalmsg += 1
            if msg.author == message.author and word.lower() in message.content.lower():
                count+=1
        await newmsg.delete()
    await message.channel.send(message.author.nick + " has said " + word + " " + str(count) + " many times in " + str(message.channel))

async def angelo(message):
    chan = message.channel
    count = 0
    totalmsg = 0
    newmsg = await message.channel.send("Counting...")
    async with message.channel.typing():
        async for msg in chan.history(limit=LIMIT):
            totalmsg += 1
            if msg.author == message.author:
                count+=1
        await newmsg.delete()
        await message.channel.send(message.author.nick + " has accounted for " + str((count/totalmsg)*100) + "% of all messages in " + str(message.channel))
    if message.author.nick == "Angelo Nelson":
        await message.channel.edit(topic = "Pretty much just Angelo saying dumb shit " + str((count/totalmsg)*100) + "% of the time")
        await message.channel.send("Based on " + str(totalmsg) + " messages")

async def bigangelo(message):
    chan = message.channel
    users = {}
    result = ""
    totalmsg = 0
    newmsg = await message.channel.send("Counting...")
    async with message.channel.typing():
        async for msg in chan.history(limit=LIMIT):
            try:
                if msg.author.nick == None:
                    name = msg.author
                else:
                    name = msg.author.nick
            except:
                name = msg.author
            totalmsg+=1
            if name not in users:
                users[name] = 1
            else:
                users[name] = users[name] + 1
        sortedusers = dict(sorted(users.items(),key= lambda x:x[1], reverse=True))
        await newmsg.delete()
        for k, v in sortedusers.items():
            await message.channel.send("***"+str(k)+"***" + " has accounted for " + "***"+str((v/totalmsg)*100) + "%*** of all messages in " + str(message.channel))
    await message.channel.send("Based on " + str(totalmsg) + " messages")
    