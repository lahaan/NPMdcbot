import discord
import responses
import data


async def send_message(username, message, user_message):
    try:
        response = responses.get_response(user_message)
        if user_message == data.choice4 and response[:1] == 'h':
            await message.channel.send(f'{username}, {data.random_copypasta4}')
            await message.channel.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = data.dc_token
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

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.lower() in data.written_message_list:
            await send_message(username, message, 'kn')

        if user_message[0] == '!' or user_message[:3].lower() == 'pls':
            if user_message[0] == '!':
                user_message = user_message[1:].lower()
            else:
                user_message = user_message[4:].lower()
            await send_message(username, message, user_message)

    client.run(TOKEN)
