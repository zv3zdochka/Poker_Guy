# Poker Card Recognition Tool

Welcome to the Poker Card Recognition project repository! This project is designed to automatically recognize and classify cards displayed in a poker game using neural networks and image recognition techniques. The primary goal of the project is to assist players by automatically identifying cards during a game running through Bluestacks X.

## Features

- **Real-time Card Recognition**: Automatically identifies and displays the cards on the table and in your hand during a poker game.
- **Image Recognition**: Utilizes neural networks to recognize and classify the cards from the game's screen.
- **Integration with Bluestacks X**: Seamlessly operates within the Bluestacks X environment to capture and process game visuals.

## Table of Contents

- [Usage](#usage)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [License](#license)

## Usage

1. **Start Bluestacks X**: Open Bluestacks X and launch the poker game.

2. **Run the Recognition Script**:
   ```bash
   python main.py
   ```

3. **Play Poker**: The program will automatically recognize and display the cards on the table and in your hand in real-time.

## How It Works

This project employs a combination of screen capture, image processing, and neural networks to recognize poker cards during the game. The main steps include:

1. **Screen Capture**: The program captures the image of the game table from Bluestacks X.
2. **Image Processing**: The captured image is pre-processed to highlight the cards.
3. **Recognition and Classification**: A neural network analyzes the highlighted areas and determines the cards present.

## Requirements

- Python 3.8 or higher
- Bluestacks X
- Libraries specified in `requirements.txt`

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3. See the [LICENSE](LICENSE) file for the full terms.

**Note**: This project is intended for personal use only to enhance poker playing skills. Using automated tools in live games or competitions may be illegal or violate service terms. Please use it responsibly.