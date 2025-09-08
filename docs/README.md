# Documentation for DFS Channel Analysis

This folder contains documentation and troubleshooting guides for the `dfs-channel-analysis` repository.  
Each file addresses a specific topic to help users understand, troubleshoot, and extend the codebase.

## Directory Structure

```
dfs-channel-analysis/
└── docs/
    ├── matplotlib_latex_troubleshooting.md
    ├── figure_tick_customization.md
    ├── environment_setup.md
    └── usage_notes.md
```

- [`matplotlib_latex_troubleshooting.md`](matplotlib_latex_troubleshooting.md):  
  Fixes and workarounds for LaTeX and font-related errors when plotting with matplotlib and scienceplots.

- [`figure_tick_customization.md`](figure_tick_customization.md):  
  Guides on customizing tick appearance in figures, including how to edit scienceplots style files for consistent figure styling.

- [`environment_setup.md`](environment_setup.md):  
  Instructions for setting up the development environment, required dependencies, and recommended tools.

- [`usage_notes.md`](usage_notes.md):  
  Additional notes, tips, and best practices for using and extending this repository.

## How to Use

- Refer to these files whenever you encounter issues, want to reproduce figure styles, or need more information about setup and usage.
- Link to relevant documentation from your notebooks or main `README.md` for user convenience.

## Contributing

If you resolve a new issue or have tips to share, please add a new markdown file or update an existing one in this directory.  
Use clear, descriptive filenames for new documentation topics.

---

## Environment Setup

This guide helps you set up the environment for the `dfs-channel-analysis` repository.

### 1. Python Version

- Recommended: **Python 3.8+**  
- Check your version:
  ```sh
  python --version
  ```

### 2. Clone the Repository

```sh
git clone https://github.com/kwetishedanjuma/dfs-channel-analysis.git
cd dfs-channel-analysis
```

### 3. Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 4. Install Requirements

- Install core dependencies:
  ```sh
  pip install -r requirements.txt
  ```

- If there is a `requirements-dev.txt`, install with:
  ```sh
  pip install -r requirements-dev.txt
  ```

### 5. Optional: Jupyter Notebook

- If you want to run notebooks:
  ```sh
  pip install notebook
  ```

### 6. Optional: Install `scienceplots`

- For enhanced matplotlib plotting:
  ```sh
  pip install scienceplots
  ```

### 7. Optional: GIS & Earth Engine Tools

- If using `arcgis-tools` or `google-earth-engine` modules, follow the respective setup guides in their folders or docs.

### 8. Test Your Setup

- Run a sample notebook or script to confirm your environment is working.

---

**Troubleshooting:**  
If you encounter issues, check the files in `docs/` for platform-specific notes and workarounds.

---

## Usage Notes

Helpful tips and best practices for using the `dfs-channel-analysis` repository.

---

### General Recommendations

- Always activate your virtual environment before running scripts or notebooks.
- Keep your dependencies up to date. Re-run `pip install -r requirements.txt` after pulling changes.

---

### Working with Notebooks

- Open Jupyter notebooks with:
  ```sh
  jupyter notebook
  ```
- Read notebook instructions and bullet notes at the top before running code cells.
- If you encounter plotting or LaTeX errors, see the troubleshooting docs in `docs/`.

---

### Data Organization

- Place your data files in the `data/` directory.
- Update the `DATA_PATH` variable in the notebooks as needed.

---

### Results

- Output figures and analysis results are saved in the `results/` directory.
- Check for any path changes or overwrites before running batch scripts.

---

### Customizing Plots

- See [`figure_tick_customization.md`](figure_tick_customization.md) for plot style details.
- For LaTeX or font issues with matplotlib, see [`matplotlib_latex_troubleshooting.md`](matplotlib_latex_troubleshooting.md).

---

### Environment Issues

- If you have trouble installing dependencies, check for OS-specific instructions in [`environment_setup.md`](environment_setup.md).
- Always check your Python version if you see unexpected errors.

---

### Contributing

- Add new documentation to `docs/` with clear, descriptive filenames.
- Comment your code and notebooks to help others understand your process.

---
