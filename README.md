Subtitle Matching and Renaming Tool
This Python script provides a solution to efficiently match subtitle files (.srt) with corresponding video files based on season and episode numbers. It also ensures that the subtitle files are encoded in UTF-8 and renames them to match the video filenames.

Features
Subtitle Encoding Conversion: Converts subtitle files to UTF-8 encoding if they are not already in UTF-8.
Subtitle and Video Matching: Matches subtitle files with video files based on season and episode pattern (e.g., S01E01).
Automatic Renaming: Renames subtitle files to match the corresponding video filenames.
Supports All Video Formats: Recognizes all known video file formats.
Requirements
Python 3.x
chardet library
Installation
Install Required Libraries
Before running the script, ensure that the chardet library is installed. Open a command prompt and run:

bash
Copy code
pip install chardet
Clone the Repository
If the script is hosted in a repository, clone it using:

bash
Copy code
git clone https://github.com/yourusername/subtitle-matching-tool.git
Replace the URL with the appropriate repository URL.

Making an Executable (Optional)
If you want to create a standalone executable for Windows, you can use PyInstaller:

bash
Copy code
pip install pyinstaller
pyinstaller --onefile script.py
The executable will be located in the dist directory.

Usage
Place the script in the directory containing the video and subtitle files, then run it using:

bash
Copy code
python script.py
Replace script.py with the appropriate filename if different.

How It Works
Iterates Through Files: The script scans the directory for video and subtitle files.
Converts Subtitle Encoding: Converts each subtitle file to UTF-8 encoding if needed.
Matches Subtitles with Videos: Matches each subtitle file with a video file based on season and episode numbers.
Renames Subtitles: Renames subtitle files to match the corresponding video filenames.
Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Support and Contact
If you have any queries or need further assistance, please open an issue or contact the maintainers.

This README includes detailed information on the features, installation, usage, and more, for users of different experience levels. Modify the URLs and other specific details as needed for your project. If the script is part of a larger project with contributing guidelines or a specific license, you may need to create those files (CONTRIBUTING.md, LICENSE.md, etc.) and link to them accordingly.
