import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('BOT DO JOAO ONLINE')
    print(client.user.name)
    print(client.user.id)
    print('------------------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('!say'):
        channel = message.channel
        await channel.send("Say Hello!!")

        def check(m):
            return m.content == 'hello' and m.channel == channel
        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!!'.format(msg))



client.run('NzEyMzcwMDc1MjEwMDg4NTIw.XsWZFg.bRWO-GUfB23WTT22hc0qkQTMo0g')