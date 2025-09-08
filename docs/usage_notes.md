# Usage Notes

Helpful tips and best practices for using the `dfs-channel-analysis` repository.

---

## General Recommendations

- Always activate your virtual environment before running scripts or notebooks.
- Keep your dependencies up to date. Re-run `pip install -r requirements.txt` after pulling changes.

---

## Working with Notebooks

- Open Jupyter notebooks with:
  ```sh
  jupyter notebook
  ```
- Read notebook instructions and bullet notes at the top before running code cells.
- If you encounter plotting or LaTeX errors, see the troubleshooting docs in `docs/`.

---

## Data Organization

- Place your data files in the `data/` directory.
- Update the `DATA_PATH` variable in the notebooks as needed.

---

## Results

- Output figures and analysis results are saved in the `results/` directory.
- Check for any path changes or overwrites before running batch scripts.

---

## Customizing Plots

- See [`figure_tick_customization.md`](figure_tick_customization.md) for plot style details.
- For LaTeX or font issues with matplotlib, see [`matplotlib_latex_troubleshooting.md`](matplotlib_latex_troubleshooting.md).

---

## Environment Issues

- If you have trouble installing dependencies, check for OS-specific instructions in [`environment_setup.md`](environment_setup.md).
- Always check your Python version if you see unexpected errors.

---

## Contributing

- Add new documentation to `docs/` with clear, descriptive filenames.
- Comment your code and notebooks to help others understand your process.

---
