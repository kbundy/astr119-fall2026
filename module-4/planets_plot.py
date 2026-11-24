# planets_plot_starter.py -- the ten planets as arrays, ready to plot (Pod 6). Copy this file to planets_plot.py and work on the copy.
# Run from the repository folder:  python module-4/planets_plot.py
import numpy as np
import matplotlib.pyplot as plt

SIGMA = 5.67e-8          # Stefan-Boltzmann constant, W m^-2 K^-4
L_SUN = 3.8e26           # solar luminosity, W
AU = 1.496e11            # meters per AU
L_HSUN = L_SUN / 2       # half the solar luminosity

name = np.array(["Earth", "Mars", "HD 209458 b", "51 Peg b", "TRAPPIST-1 e",
                 "Kepler-22 b", "55 Cnc e", "HD 189733 b", "Kepler-452 b", "Proxima b"])
lum = np.array([1.0, 1.0, 1.6, 1.3, 0.00055, 0.79, 0.58, 0.34, 1.2, 0.0016])        # star luminosity, solar units
dist = np.array([1.000, 1.524, 0.047, 0.052, 0.029, 0.85, 0.0154, 0.031, 1.046, 0.0485])   # distance, AU


def t_eq(L, d):
    """Equilibrium temperature (K) at distance d (m) from a star of luminosity L (W)."""
    return (L / (16 * np.pi * SIGMA * d**2)) ** 0.25

if __name__ == "__main__":
    T = t_eq(lum * L_SUN, dist * AU) # calculate the equilibrium temperatures for each planet

    d = np.linspace(0.01, 10, 100) # create a range of distances for the curve
    T_curve = t_eq(L_SUN, d * AU) # calculate the equilibrium temperature curve for a solar-luminosity star

    fig, ax = plt.subplots()

    ax.scatter(dist, T) # plot the equilibrium temperatures of the planets at their respective distances
    ax.plot(d, T_curve) # plot the equilibrium temperature curve for a solar-luminosity star

    ax.set_xscale("log") # use a logarithmic scale for the x-axis
    ax.set_yscale("log") # use a logarithmic scale for the y-axis

    for n, x, y in zip(name, dist, T):

        # I tried to change the labels so they wouldn't overlap, but I couldn't figure it out in time.

        ax.annotate(n, (x, y), fontsize=7) # assign names to data points from the name array

    ax.set_xlabel("Distance from star (AU)") # label the x-axis
    ax.set_ylabel("Equilibrium temperature (K)") # label the y-axis
    ax.set_title("Equilibrium Temperatures of Planets vs Distance from Star")
    
    fig.savefig("module-4/planets.png", dpi=150) # save the plot to a file
    print("wrote module-4/planets.png") # print a message when the file is saved
