# Visualize equimaterial zones on a rolled cylinder

import numpy as np
import matplotlib.pyplot as plt

def product_remaining(r, R_new=3):
    """Fraction of product remaining by visible roll radius.

    Parameters
    ----------
    r : float, 1 <= r
        Visible radius of roll in units of r0, the cardboard cylinder radius.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0.

    Returns
    -------
    Current remaining length as fraction of original length of new roll.
    """

    x = r / R_new
    f = ( ( (R_new**2) * (x**2) ) - 1 ) / ((R_new**2) - 1)

    return f

def product_visible(el_frac, R_new=3):
    """Visible roll radius by fraction of remaining product.

    Parameters
    ----------
    el_frac : float, 0 <= el_frac <= 1
        Current remaining length as fraction of original length of new roll.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.

    Returns
    -------
    Current visible radius of roll, in units of r0, the cardboard cylinder
    radius.
    """

    f = el_frac
    x = np.sqrt( ( ( ((R_new**2)-1) * f ) + 1 ) / (R_new**2) )

    return x

def visualize_danger(n, R_new=3, saveas=''):
    """Use n line segments of equal product to visualize paradox of the roll.

    Parameters
    ----------
    n : int scalar
        Number of line segments to display.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.
    saveas : str, optional, default: empty
        If not empty save figure to file 

    Returns
    -------
    None
    """

    # Start with a new figure window
    plt.close('all') # this helps get rid of old figures you forgot to close
    fh = plt.figure(figsize=(8,6)) # my favorite figure size

    ### YOUR CODE HERE ###

    # Do the core plotting commands here
    ## use the functions defined above to calculate the line segments to plot
    fracs = np.linspace(0, 1, n + 1)        # fraction remaining at each boundary
    radii = product_visible(fracs, R_new)   # in units of R_new: 1/R_new ... 1

    ax = fh.add_subplot(1, 1, 1)
    ax.add_patch(plt.Circle((0, 0), radii[0], color='0.75'))   # shaded core
    for r in radii:
        ax.add_patch(plt.Circle((0, 0), r, fill=False, color='k'))

    # Label each ring's thickness, converted from units of R_new to units of r0
    thick = np.diff(radii)                  # n thicknesses, outer ones smaller
    mids = (radii[:-1] + radii[1:]) / 2     # midpoint of each ring along +x
    for xm, t in zip(mids, thick):
        ax.text(xm, 0, f'{t * R_new:.3f}', rotation=90, fontsize=8,
                ha='center', va='center')

    # Set axes properties here for a better view
    ## things like axis limits and tick marks
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_aspect('equal')   # circles look like circles, not ellipses
    ax.axis('off')           # spec: no axes or labels

    # Stylize and annotate
    ## things like axes labels, font sizes, or any other finishing touches
    ax.set_title('five equal amounts of paper (core at one third of the radius)')

    ######################

    # Finally, show on screen and/or save to file
    if saveas:
        plt.savefig(saveas)
    plt.close()   # figures in this course are files: look at the saved PNG (plt.show() would pop a window instead)

if __name__ == '__main__':
    visualize_danger(5, saveas='squarespare.png')