from redbot.core import commands
import random

class drop(commands.Cog):
    """Randomly select Fortnite locations"""

    def fortniteList = [
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
        "misty!", #unmarked waypoints below
        "risky!",
        "apreski!",
        "box factory!",
        "compact cars!", ##
        "crash site!",
        "coral cove!",
        "fancy view!",
        "fn radio!", ##
        "hydro 16!",
        "lockie's light house!",
        "logjam woodworks!",
        "pristine point!",
        "orchard!",
        ]

    @commands.command()

    async def drop(self, ctx):
        await ctx.send(random.choice(fortniteList))