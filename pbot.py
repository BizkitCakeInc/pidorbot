import discord
import asyncio
import random
import time
from datetime import datetime

client = discord.Client()
user = discord.User()
# server = discord.Server()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + '. CLIENT_ID: ' + client.user.id)
    print('------')
    print('Performing initial import of members...')
    global pidors
    pidors = await initial_members_checklist()
    print('------')
    print('Performing file creation...')


@client.event
async def on_message(message):



    if message.content.startswith('pidor'):
        for i in pidors:
            await client.send_message(message.channel, '<@' + str(i) + '>')
            await client.send_message(message.channel, 'pong')

    # Default value to check that bot works at least
    if message.content.startswith('ping'):
        await client.send_message(message.channel, 'pong')

# Get all current members
async def initial_members_checklist():
    members_data = {}
    for server in client.servers:
        for member in server.members:
            members_data[member.id] = {'name': member.name,
                                       'display_name': member.name + '#' + member.discriminator,
                                       'bot': member.bot,
                                       'created_at': str(member.created_at)}
    if members_data != {}:
        print('Initial checklist verified successfully.')
        return member
    else:
        raise ValueError
    return members_data

client.run('MzE2OTI5MTUzNTIzOTA4NjA4.DAceDA.mkmAzQzSMyo8hjDBMoKLgAvBRlM')


# client_id = '316929153523908608'
# token = 'RXA80TFw6oPd4wVYx3uMINxXoQXdju_h'