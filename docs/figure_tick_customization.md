
## Customizing Tick Appearance in Figures

To achieve consistent figure appearance (ticks out, keep minor ticks, remove major ticks, remove x-top and y-right ticks):

- Set ticks to point outward.
- Keep minor ticks visible.
- Remove major ticks if not needed.
- Remove top ticks on the x-axis and right ticks on the y-axis.

**Example code:**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
# ... your plotting code ...

# Ticks out
ax.tick_params(direction='out')
# Show minor ticks
ax.minorticks_on()
# Remove top and right ticks
ax.tick_params(top=False, right=False)
# Optionally, remove major ticks
ax.tick_params(which='major', length=0)
```

---

## Editing scienceplots Style File

If you want these settings to be the default when using `scienceplots`, you can edit the relevant `.mplstyle` file:

### How to Locate `scienceplots` Styles

1. **Find the installed package location:**

   - In a Python terminal, run:
     ```python
     import scienceplots
     print(scienceplots.__file__)
     ```
   - This will show the path to the `scienceplots` package directory.

2. **Navigate to the `styles` folder:**
   - Inside the package directory, find the `styles` folder.
   - The style files (e.g., `science.mplstyle`, `ieee.mplstyle`) are located here.

3. **Edit the desired `.mplstyle` file:**
   - Open the file (e.g., `science.mplstyle`) in a text editor.
   - Add or modify tick-related lines. For example:
     ```
     axes.tickdirection : out
     xtick.top : False
     ytick.right : False
     xtick.minor.visible : True
     ytick.minor.visible : True
     xtick.major.size : 0
     ytick.major.size : 0
     ```
   - Save the file.

### Platform Notes

- **Windows:** The path will look something like  
  `C:\Users\<YourUser>\AppData\Local\Programs\Python\Python3x\Lib\site-packages\scienceplots\styles\`
- **macOS/iOS:** The path will look something like  
  `/Users/<YourUser>/opt/anaconda3/lib/python3.x/site-packages/scienceplots/styles/`  
  or  
  `/Library/Frameworks/Python.framework/Versions/3.x/lib/python3.x/site-packages/scienceplots/styles/`

---

**Now, `with plt.style.context(['science', ...])` will use your customized tick settings by default.**
