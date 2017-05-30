import discord
import internal_db
import internal_api
import config as cfg

client = discord.Client()
user = discord.User()
indb = internal_db.InternalDB()
inapi = internal_api.InternalAPI()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + '. CLIENT_ID: ' + client.user.id)
    print('------')
    print('Initiating pidors list')
    pidors = await prepare_dict_from_members()
    print('Performing db initialize...')
    indb.initial_connection_to_database()
    print('Performing initial import of members...')
    indb.initialize_import_to_database(pidors)
    print('------')

@client.event
async def on_message(message):
    pidors = await prepare_dict_from_members()

    #pidor
    if message.content.startswith('pidor') or message.content.startswith('пидор'):
        pid = inapi.choose_pidor_randomly(pidors)
        indb.increase_being_pidor_value(pid)
        indb.update_activity_table(pid)
        await client.send_message(message.channel, '<@' + str(pid) + '>')

    #ping
    if message.content.startswith('ping'):
        await client.send_message(message.channel, 'pong')

# Get all current members
async def prepare_dict_from_members():
    members_data = {}
    for server in client.servers:
        for member in server.members:
            if member.bot is False:
                members_data[member.id] = {'name': member.name,
                                           'display_name': member.name + '#' + member.discriminator,
                                           'bot': member.bot,
                                           'created_at': str(member.created_at)}
    if members_data != {}:
        return members_data
    else:
        raise ValueError

client.run(cfg.discord_client_token)