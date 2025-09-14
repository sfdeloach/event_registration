Setting up a Python virtual environment on your Arch Linux machine is straightforward and helps isolate your development projects' dependencies. Below is a step-by-step guide to create, activate, use, and manage a Python virtual environment.

### Step 1: Ensure Python and Required Tools are Installed

Arch Linux typically comes with Python, but confirm it's installed, along with the `venv` module.

- Check Python version:

  ```
  python --version
  ```

  (Arch uses `python` for Python 3.x, e.g., 3.12.3 as of your current date, September 14, 2025.)

- Ensure `python-venv` is installed (included with the base `python` package in Arch):
  ```
  pacman -Qs python
  ```
  Look for `local/python`. If missing, install it:
  ```
  sudo pacman -S python
  ```

### Step 2: Create a Virtual Environment

1. **Navigate to your project directory** (or create one):

   ```
   mkdir myproject
   cd myproject
   ```

2. **Create the virtual environment**:
   Use the `venv` module to create an isolated environment. Replace `venv` with any name you prefer for the environment folder.
   ```
   python -m venv venv
   ```
   This creates a `venv` directory in `myproject/` containing the isolated Python environment.

### Step 3: Activate the Virtual Environment

To use the virtual environment, activate it. This changes your shell's `PATH` to use the isolated Python and `pip`.

- **Activate on Arch Linux (bash/zsh)**:

  ```
  source venv/bin/activate
  ```

  Your prompt should change (e.g., `(venv) user@machine:~/myproject$`).

- **Verify you're in the virtual environment**:
  ```
  which python
  ```
  Should point to `~/myproject/venv/bin/python`.
  ```
  python --version
  ```
  Should match your system's Python version.
  ```
  pip list
  ```
  Should show only minimal packages (`pip`, `setuptools`).

### Step 4: Install Packages in the Virtual Environment

With the environment activated, use `pip` to install packages. These will be isolated to the `venv` directory, not affecting your system.

- Example: Install Django and NumPy:

  ```
  pip install django numpy
  ```

- Check installed packages:

  ```
  pip list
  ```

- Save dependencies to a file (optional, for reproducibility):
  ```
  pip freeze > requirements.txt
  ```
  Later, you can reinstall them with `pip install -r requirements.txt`.

### Step 5: Deactivate the Virtual Environment

When done, exit the virtual environment:

```
deactivate
```

Your prompt returns to normal, and `which python` points back to the system Python (`/usr/bin/python`).

### Step 6: Managing Virtual Environments

- **Delete an environment**: Simply delete the `venv` folder:
  ```
  rm -rf venv
  ```
- **Create multiple environments**: Repeat the process in different project folders with unique names (e.g., `venv`, `env`, `myenv`).
- **Re-activate later**: Just run `source venv/bin/activate` from the project directory.

### Tips for Arch Linux Users

- **Avoid global `pip` installs**: Always activate a virtual environment before using `pip` to avoid conflicts with pacman-managed packages (e.g., `python-django`).
- **Use an AUR helper for Python tools**: If you need tools like `poetry` or `virtualenvwrapper` from the AUR, install them with `yay -S python-poetry` or similar.
- **Check for system conflicts**: If you kept packages like `python-django` via pacman, avoid installing the same package via `pip` in the virtual environment to prevent version mismatches.
- **Update pip in the virtual environment** (optional):
  ```
  pip install --upgrade pip
  ```

### Example Workflow

1. Create and activate:
   ```
   mkdir myproject && cd myproject
   python -m venv venv
   source venv/bin/activate
   ```
2. Install packages:
   ```
   pip install django numpy
   ```
3. Work on your project, then deactivate:
   ```
   deactivate
   ```

If you run into issues (e.g., permission errors or missing `venv`), share the error output, and I can help troubleshoot!
