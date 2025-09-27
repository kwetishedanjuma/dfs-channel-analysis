# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set plotting font to Times New Roman (serif)
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

def main():
    # Define data path (relative to repo root)
    data_path = "hartley_et_al_modern_dfs.xlsx"

    # Load dataset and clean column names
    modern_dfs = pd.read_excel(data_path)
    modern_dfs.columns = modern_dfs.columns.str.lower().str.replace(' ', '_')
    print(modern_dfs.head())

    # Subset relevant columns
    subset_cols = ['tectonic_setting', 'apex-toe_dist_(km)', 'climate_basin']
    modern_dfs_subset = modern_dfs[subset_cols]

    # Save subset for further analysis
    modern_dfs_subset.to_excel('modern_dfs_subset.xlsx', sheet_name='modern_dfs_subset', index=False)

    # If using a manually filtered file, load it here
    # modern_dfs_subset = pd.read_excel('modern_dfs_filter.xlsx')
    # print(modern_dfs_subset.head())

    # Histogram by tectonic setting
    tectonic_types = ['compressional', 'cratonic', 'extensional', 'foreland', 'strike-slip']
    data_tectonic_setting = [
        modern_dfs_subset.loc[modern_dfs_subset['tectonic_setting'] == t, 'apex-toe_dist_(km)']
        for t in tectonic_types
    ]
    colors = ['#004488', '#228833', '#CC3311', '#AA4499', '#EE7733']
    bins_main = np.arange(30, 711, 20)

    plt.figure(figsize=(6.4, 4.8), dpi=300)
    plt.hist(data_tectonic_setting, bins=bins_main, stacked=True, rwidth=0.9, align='left', color=colors, edgecolor="black")
    plt.legend([t.title() for t in tectonic_types])
    plt.xticks(bins_main, rotation='vertical')
    plt.ylabel('Frequency distribution')
    plt.xlabel('Apex-toe distance (km)')
    plt.title('Modern DFS distribution across tectonic settings')
    plt.savefig('figures/tectonic_setting_main_figure.svg', bbox_inches='tight', facecolor='w')
    plt.show()

    # Histogram by climate basin
    climate_types = ['continental', 'drylands', 'polar', 'subtropical', 'tropical']
    data_climate_basins = [
        modern_dfs_subset.loc[modern_dfs_subset['climate_basin'] == c, 'apex-toe_dist_(km)']
        for c in climate_types
    ]

    plt.figure(figsize=(6.4, 4.8), dpi=300)
    plt.hist(data_climate_basins, bins=bins_main, stacked=True, rwidth=0.9, align='left', color=colors, edgecolor='black')
    plt.legend([c.title() for c in climate_types])
    plt.xticks(bins_main, rotation='vertical')
    plt.ylabel('Frequency distribution')
    plt.xlabel('Apex-toe distance (km)')
    plt.title('Modern DFS distribution across climate basins')
    plt.savefig('figures/climate_basin_main_figure.svg', bbox_inches='tight', facecolor='w')
    plt.show()

    # Zoomed-in histogram for climate basins
    bins_zoomed = np.arange(30, 101, 5)
    plt.figure(figsize=(6.4, 4.8), dpi=300)
    plt.hist(data_climate_basins, bins=bins_zoomed, stacked=True, rwidth=0.9, align='left', color=colors, edgecolor='black')
    plt.legend([c.title() for c in climate_types])
    plt.xticks(bins_zoomed)
    plt.ylabel('Frequency distribution')
    plt.xlabel('Apex-toe distance (km)')
    plt.title('Modern DFS (Zoomed) across climate basins')
    plt.savefig('figures/climate_basin_zoomed_in_figure.svg', bbox_inches='tight', facecolor='w')
    plt.show()
    # --- To adapt for tectonic setting zoomed-in version: ---
    # Change 'data_climate_basins' to your tectonic data variable (e.g., data_tectonic_settings)
    # Change 'climate_types' to your tectonic types list (e.g., tectonic_types)
    # Update title/labels and output filename to reflect tectonic setting, e.g.:
    # plt.title('Modern DFS (Zoomed) across tectonic settings')
    # plt.savefig('figures/tectonic_setting_zoomed_in_figure.svg', ...)
if __name__ == "__main__":
    main()
