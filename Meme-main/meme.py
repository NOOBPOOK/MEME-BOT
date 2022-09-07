import nextcord
from nextcord.ui import Button, View 
from nextcord.utils import get
from nextcord.ext import commands
import os
from dotenv import load_dotenv
import wikipedia
import smtplib
import datetime
import webbrowser
import youtube_dl
import humanfriendly
import time
import random
import asyncio
import asyncpraw

reddit = asyncpraw.Reddit(client_id= "poL3KE8PgI8doxJB7-aYGw",
                     client_secret = "2aSpJ5aiEmLHKwvkTGE61DblaIM-aw",
                     username = "Advanced_Daikon756",
                     password = "#noobpookveduki1234",
                     user_agent = "scrbot")

intents = nextcord.Intents(messages = True, message_content=True, guilds = True, voice_states = True, members=True)
client = commands.Bot(command_prefix="*", help_command=None, intents=intents)

@client.event
async def on_ready():
    print("Bot just landed on the server!")
  
@client.event
async def on_member_join(member):
    myEmbed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description="Welcome to the Server!", color=0xffff00)
    myEmbed.add_field(name="🤖" ,value = member.mention, inline=False)
    myEmbed.add_field(name="Description:-",value="The Offical Server of -SCRUNCHY- channel on youtube!", inline=False)
    myEmbed.set_footer(text="Explore outside while being inside \n #DISCORD😎")
    myEmbed.set_author(name="Reddit Meme Bot#4970")
    chn = client.get_channel(960054719865294908)
    await chn.send(embed=myEmbed)
    
@client.event
async def on_member_remove(member):
    mem_rol = member.roles
    myEmbed = nextcord.Embed(title = "-SCRUNCHYPLANET🌎-", description=f"{member} has just left the server!", color=0xffff00)
    myEmbed.add_field(name= "ROLES:-" ,value=('\n'.join(map(str, mem_rol))), inline=False)
    myEmbed.add_field(name="❌",value="The above user with the concerned roles have left the server!", inline=False)
    myEmbed.set_author(name="Reddit Meme Bot#4970")
    chn = client.get_channel(960054719865294908)
    await chn.send(embed=myEmbed)
    
@client.command()
async def meme(ctx):
    all_subs = []
    subreddit = await reddit.subreddit("memes","jokes")
    top_red = subreddit.top("day", limit=50)
    print("Running!")
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    #print(url)
    if url.endswith(".jpg") or url.endswith(".png") or url.endswith(".gif"):
        memEmbed = nextcord.Embed(title= name)
        memEmbed.set_image(url = url)
        ctx_mem = await ctx.send(embed = memEmbed)
        await meme_but(ctx,ctx_mem)
    else:
        ctx_mem = await ctx.send(content = url)
        await meme_but(ctx,ctx_mem)
        
async def meme_but(ctx,ctx_mem):
    button = Button(label="Yes", style=nextcord.ButtonStyle.green, emoji="🤚")
    view = View(timeout=100)
    view.add_item(button)
    async def button_callback(interaction):
        await mem_rep(ctx,ctx_mem)
    button.callback = button_callback
    await ctx.reply(view = view)
        
async def mem_rep(ctx,ctx_mem):
    all_subs = []
    subreddit = await reddit.subreddit("memes","jokes")
    top_red = subreddit.top("day", limit=50)
    async for top_hot in top_red:
        all_subs.append(top_hot)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    #print(url)
    if url.endswith(".jpg") or url.endswith(".png") or url.endswith(".gif"):
        memEmbed = nextcord.Embed(title= name)
        memEmbed.set_image(url = url)
        await ctx_mem.edit(embed = memEmbed)
    else:
        await ctx_mem.edit(content = url)
 
            
client.run("******BOT-TOKEN******")
