import discord
import random
import internal_db

client = discord.Client()
user = discord.User()
inapi = internal_db.InternalDB()

class InternalAPI:
    # async def initial_members_checklist():
    #     members_data = {}
    #     for server in client.servers:
    #         for member in server.members:
    #             members_data[member.id] = {'name': member.name,
    #                                        'display_name': member.name + '#' + member.discriminator,
    #                                        'bot': member.bot,
    #                                        'created_at': str(member.created_at)}
    #     if members_data != {}:
    #         print(members_data)
    #         print(list(members_data.keys()))
    #         return members_data, list(members_data.keys())
    #     else:
    #         raise ValueError

    def choose_pidor_randomly(self, pidors):
        pidors_id_list = list(pidors.keys())
        try:
            ran = random.randint(0, len(pidors_id_list) - 1)
            return pidors_id_list[ran]
        except:
            print("Failed to choose a pidor")

