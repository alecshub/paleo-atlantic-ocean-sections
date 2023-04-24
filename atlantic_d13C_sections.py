# This program reads in and combines two sediment core stable isotope databases. 
# Then it automates some data cleaning and wrangling to filter for the desired geographic location of sediment cores, splice the data set by specified Marine Isotope Stage (MIS) age ranges, calculate a mean stable isotope value for each sediment core within a given MIS, and return a finalized MultiIndex data set.
# Lastly, the program develops a detailed figure, showing stable isotope values throughout the Atlantic ocean for each MIS.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import seaborn as sns
import matplotlib.cm as cm
import matplotlib.colors as mcolors

# Read in Oliver sediment core database.
df = pd.read_csv("Oliver2010_core_database.csv", names=["name", "Latitude", "longitude", "Depth", "depthincore", "age", "species", "d18O", "d13C"], skiprows=[0])

# Read in supplementary sediment core database.
df2 = pd.read_csv("additional_core_database.csv",names=["name", "Latitude", "longitude", "Depth", "depthincore", "age", "species", "d18O", "d13C"], skiprows=[0])

# Merge both dataframes together.
df = pd.concat([df, df2], axis=0)

# Convert any hidden strings in stable isotope data columns to NaN values.
df['d13C'] = pd.to_numeric(df['d13C'], errors='coerce')
df['d18O'] = pd.to_numeric(df['d18O'], errors='coerce')

# Filter for longitude (we only want data for the Atlantic Ocean).
df = df[(df['longitude'] >= -70) & (df['longitude'] <= 15)]

# Create new column of NaNs that we will assign Marine Isotope Stage (MIS) names to.
df["MIS"] = np.nan

# Define MIS age ranges.
MIS_age_ranges = {
    'MIS1': [0, 5],
    'MIS2': [19, 24],
    'MIS4': [61, 66],
    # 'MIS5a': [70, 87],
    'MIS5d': [108, 114],
    'MIS5e': [120, 130],
    'MIS6':[137, 142],
    }

# Filter dataframe for each MIS age range and assign MIS name to each slice.
for MIS_name, age_ranges in MIS_age_ranges.items():
    for age_range in age_ranges:
        df.loc[(df['age'] >= age_ranges[0]) & (df['age'] <= age_ranges[1]),'MIS'] = MIS_name

# Remove data rows with ages outside of specified MIS age ranges.
df = df.dropna(subset=['MIS'])

# Construct MultiIndex from dataframe by setting index columns and then sorting on those indexes.
df = df.set_index(['MIS','name']).sort_index()

# For a given MIS, drop all cores that have 2 or less data points.
    # Start by dropping all rows that have NaNs in the d13C column.
df = df.dropna(subset=['d13C'])

    # Then, filter for greater than 2 appearances of a core name in the 'name' column.
df = df.groupby(['MIS','name']).filter(lambda x: len(x) > 2)

# For a given MIS, find the average isotope value for each separate sediment core.
df = df.groupby(level=['MIS', 'name']).mean()

# Remove extraneous columns.
df = df.drop(columns=['depthincore', 'age', 'd18O'])

# Round columns to desired decimal places.
df = df.round({'Latitude': 2, 'longitude':2, 'Depth':0, 'd13C':2})


# Plotting:

# Create list of MIS names in the intended plotting order.
mis_names = ["MIS1","MIS2","MIS5e","MIS6","MIS5d","MIS4"]
fig, axes = plt.subplots(3, 2, sharex=True, sharey=True)
for mis, ax in zip(mis_names, axes.flatten()):

    # Define data variables.
    x=df.loc[mis]['Latitude']
    y=df.loc[mis]['Depth']
    c=df.loc[mis]['d13C']

    # Define color map and color bar attributes.
    vcenter = 0.3
    vmin, vmax = -0.5, 1.5
    normalize = mcolors.TwoSlopeNorm(vcenter=vcenter, vmin=vmin, vmax=vmax)
    colormap = cm.seismic

    # Plot using seaborn.
    s=sns.scatterplot(
        y=y,
        x=x,
        c=c,
        norm=normalize,
        cmap=colormap,
        ax=ax,
        edgecolor="black"
    )

    # Add MIS title label inside of plot.
    trans = mtransforms.ScaledTranslation(10/72, -5/72, fig.dpi_scale_trans)
    ax.text(0.0, 1.0, mis, transform=ax.transAxes + trans,
            fontsize='medium', verticalalignment='top', fontfamily='serif')

    # Remove automatic axis labels.
    ax.set(xlabel=None)
    ax.set(ylabel=None)

# Invert y axis.
plt.gca().invert_yaxis()
# Adjust white space.
fig.subplots_adjust(wspace=0.05, hspace=0.1)
# Set x and y axis ranges and intervals.
plt.xticks(np.arange(-40, 80, 20))
plt.yticks(np.arange(0, 6000, 1000))
# Set x axis limit.
plt.xlim([-60, 80])
# Add secondary y axis.
for i in range(3):
    axes[i,1].secondary_yaxis('right').set_yticks(np.arange(0, 6000, 1000))
# Add secondary x axis.
for i in range(2):
    axes[0,i].secondary_xaxis('top').set_xticks(np.arange(-40, 80, 20))

# Add colorbar.
scalarmappaple = cm.ScalarMappable(norm=normalize, cmap=colormap)
scalarmappaple.set_array(y)
cb = fig.colorbar(scalarmappaple, ax=axes.ravel().tolist(), pad=0.08)
    # Set color bar label. Need to use unicode to write d13C permil.
cb.set_label('$\u03B4^{13}C$ \u2030', rotation=-90)
cb.ax.set_yscale('linear')

# Add common labels for all axes.
fig.text(0.425, 0.05, 'Latitude', ha='center')
fig.text(0.07, 0.5, 'Depth (m)', va='center', rotation='vertical')

plt.show()