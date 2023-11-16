import discord
import responses
import data
import json


async def send_message(message, user_message):
    try:
        if data.choices[13] in user_message.strip() and 'x' in user_message:
            x = 0
            x_list = []
            while x < int(user_message[8:]) and x < 50:
                x_list.append(f"{responses.get_response(data.choices[13])}\n")
                x += 1
            await message.channel.send(f'```{"".join(x_list)}```') if len(x_list) > 0 else\
                message.channel.send(data.choices[14])
        else:
            await message.channel.send(responses.get_response(user_message))

    except Exception as e:
        print(e)


def run_discord_bot():
    f = open("token.json")
    file_data = json.load(f)
    TOKEN = file_data["TOKEN"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username}: "{user_message}" ({channel})' if len(user_message) > 0 else '[nothing]')

        if user_message.lower() in data.written_message_list:
            await send_message(username, message, 'kn')

        if user_message[0] == '!' or user_message[:3].lower() == 'pls':
            if user_message[0] == '!':
                user_message = user_message[1:].lower()
            else:
                user_message = user_message[4:].lower()
            await send_message(username, message, user_message)

    client.run(TOKEN)
