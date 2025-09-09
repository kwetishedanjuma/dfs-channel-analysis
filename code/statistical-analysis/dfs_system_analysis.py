# DFS System Analysis
#
# Multi-scale statistical analysis of distributive fluvial systems using manual digitisation data.
#
# Instructions:
# - Change DATA_PATH below to analyze a different system file in your data/ folder.
# - All analysis steps are modular and reusable.
# - If you see LaTeX or font-related errors when plotting, see docs/matplotlib_latex_troubleshooting.md for quick fixes.

import scienceplots
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from moepy import lowess

plt.style.use(['science','ieee'])
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": "Computer Modern"
})

# ## Configurable Parameters

# Use path relative to your repository
DATA_PATH = "data/rio_fragua_chorroso_analysis_data.xlsx"  # Change for other systems
SHEETS = {
    "channel_profile": "channel_profile",
    "cross_section_scale": "cross_section_scale",
    "system_scale": "system_scale",
    "domain_scale": "domain_scale",
    "reach_scale": "reach_scale"
}

# ## Load All Standard Data Sheets

channel_profile = pd.read_excel(DATA_PATH, sheet_name=SHEETS["channel_profile"])
cross_section = pd.read_excel(DATA_PATH, sheet_name=SHEETS["cross_section_scale"])
system_scale = pd.read_excel(DATA_PATH, sheet_name=SHEETS["system_scale"])
domain_scale = pd.read_excel(DATA_PATH, sheet_name=SHEETS["domain_scale"])
reach_scale = pd.read_excel(DATA_PATH, sheet_name=SHEETS["reach_scale"])

# Display heads for QC
cross_section.head()

# ## Reusable OLS Regression Function

def ols_regression(df, y_col, x_col='segment'):
#     """
#     Run OLS regression and print summary for y_col vs x_col.
#     """
    y = df[y_col]
    x = sm.add_constant(df[x_col])
    model = sm.OLS(y, x).fit()
    print(f"OLS regression for {y_col} vs {x_col}:")
    print(model.summary())
    return model

# ## Channel Profile Analysis (LOWESS Smoothing)

x = channel_profile['distance_km'].values
y = channel_profile['elevation_m'].values
lowess_model = lowess.Lowess()
lowess_model.fit(x, y)
x_pred = np.linspace(x.min(), x.max(), 30)
y_pred = lowess_model.predict(x_pred)

plt.plot(channel_profile['distance_km'], channel_profile['elevation_m'], label='Raw Data', color='#1F77B4')
plt.plot(x_pred, y_pred, '-', label='LOWESS', color='#FF7F0E', zorder=6)
plt.xlabel("Distance ($km$)")
plt.ylabel("Elevation ($m$)")
plt.legend(frameon=True)
plt.savefig('rio_fragua_chorroso_channel_gradient.png', dpi=300)
plt.savefig('rio_fragua_chorroso_channel_gradient.svg', dpi=300)
plt.show()

# ## Slope Calculation

x1 = channel_profile['distance_km'][0]*1000
y1 = channel_profile['elevation_m'][0]
xLast = channel_profile['distance_km'].iloc[-1]*1000
yLast = channel_profile['elevation_m'].iloc[-1]
slope = (yLast-y1)/(xLast-x1)
print('Slope:', slope, '| Abs Slope:', abs(slope))

# ## Scatter Plot: Channel Belt vs Wetted Channel

# Scatter Plot: Channel Belt vs Wetted Channel
# To plot Dry Riverbed instead of Wetted Channel, substitute 'wettedChannel' with 'dryRiverbed' below.
a, b = np.polyfit(cross_section['segment'], cross_section['channelBelt'], 1)
c, d = np.polyfit(cross_section['segment'], cross_section['wettedChannel'], 1)

with plt.style.context(['science', 'nature']):
    plt.scatter(cross_section['segment'], cross_section['channelBelt'], color='#000000', label='Channel Belt')
    plt.scatter(cross_section['segment'], cross_section['wettedChannel'], color='#1F77B4', label='Wetted Channel')
    
    plt.plot(cross_section['segment'], a*cross_section['segment']+b, color='#dc0500ff', label='Channel Belt Fit')
    plt.plot(cross_section['segment'], c*cross_section['segment']+d, color='#FF7F0E', label='Wetted Channel Fit')

    plt.xlabel("% total distance")
    plt.ylabel("width ($km$)")
    plt.margins(0.05, 0.2)    
    plt.legend(frameon=True)
    plt.tight_layout()
    plt.savefig('rio_fragua_chorroso_cross_section_scatter_channelBelt_vs_wettedChannel.png', dpi=300)
    plt.savefig('rio_fragua_chorroso_cross_section_scatter_channelBelt_vs_wettedChannel.svg', dpi=300)
    plt.show()

# ## Stack Plot: Wetted Channel vs Unvegetated Bar vs Vegetated Bar

# Stack Plot: Wetted Channel vs Unvegetated Bar vs Vegetated Bar using cross_section DataFrame
# For reach-scale, use reach_scale DataFrame and update ylabel to "Area ($km^2$)" if columns represent area.
cross_section.plot(
    x="segment",
    y=['wettedChannel', 'unvegetatedBar', 'vegetatedBar'],
    kind="bar",
    stacked=True,
    color=['#4477aa', '#ccbb44', '#009988'],
)

