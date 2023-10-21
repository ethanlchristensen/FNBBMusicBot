import discord
import youtube_dl
from discord.ext import commands
from discord import app_commands


class Stream(commands.GroupCog, name="stream"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()
    
    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Must be in voice channel to play music.")
        voice_channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)
        
    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def play(self, ctx, url):
        try:
            ctx.voice_client.stop()
        except:
            pass

        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        YTDL_OPTIONS = {
            'format': 'bestaudio'
        }

        vc = ctx.voice_client

        if vc:
            with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ytdl:
                info = ytdl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                print("now trying to play . . .")
                try:
                    vc.play(source)
                except:
                    await ctx.send("Brotha, I tried to play it, I really did . . .")
        else:
            await ctx.send("I AINT IN A VC!")
    
    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("paused")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("resumed")
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Stream(bot))
