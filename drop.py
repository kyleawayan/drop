from redbot.core import commands # pylint: disable=import-error
import random # pylint: disable=import-error
import discord # pylint: disable=import-error
import os.path # pylint: disable=import-error
from redbot.core.utils.menus import start_adding_reactions # pylint: disable=import-error
from redbot.core.utils.predicates import ReactionPredicate # pylint: disable=import-error

class drop(commands.Cog):
    """Randomly select Fortnite locations"""

    @commands.command()
    async def drop(self, ctx): # !drop command
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
            "risky! E3", ## unmarked locations below
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
            map = "map/risky.png"
            unmarked = 1

        if "apres ski" in thedrop:
            map = "map/apreski.png"
            unmarked = 1

        if "box factory" in thedrop:
            map = "map/boxfactory.png"
            unmarked = 1

        if "compact cars" in thedrop:
            map = "map/compactcars.png"
            unmarked = 1

        if "crash site" in thedrop:
            map = "map/crashsite.png"
            unmarked = 1

        if "coral cove" in thedrop:
            map = "map/coralcove.png"
            unmarked = 1

        if "fancy view" in thedrop:
            map = "map/fancyview.png"
            unmarked = 1

        if "fn radio!" in thedrop:
            map = "map/fnradio.png"
            unmarked = 1

        if "hydro 16!" in thedrop:
            map = "map/hydro16.png"
            unmarked = 1

        if "lockie's light house" in thedrop:
            map = "map/lockielighthouse.png"
            unmarked = 1

        if "logjam woodworks" in thedrop:
            map = "map/logjam.png"
            unmarked = 1
        
        if "pristine point" in thedrop:
            map = "map/pristine.png"
            unmarked = 1

        if "orchard!" in thedrop:
            map = "map/orchard.png"
            unmarked = 1

        if unmarked == 0:
            repeat = await ctx.send(thedrop)
        else:
            await ctx.send(thedrop)
            # relative path
            # a.k.a. use "map/orchard.png" instead of "home/ubuntu/.local/share/Red-DiscordBot bla bla bla"
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, map)
            repeat = await ctx.send(file=discord.File(path))

        start_adding_reactions(repeat, "🔁")
        pred = ReactionPredicate.with_emojis("🔁", repeat)
        await ctx.bot.wait_for("reaction_add", check=pred)
        await ctx.send("test") #code to replay command goes here