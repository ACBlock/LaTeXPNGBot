import discord
from discord.ext import commands
import os

import matplotlib.pyplot as plt
import numpy as np

def plot_equation(eq, fontsize=50, outfile="test", padding=0.1, **kwargs):
    """Plot an equation as a matplotlib figure.
    Parameters
    ----------
    eq : string
        The equation that you wish to plot. Should be plottable with
        latex. If `$` is included, they will be stripped.
    fontsize : number
        The fontsize passed to plt.text()
    outfile : string
        Name of the file to save the figure to.
    padding : float
        Amount of padding around the equation in inches.
    Returns
    -------
    ax : matplotlib axis
        The axis with your equation.
    """
    # clean equation string
    eq = eq.strip('!tex').replace(' ', '')
    
    # set up figure
    f = plt.figure()
    ax = plt.axes([0,0,1,1])    
    r = f.canvas.get_renderer()

    # display equation
    t = ax.text(0.5, 0.5, '${}$'.format(eq), fontsize=fontsize,
        horizontalalignment='center',verticalalignment='center')
    
    # resize figure to fit equation
    bb = t.get_window_extent(renderer=r)
    w,h = bb.width/f.dpi,np.ceil(bb.height/f.dpi)
    f.set_size_inches((padding+w,padding+h))

    # set axis limits so equation is centered
    plt.xlim([0,1])
    plt.ylim([0,1])
    ax.grid(False)
    ax.set_axis_off()

    #outfile_name = "test" + str(np.random.rand_int(1,1000000))
    if outfile is not None:
        plt.savefig(outfile, **kwargs)

    return ax


#client = discord.Client()
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	print('LaTeX Bot is ready!')

@client.command()
async def tex(ctx):
	image = plot_equation(ctx.message.content)
	await ctx.send(file=discord.File(r'C:\Users\andre\Desktop\LaTeXBot\test.png'))



client.run(os.getenv('TOKEN'))