import discord
import responses


async def send_message(username, message, user_message):
    try:
        response = responses.get_response(user_message)
        if user_message == 'star' and response[:1] == 'h':
            await message.channel.send(f'{username}, you are such a nice guy (over 95% to be exact)')
            await message.channel.send(response)
        else:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = ''
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message.lower() in ['choice1', 'choice2']:
            await send_message(username, message, 'kn')

        if user_message[0] == '!':
            user_message = user_message[1:].lower()
            await send_message(username, message, user_message)

    client.run(TOKEN)