import os
import random
import discord
from discord.ext import commands

# Enable intent for reading message content
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    """Logs successful bot connection to Discord gateway."""
    print(f'Logged in successfully as {bot.user} (ID: {bot.user.id})')


@bot.command(name='hello')
async def hello(ctx):
    """Responds with a greeting message."""
    await ctx.send(f'Hello! I am {bot.user}, your Discord assistant!')


@bot.command(name='add')
async def add(ctx, left: int, right: int):
    """Adds two integers together."""
    await ctx.send(f'Result: {left + right}')


@add.error
async def add_error(ctx, error):
    """Error handler for invalid arguments in add command."""
    if isinstance(error, commands.BadArgument):
        await ctx.send('Please provide valid integers (e.g., `$add 5 10`).')


@bot.command(name='roll')
async def roll(ctx, dice: str):
    """Rolls dice in NdN format (e.g. 2d6)."""
    try:
        rolls, limit = map(int, dice.split('d'))
        if rolls <= 0 or limit <= 0 or rolls > 20:
            await ctx.send('Please specify between 1 and 20 dice with positive sides.')
            return

        results = [str(random.randint(1, limit)) for _ in range(rolls)]
        await ctx.send(f'🎲 Rolls: {", ".join(results)}')
    except ValueError:
        await ctx.send('Invalid format! Use NdN format (e.g., `$roll 2d6` or `$roll 1d20`).')


if __name__ == '__main__':
    TOKEN = os.environ.get('DISCORD_TOKEN', '')
    if TOKEN:
        bot.run(TOKEN)
    else:
        print("[Error] DISCORD_TOKEN environment variable is missing.")
