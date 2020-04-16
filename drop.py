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
        
        #has to correspond with picture in /map/
        unmarked_list = { 
            1:"apres ski",
            2:"box factory",
            3:"compact cars",
            4:"coral cove",
            5:"crash site",
            6:"fancy view",
            7:"fn radio",
            8:"hydro 16",
            9:"lockies lighthouse",
            10:"logjam woodworks",
            11:"orchard",
            12:"pristine point",
            13:"risky reels"
        }
        
        unmarked_coors = {
            1: 'D8', # apres ski
            2: 'G7', # box factory
            3: 'G4', # compact cars
            4: '2', # coral cove
            5: '2', # crash site
            6: '2', # fancy view
            7: 'F2', # fn radio
            8: 'D7', # hydro 16
            9: 'C1', # lockies lighthouse
            10: 'B6', # logjam woodworks
            11: '', # orchard
            12: 'G1', # pristine point
            13: 'E4' # risky
        }

        #random list
        if random.randint(1,2) == 1:
            the_drop = random.choice(marked_list)
            unmarked = False
        else:
            rand_drop = random.randint(1,13)
            the_drop = unmarked_list.get(rand_drop)
            the_coors = unmarked_coors.get(rand_drop)
            unmarked = True
            drop_map = f'map/{the_drop}.png'

        if unmarked == False:
            repeat = await ctx.send(the_drop + '!')

        if unmarked == True:
            await ctx.send(the_drop + '! ' + the_coors)
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, drop_map)
            repeat = await ctx.send(file=discord.File(path))

        start_adding_reactions(repeat, "🔁")
        pred = ReactionPredicate.with_emojis("🔁", repeat)
        await ctx.bot.wait_for("reaction_add", check=pred) 
        await ctx.invoke(self.drop)