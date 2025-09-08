# Matplotlib + LaTeX (MiKTeX) Troubleshooting

If you encounter LaTeX errors with matplotlib (e.g., `LaTeX Error: Command \jmath already defined.`), especially when using `scienceplots` with the `'science'` or `'ieee'` style, follow these steps:

---

## 1. Update MiKTeX

- Open **MiKTeX Console** (as Administrator).
- Go to the **Updates** tab.
- Click **Check for updates** and install all updates.

---

## 2. Avoid Conflicting Packages

- The error usually comes from a conflict in the `sfmath.sty` package, loaded by `'science'` or `'ieee'` styles in `scienceplots`.
- **Recommendation:** Unless you need full LaTeX, use Matplotlib’s built-in mathtext:
    ```python
    import matplotlib as mpl
    mpl.rcParams['text.usetex'] = False
    ```
    Or, just use plain labels in your plotting code (e.g., `Width (km)`) instead of LaTeX math labels (`Width ($km$)`).

---

## 3. Use Compatible Fonts (If you need LaTeX rendering)

- Use a basic font setup:
    ```python
    import matplotlib.pyplot as plt
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.serif": "Computer Modern"
    })
    ```
- Avoid using `Helvetica`, `Times`, or `sfmath` unless you are sure the packages are installed and not conflicting.

---

## 4. Test LaTeX Rendering

Try this minimal example to check if LaTeX works:

```python
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
plt.title(r"$\\alpha_i > \\beta_i$")
plt.show()
```

If this fails, the issue is with your LaTeX installation or configuration.

---

## 5. For Jupyter Notebooks

- Keep your plotting code simple and portable. Use plain text labels if you don’t need LaTeX, e.g.:

    ```python
    plt.ylabel('Width (km)')
    ```

- If you want to remind users, add a markdown cell at the top of your notebook:

    ```
    > **Note:** If you see LaTeX or font-related errors when plotting, see `docs/matplotlib_latex_troubleshooting.md` for quick fixes.
    ```

---

## Example: Channel Belt vs Wetted Channel Plot

```python
# Scatter Plot: Channel Belt vs Wetted Channel
# To plot Dry Riverbed instead of Wetted Channel, substitute 'wettedChannel' with 'dryRiverbed' below.
a, b = np.polyfit(cross_section['segment'], cross_section['channelBelt'], 1)
c, d = np.polyfit(cross_section['segment'], cross_section['wettedChannel'], 1)

with plt.style.context(['science', 'nature']):
    plt.scatter(cross_section['segment'], cross_section['channelBelt'], color='#000000', label='Channel Belt')
    plt.scatter(cross_section['segment'], cross_section['wettedChannel'], color='#1F77B4', label='Wetted Channel')
    plt.plot(cross_section['segment'], a*cross_section['segment']+b, color='#dc0500ff', label='Channel Belt Fit')
    plt.plot(cross_section['segment'], c*cross_section['segment']+d, color='#FF7F0E', label='Wetted Channel Fit')
    plt.xlabel('% total distance')
    plt.ylabel('Width (km)')
    plt.legend(frameon=True)
    plt.margins(0.05, 0.2)
    plt.tight_layout()
    plt.show()
```

---

**Tip:** For most scientific plots, using mathtext (the default) is sufficient and avoids most font/package issues.
