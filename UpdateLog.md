# PyBridge (update log)

PyBridge allows you to create a project that can be ran in the main platforms (Linux, macOS and Windows).
PyBridge has a native library making it easy to access your FileSystem such as "Downloads", "Documents" and "Desktop" folders in all platforms.

## News

- Added new native library: time
- Added Module "system" to PyBridge
- Added Library "Logs.py" to "system" module
- Added Library "Requirements.py" to "system" module
- Added Backup reference to FileSystem.py
- Added Samples reference to FileSystem.py
- Added .gitignore to projects created by PyBridge
- Added .gitignore to PyBridge
- Added ability to download more sample codes
- Added ability to create a Jupyter Notebook project


## Changes

- Updated modules and libraries to improve system ("SystemRequirements.py" is deprecated. Use "Requirements.py" instead)
- Projects create using PyBridge will follow PyBridge FileSystem standards (See "Structure of Projects Created by PyBridge" in README.MD file in the root of project)

1. Renamed Module "ErrorReport" to "exception"
2. Renamed Module "Linux" to "linux"
3. Renamed Module "Mac" to "mac"
4. Renamed Module "Windows" to "windows"

## Fixes

- Improvements in "Download Samples" feature