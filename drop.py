from redbot.core import commands # pylint: disable=import-error
import random # pylint: disable=import-error
import discord # pylint: disable=import-error
import os.path # pylint: disable=import-error
from redbot.core.utils.menus import start_adding_reactions # pylint: disable=import-error
from redbot.core.utils.predicates import ReactionPredicate # pylint: disable=import-error
import asyncio # pylint: disable=import-error

class drop(commands.Cog):
    """Randomly select Fortnite locations"""

    @commands.command()
    async def drop(self, ctx): # !drop command

 #       my_path = os.path.abspath(os.path.dirname(__file__))
  #      path = os.path.join(my_path) # relative path
    #    for file in os.listdir(path):
     #       if file.endswith(".png"):
      #          await ctx.send(os.path.join("/mydir", file))
        
        shark = "The Shark!"
        yacht = "The Yacht!"
        grotto = "The Grotto!"
        rig = "The Rig!"
        craggy = "Craggy Cliffs!"
        steamy = "Steamy Stacks"
        pleasant = "Pleasant Park"
        sweaty = "Sweaty Shores"
        frenzy = "Frenzy Farm!"
        dirty_docks = "Dirty Docks!"
        holly_hedges = "Holly Hedges!"
        weeping_woods = "Weeping Woods!"
        lazy = "Lazy Lake!"
        retail = "Retail Row!"
        slurpy = "Slurpy Swamp!"
        misty = "Misty Meadows!"
        apreski = "Apres Ski! (E8)"
        boxfactory = "Box Factory! (G7)"
        compactcars = "Compact Cars! (G4)"
        coralcove = "Coral Cove! (A2)"
        crashsite = "Crash Site! (B2)"
        fancyview = "Fancy View! (A4)"
        fnradio = "FN Radio (F2)"
        hydro16 = "Hydro 16! (D7)"
        lockielighthouse = "Lockie's Lighthouse! (B6)"
        logjam = "Logjam Woodworks! (B6)"
        orchard = "The Orchard! (F3)"
        pristine = "Pristine Point! (G1)"
        risky = "Risky Reels! (E3)"


        marked_list = [
            'shark',
            'yacht',
            'grotto',
            'rig',
            'craggy cliffs',
            'steamy stacks',
            'pleasant park',
            'sweaty sands',
            'frenzy farm',
            'dirty docks',
            'holly hedges',
            'weeping woods',
            'lazy lake',
            'retail row',
            'slurpy swamp',
            'misty meadows'            
        ]
        unmarked_list = [
            "apres ski",
            "box factory",
            "compact cars",
            "coral cove",
            "crash site",
            "fancy view",
            "fn radio",
            "hydro 16",
            "lockies lighthouse",
            "logjam woodworks",
            "orchard",
            "pristine point",
            "risky reels"
        ]
        if random.randint(1,2) == 1:
            the_drop = random.choice(marked_list)
            unmarked = False
        else:
            the_drop = random.choice(unmarked_list)
            unmarked = True
            drop_map = f'map/{the_drop}.png'

        if unmarked == False:
            repeat = await ctx.send(the_drop)
            await ctx.send(the_drop)
        if unmarked == True:
            await ctx.send(the_drop)
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, drop_map)
            repeat = await ctx.send(file=discord.File(path))

            start_adding_reactions(repeat, "🔁")
            pred = ReactionPredicate.with_emojis("🔁", repeat)
            await ctx.bot.wait_for("reaction_add", check=pred)
            await ctx.send("fuck you")