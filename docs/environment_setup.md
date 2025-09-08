# Environment Setup

This guide helps you set up the environment for the `dfs-channel-analysis` repository.

## 1. Python Version

- Recommended: **Python 3.8+**  
- Check your version:
  ```sh
  python --version
  ```

## 2. Clone the Repository

```sh
git clone https://github.com/kwetishedanjuma/dfs-channel-analysis.git
cd dfs-channel-analysis
```

## 3. Create a Virtual Environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

## 4. Install Requirements

- Install core dependencies:
  ```sh
  pip install -r requirements.txt
  ```

- If there is a `requirements-dev.txt`, install with:
  ```sh
  pip install -r requirements-dev.txt
  ```

## 5. Optional: Jupyter Notebook

- If you want to run notebooks:
  ```sh
  pip install notebook
  ```

## 6. Optional: Install `scienceplots`

- For enhanced matplotlib plotting:
  ```sh
  pip install scienceplots
  ```

## 7. Optional: GIS & Earth Engine Tools

- If using `arcgis-tools` or `google-earth-engine` modules, follow the respective setup guides in their folders or docs.

## 8. Test Your Setup

- Run a sample notebook or script to confirm your environment is working.

---

**Troubleshooting:**  
If you encounter issues, check the files in `docs/` for platform-specific notes and workarounds.