plt.ylabel("Width ($km$)")
# For reach-scale: plt.ylabel("Area ($km^2$)")
plt.xlabel("% total distance")
plt.margins(0.05, 0.19)
plt.legend(['Wetted Channel', 'Unvegetated Bar', 'Vegetated Bar'], frameon=True)
plt.tight_layout()
plt.savefig('rio_fragua_chorroso_cross_section_stack_wettedChannel_vs_unvegetatedBar_vs_vegetatedBar.png', dpi=300)
plt.savefig('rio_fragua_chorroso_cross_section_stack_wettedChannel_vs_unvegetatedBar_vs_vegetatedBar.svg', dpi=300)
plt.show()

# ## Stack Plot (Normalised): Wetted Channel vs Unvegetated Bar vs Vegetated Bar

# Stack Plot (Normalised): Wetted Channel vs Unvegetated Bar vs Vegetated Bar
# This version normalises the widths per segment to percentage (row-wise).
# Make a copy of the original DataFrame (replace 'cross_section' with your DataFrame if needed)
# For reach-scale, use reach_scale DataFrame and update ylabel to "Area normalised ($\\%$)" if columns represent area.
cross_section_2 = cross_section.copy()

# Convert row values to percentages (row-wise normalisation)
cols = ['wettedChannel', 'unvegetatedBar', 'vegetatedBar']
cross_section_2[cols] = cross_section_2[cols].apply(lambda x: x/x.sum(), axis=1).multiply(100)

# Stack plot
cross_section_2.plot(
    x="segment",
    y=cols,
    kind="bar",
    stacked=True,
    color=['#4477aa', '#ccbb44', '#009988'],
)

plt.ylabel("Width normalised ($\\%$)")
# For reach-scale: plt.ylabel("Area normalised ($\\%$)")
plt.xlabel("% total distance")
plt.legend(['Wetted Channel', 'Unvegetated Bar', 'Vegetated Bar'], frameon=True)
plt.tight_layout()
plt.savefig('rio_fragua_chorroso_cross_section_stack_normalised_wettedChannel_vs_unvegetatedBar_vs_vegetatedBar.png', dpi=300)
plt.savefig('rio_fragua_chorroso_cross_section_stack_normalised_wettedChannel_vs_unvegetatedBar_vs_vegetatedBar.svg', dpi=300)
plt.show()

# ## System-scale Pie Chart

# System-scale pie chart of total system area by class/category
# Loads data from 'manualSystemWide' sheet in 'colombia06RiverData.xlsx'

# Create pie chart using 'environment' and 'area'
ax = system_scale.plot.pie(
    y='area',
    labels=system_scale['environment'],
    legend=False,
    autopct="%1.1f%%",
    explode=[0.0] * len(system_scale),  # Adjust if you want to highlight any slice
    shadow=False,
    startangle=90,
    colors=['#4477aa', '#ccbb44', '#009988'][:len(system_scale)]
)

plt.ylabel("")  # Remove default ylabel
plt.axis('equal')
plt.tight_layout()
plt.savefig('system_scale_pie_environment_vs_area.png', dpi=300)
plt.savefig('system_scale_pie_environment_vs_area.svg', dpi=300)
plt.show()

# ## Domain-scale Stacked Bar Plot

# Domain-scale stacked bar plot: Proximal, Medial, Distal zones
# Loads area data for water, sediment, and vegetation from the domain_scale sheet
# Load proximal-medial-distal (domain scale) dataset

# Create stacked bar plot for domain scale
ax = domain_scale.plot(
    x="zone",
    y=['wettedChannel', 'unvegetatedBar', 'vegetatedBar'],
    kind="bar",
    stacked=True,
    color=['#4477aa', '#ccbb44', '#009988']
)

plt.xlabel("")
plt.xticks(rotation=0)
plt.ylabel("Area ($km^2$)")
plt.margins(0.05, 0.08)
plt.legend(['Wetted Channel', 'Unvegetated Bar', 'Vegetated Bar'], frameon=True)
plt.tight_layout()
plt.savefig('domain_scale_stack_waterArea_vs_sedimentArea_vs_vegetationArea.png', dpi=300)
plt.savefig('domain_scale_stack_waterArea_vs_sedimentArea_vs_vegetationArea.svg', dpi=300)
plt.show()

# ## Domain-scale Stacked Bar Plot (Normalised)

# Domain-scale stacked bar plot (normalised): Proximal, Medial, Distal zones
# Each zone's area composition is normalised to percentage (row-wise)
# Load proximal-medial-distal (domain scale) dataset

# Convert area columns to percentages (row-wise normalisation)
cols = ['wettedChannel', 'unvegetatedBar', 'vegetatedBar']
domain_scale_percent = domain_scale.copy()
domain_scale_percent[cols] = domain_scale_percent[cols].apply(lambda x: x/x.sum(), axis=1).multiply(100)

# Create stacked bar plot (normalised)
ax = domain_scale_percent.plot(
    x="zone",
    y=cols,
    kind="bar",
    stacked=True,
    color=['#4477aa', '#ccbb44', '#009988']
)

plt.xlabel("")
plt.xticks(rotation=0)
plt.ylabel("Area normalised ($\\%$)")
plt.legend(['Wetted Channel', 'Unvegetated Bar', 'Vegetated Bar'], frameon=True)
plt.tight_layout()
plt.savefig('domain_scale_stack_normalised_waterArea_vs_sedimentArea_vs_vegetationArea.png', dpi=300)
plt.savefig('domain_scale_stack_normalised_waterArea_vs_sedimentArea_vs_vegetationArea.svg', dpi=300)
plt.show()

# ## OLS Regression for All Environment Types (Cross-section)

# For dryland systems (e.g. Iran) include 'dryRiverbed' in environment columns
env_cols = ['channelBelt', 'wettedChannel', 'barComplex', 'unvegetatedBar', 'vegetatedBar']
for col in env_cols:
    if col in cross_section.columns:
        ols_regression(cross_section, col)