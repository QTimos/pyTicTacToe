# pyTicTacToe
<div align="center">
  <img src="./assets/iconProject.png" alt="Tic-Tac-Toe" width="200">
</div>

A classic Tic-Tac-Toe game with a graphical interface, built in Python using Pygame. Created as part of the Cerberus coding challenge.

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
- 🌍 Cross-platform support

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
1. Clone or download the repository
2. Navigate to the project directory:
if you're on windows:
```bash
cd path/to/pyTicTacToe
```

if you're on linux or mac:
```bash
cd path/to/pyTicTacToe
```

3. Install dependencies:
```bash
pip install -r src/requirements.txt
```

or:
```bash
pip install pygame
```

3. Run the game:
```bash
python src/main.py
```

### Option 3: Build Your Own Binary

1. Navigate to the source directory:
if you're on windows:
```bash
cd path/to/pyTicTacToe/src
```

if you're on linux or mac:
```bash
cd path/to/pyTicTacToe/src
```

2. Install PyInstaller:
```bash
pip install pyinstaller
```

3. Build the executable:
```bash
pyinstaller ../TicTacToe.spec
```

## How to Play

Player 1 is X, Player 2 is O

Click on any empty square to place your mark

First player to get 3 marks in a row (horizontally, vertically, or diagonally) wins

The game automatically detects wins and draws

Click replay to restart after a game ends

## Project Structure

pyTicTacToe/
├── src/                         # Source code
│   ├── main.py                  # Main game logic
│   ├── requirements.txt         # dependencies
│   ├── run.bat                  
├── build/
│   └── TicTacToe/               # pyinstaller build files
├── assets/
│   ├── iconProject.ai 
│   ├── iconProject.png 
│   ├── iconProject.ico          # application icon
│   └── Animation.gif
├── dist/                        # Pre-built binaries
│   ├── TicTacToeLinux.tar.gz
│   └── TicTacToeWin.zip
├── .gitattributes                
├── TicTacToe.spec               # spec file
├── README.md                    # This file
└── LICENSE                      # License file

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

The formatting will automatically work when viewed on GitHub or other Markdown-supported platforms. Remember to:
- Add a real screenshot file to your assets folder
- Create a LICENSE file if you're using the MIT license
- Update any paths if your project structure is different
