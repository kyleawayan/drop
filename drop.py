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
    async def drop(self, ctx): # ?drop command

        # locations without picture (labeled)
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
        
        #locations with corresponding picture in /map/
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

        #random list
        if random.randint(1,2) == 1:
            the_drop = random.choice(marked_list)
            unmarked = False
        else:
            the_drop = random.choice(unmarked_list)
            unmarked = True
            drop_map = f'map/{the_drop}.png'

        if unmarked == False:
            repeat = await ctx.send(the_drop + '!')

        if unmarked == True:
            await ctx.send(the_drop + '!')
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, drop_map)
            repeat = await ctx.send(file=discord.File(path))

        start_adding_reactions(repeat, "🔁")
        pred = ReactionPredicate.with_emojis("🔁", repeat)
        await ctx.bot.wait_for("reaction_add", check=pred)
        await ctx.send("no fuck you that doesn't work yet")