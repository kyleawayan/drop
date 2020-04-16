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
            'shark!',
            'yacht!',
            'grotto!',
            'rig!',
            'craggy cliffs!',
            'steamy stacks!',
            'pleasant park!',
            'sweaty sands!',
            'frenzy farm!',
            'dirty docks!',
            'holly hedges!',
            'weeping woods!',
            'lazy lake!',
            'retail row!',
            'slurpy swamp!',
            'misty meadows!' 
        ]
        
        # before '!' has to correspond with picture in /map/ 
        unmarked_list = [ 
            'apres ski! D8',
            'box factory! G7',
            'compact cars! G4',
            'coral cove! A2',
            'crash site! B2',
            'fancy view! A4',
            'fn radio! F2',
            'hydro 16! D7',
            'lockies lighthouse! C1',
            'logjam woodworks! B6',
            'orchard! F3',
            'pristine point! G1',
            'risky reels! E4'
        ]

        if random.randint(1,2) == 1:
            the_drop = random.choice(marked_list)
            unmarked = False
        else:
            the_drop = random.choice(unmarked_list)
            drop_filename = the_drop[:-4]
            unmarked = True
            drop_map = f'map/{drop_filename}.png'

        if unmarked == False:
            repeat = await ctx.send(the_drop)

        if unmarked == True:
            await ctx.send(drop_filename)
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, drop_map)
            repeat = await ctx.send(file=discord.File(path))

        start_adding_reactions(repeat, "🔁")
        pred = ReactionPredicate.with_emojis("🔁", repeat)
        await ctx.bot.wait_for("reaction_add", check=pred) 
        await ctx.invoke(self.drop)