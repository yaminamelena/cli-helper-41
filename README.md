# cli-helper-41 

cli-helper-41 is a versatile autoclicker designed to improve efficiency in repetitive tasks. Built with Python, this tool offers a simple configuration to help users automate mouse clicks seamlessly.

## Features
- **Custom Click Intervals**: Users can specify how rapidly clicks occur, providing flexibility for various applications.
- **Hotkey Support**: Easily start and stop the autoclicking process with user-defined keyboard shortcuts for convenient operation.
- **Click Location Control**: Choose between clicking at the current mouse position or a fixed screen location to accommodate different workflows.
- **Log Click Actions**: Maintains a log of click events, allowing users to review their actions and performance metrics.

## Installation
To get started with cli-helper-41, clone the repository and install the required dependencies via pip:
```bash
git clone https://github.com/YourUsername/cli-helper-41.git
cd cli-helper-41
pip install -r requirements.txt
```

## Basic Usage
Run the autoclicker script with Python, specifying your desired parameters for clicks per second and hotkeys:
```bash
python autoclicker.py --clicks 10 --interval 0.1 --hotkey 'ctrl + b'
```
This command configures the autoclicker to perform clicks at a rate of 10 clicks per second, with a 0.1-second interval betweenClicks whenever the 'ctrl + b' hotkey is pressed.

For more customization options, run:
```bash
python autoclicker.py --help
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Feel free to contribute to this project or reach out with any suggestions or issues you encounter. Your feedback helps improve cli-helper-41!