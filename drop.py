from redbot.core import commands # pylint: disable=import-error
import random # pylint: disable=import-error
import discord # pylint: disable=import-error

class drop(commands.Cog):
    """Randomly select Fortnite locations"""

    @commands.command()
    async def drop(self, ctx):
        fortniteList = [
            "shark!",
            "yacht!",
            "agency!",
            "grotto!",
            "rig!",
            "craggy!",
            "steamy!",
            "pleasant!",
            "sweaty!",
            "frenzy!",
            "salty!",
            "dirty docks!",
            "holly hedges!",
            "weeping woods!",
            "lazy!",
            "retail!",
            "slurpy!",
            "misty!",
            "risky! E3", ## unmarked locations
            "apres ski! E8",
            "box factory! G7",
            "compact cars! G4",
            "crash site! B2",
            "coral cove! A2",
            "fancy view! A4",
            "fn radio! F2",
            "hydro 16! D7",
            "lockie's light house! C1",
            "logjam woodworks! B6",
            "pristine point! G1",
            "orchard! F3",
        ]

        thedrop = random.choice(fortniteList)

        unmarked = 0

        if "risky" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/risky.png"
            unmarked = 1

        if "apres ski" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/apreski.png"
            unmarked = 1

        if "box factory" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/boxfactory.png"
            unmarked = 1

        if "compact cars" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/compactcars.png"
            unmarked = 1

        if "crash site" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/crashsite.png"
            unmarked = 1

        if "coral cove" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/coralcove.png"
            unmarked = 1

        if "fancy view" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/fancyview.png"
            unmarked = 1

        if "fn radio!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/fnradio.png"
            unmarked = 1

        if "hydro 16!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/hydro16.png"
            unmarked = 1

        if "lockie's light house" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/lockielighthouse.png"
            unmarked = 1

        if "logjam woodworks" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/logjam.png"
            unmarked = 1
        
        if "pristine point" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/pristine.png"
            unmarked = 1

        if "orchard!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/orchard.png"
            unmarked = 1

        await ctx.send(thedrop)
        if unmarked is 1:
            await ctx.send(file=discord.File(map))

    @commands.command()
    async def where(self, ctx):
        fortniteList = [
            "shark!",
            "yacht!",
            "agency!",
            "grotto!",
            "rig!",
            "craggy!",
            "steamy!",
            "pleasant!",
            "sweaty!",
            "frenzy!",
            "salty!",
            "dirty docks!",
            "holly hedges!",
            "weeping woods!",
            "lazy!",
            "retail!",
            "slurpy!",
            "misty!",
            "risky! E3", ## unmarked locations
            "apres ski! E8",
            "box factory! G7",
            "compact cars! G4",
            "crash site! B2",
            "coral cove! A2",
            "fancy view! A4",
            "fn radio! F2",
            "hydro 16! D7",
            "lockie's light house! C1",
            "logjam woodworks! B6",
            "pristine point! G1",
            "orchard! F3",
        ]

        thedrop = random.choice(fortniteList)

        unmarked = 0

        if "risky" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/risky.png"
            unmarked = 1

        if "apres ski" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/apreski.png"
            unmarked = 1

        if "box factory" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/boxfactory.png"
            unmarked = 1

        if "compact cars" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/compactcars.png"
            unmarked = 1

        if "crash site" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/crashsite.png"
            unmarked = 1

        if "coral cove" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/coralcove.png"
            unmarked = 1

        if "fancy view" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/fancyview.png"
            unmarked = 1

        if "fn radio!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/fnradio.png"
            unmarked = 1

        if "hydro 16!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/hydro16.png"
            unmarked = 1

        if "lockie's light house" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/lockielighthouse.png"
            unmarked = 1

        if "logjam woodworks" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/logjam.png"
            unmarked = 1
        
        if "pristine point" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/pristine.png"
            unmarked = 1

        if "orchard!" in thedrop:
            map = "/home/ubuntu/.local/share/Red-DiscordBot/data/niki/cogs/CogManager/cogs/drop/map/orchard.png"
            unmarked = 1

        await ctx.send(thedrop)
        if unmarked is 1:
            await ctx.send(file=discord.File(map))