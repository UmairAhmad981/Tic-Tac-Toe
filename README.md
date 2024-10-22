# Tic-Tac-Toe Game

This is a simple Tic-Tac-Toe game built with Python. Follow the instructions below to run the game or build it as an executable.

## How to Run

To run the game, simply execute the `tic_tac_toe.py` file:

```bash
python tic_tac_toe.py
```

Make sure you have Python installed in your environment.

## How to Build as Executable

To build the Tic-Tac-Toe game as a standalone executable (.exe) file, you can use **PyInstaller**.

### Step-by-Step Guide:

1. First, make sure you have **PyInstaller** installed. You can install it using the following command:

    ```bash
    pip install pyinstaller
    ```

2. After installing PyInstaller, navigate to the project directory and run the following command to build the executable:

    ```bash
    pyinstaller --onefile --windowed --icon=tic-tac-toe_1191134.ico --add-data "tic-tac-toe_1191134.png;." tic_tac_toe.py
    ```

    - `--onefile`: Creates a single executable file.
    - `--windowed`: Ensures that no console window is opened when running the app.
    - `--icon`: Specifies the icon for the executable.
    - `--add-data`: Includes additional data files (e.g., images) that the application needs.

3. Once the build is complete, the executable file will be located in the `dist` folder.

    - `tic-tac-toe_1191134.ico`: The icon for the application.
    - `tic-tac-toe_1191134.png`: The image file used in the application.

### Additional Information:

- You can replace the provided `.ico` and `.png` files with your own, or customize them as needed.
- The `dist` folder will contain the final executable, which can be distributed or run on any Windows machine without needing Python installed.
