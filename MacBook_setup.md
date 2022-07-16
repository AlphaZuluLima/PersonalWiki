# Setting up a Macbook

## Install Initial Applications

### Install xcode-select (this takes about 30 minutes)
This is a prerequisite for installing Homebrew.

In a Terminal session, type the following command:
```
xcode-select --install
```

Navigate to *System Preferences -> Software Update* and check for updates. Install any updates for xcode-select.

### Install Homebrew
#### References
https://brew.sh

https://www.youtube.com/watch?v=SELYgZvAZbU

#### Procedure
In a Terminal session, type the following command:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install Python
