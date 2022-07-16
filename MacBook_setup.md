# Setting up a Macbook

## Install Initial Applications

---

### Install xcode-select (this takes about 30 minutes)
This is a prerequisite for installing Homebrew.

In a Terminal session, enter the following command:
```
xcode-select --install
```
Navigate to *System Preferences -> Software Update* and check for updates. Install any updates for xcode-select.

---

### Install Homebrew
#### References
https://brew.sh

https://www.youtube.com/watch?v=SELYgZvAZbU

#### Procedure
In a Terminal session, enter the following command:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

### Install Python
#### References
https://docs.python-guide.org/starting/install3/osx/

#### Procedure
In a Terminal session, enter the following the commands:
```
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```
```
export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```
```
brew install python
```

---

### Install 1Password
#### Procedure
In a Terminal session, enter the following the commands:
```
brew install --cask 1password
```

---

### Install Firefox Web Browser
#### Procedure
In a Terminal session, enter the following the commands:
```
brew install --cask firefox
```

---

### Install Google Chrome Web Browser
#### Procedure
In a Terminal session, enter the following the commands:
```
brew install --cask google-chrome
```

---

### Install Visual Studio Code (vscode)
#### Procedure
In a Terminal session, enter the following command:
```
brew install --cask visual-studio-code
```
