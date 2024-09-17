[DRAFT]

# Code documentation

The RLVa code is organized into several key files and classes, each serving a specific role in integrating RLV functionality into the viewer. Below is an overview of the file layout and the purpose of each component.

## File Layout
### `rlvdefines.h`
This header file contains all the preprocessor defines, constants, and enumerations used throughout the RLVa code and the general viewer.

### `rlvactions.h` / `rlvactions.cpp`
The RlvActions class serves as the preferred interface for interacting with RLVa. It provides a comprehensive set of methods that allow developers to perform RLV checks and actions without delving into the underlying complexities of the RLV specificiation or implementation.

When integrating RLV checks or actions into new features, utilize its methods to ensure consistency and avoid dealing with low-level implementation details

### `rlvcommon.h` / `rlvcommon.cpp`
These files contain utility functions and classes that are utilized by both the RLVa code and the broader viewer codebase.

### `rlvfloaters.h` / `rlvfloaters.cpp`
These contain the code for the various RLVa floaters.

### `rlvhelper.h` / `rlvhelper.cpp`
These files contain utility functions and classes used exclusively by the RLVa code, specifically within rlvhandler.cpp, rlvinventory.cpp, and rlvui.cpp. They are not intended for use outside of these components.

### `rlvhandler.h` / `rlvhandler.cpp`
This is the main entry point for incoming RLV commands. The handler is responsible for interpreting and executing commands received from in-world objects or scripts, altering the viewer's behavior as dictated by the RLV protocol.
