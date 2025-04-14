# pyTicTacToe

### <div align="center"> <img src="./assets/iconProject.png" alt="Tic-Tac-Toe" width="65"> </div>

#### <p align="center">A classic Tic-Tac-Toe game with a graphical interface, built in Python using Pygame. </p>

## Demo

<div align="center">
  <img src="./assets/Animation.gif" alt="Demo of My Program" width="400">
</div>

## Features

- 🎮 Classic 3x3 Tic-Tac-Toe gameplay
- 🖥️ Clean graphical interface
- ✅ Win/draw detection
- ⚡ Quick animations
- 🖱️ Mouse-click controls
- 🌍 Windows and Linux support

## Installation

### Option 1: Download Pre-built Binary (Easiest)

1. Download the appropriate archive for your OS from the latest release
2. Extract the archive
3. Run the executable (`TicTacToe.exe` on Windows)

### Option 2: Run from Source

#### Prerequisites
- Python 3.8 or higher
- pip package manager

#### Steps
1. Open your prefered shell in a terminal emulator
2. Clone or download the repository
3. Navigate to the project directory:
```bash
cd path/to/pyTicTacToe
```

4. Install dependencies:
```bash
pip install -r src/requirements.txt
```

* If You're On linux And You're Having A Problem Installing Dependencies Use This:
 1. Install virtualenv (replace "bash" with your shell and "apt" with your package manager):
    ```bash
    sudo apt install pipx
    pipx install virtualenv
    pipx ensurepath
    bash
    ```
 2. Make a virtual environment:
    ```bash
    virtualenv venv
    ```
 3. Run the virtual environment:
    ```bash
    source venv/bin/activate
    ```
 4. Install dependencies:
    ```bash
    pip install -r src/requirements.txt
    ```

5. Run the game:
```bash
python src/main.py
```
* If You Used Virtualenv:
 - Clean up virtual environment:
    ```bash
    deactivate
    rm -rf venv
    exit
    ```


### Option 3: Build Your Own Binary Using Pyinstaller

#### Prerequisites
- Python 3.8 or higher
- pip package manager
- pipx package manager

#### Steps
1. Open your prefered shell in a terminal emulator
2. Clone or download the repository
3. Navigate to the source directory:
```bash
cd path/to/pyTicTacToe/src
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

* If You're On linux And You're Having A Problem Installing Dependencies Use This:
 1. Install virtualenv (replace "bash" with your shell and "apt" with your package manager):
    ```bash
    sudo apt install pipx
    pipx install virtualenv
    pipx ensurepath
    bash
    ```
 2. Make a virtual environment:
    ```bash
    virtualenv venv
    ```
 3. Run the virtual environment:
    ```bash
    source venv/bin/activate
    ```
 4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Build the executable:
```bash
pyinstaller ../TicTacToe.spec
```

* If You Used Virtualenv:
 - Clean up virtual environment:
    ```bash
    deactivate
    rm -rf venv
    exit
    ```

* The Binary Will Be in "CURRENTPATH/dist/"

## How to Play

Player 1 is X, Player 2 is O

Click on any empty square to place your mark

First player to get 3 marks in a row (horizontally, vertically, or diagonally) wins

The game automatically detects wins and draws

Click replay to restart after a game ends

## Project Structure

<pre>
pyTicTacToe/
├── src/                         # Source code
│   ├── main.py                  # Main game logic
│   ├── requirements.txt         # dependencies
│   └── run.bat
├── assets/
│   ├── iconProject.ai 
│   ├── iconProject.png 
│   ├── iconProject.ico          # application icon
│   └── Animation.gif
├── dist/                        # Pre-built binaries
│   ├── TicTacToeLinuxAndMac.tar.gz
│   └── TicTacToeWin.zip
├── .gitignore
├── .gitattributes
├── TicTacToe.spec               # spec file
├── README.md                    # This file
└── LICENSE                      # License file
</pre>

## Development

1. To contribute or modify:

        Fork the repository

        Install development requirements

        Make your changes

        Submit a pull request

## License

MIT License

To use this:
1. Create a new file named `README.md` in your project's root directory
2. Copy ALL of the above text (from `# pyTicTacToe` to the end)
3. Paste it into your new file
4. Save the file
