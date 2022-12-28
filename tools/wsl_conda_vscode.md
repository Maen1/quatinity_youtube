# WSL

Windows subsystem for Linux,  all Linux flexibility with stable apps on windows.

### Install wsl

will enable wsl and install Ubuntu by defautlt

you need to restart you machine.

```jsx
#powershell
wsl --install 
```

### checkout wsl distors

```jsx
wsl --list --online
#wsl -l -o
```

### change between versions

```jsx
wsl -l -v
wsl --set-version <distro> 2
wsl pwd
```

# Anaconda

### Link to anaconda installers

```jsx
https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```

### installation steps

```bash
curl -O  https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
shasum -a 256 Anaconda3-2022.10-Linux-x86_64.sh
bash Anacondaxxxx.sh

# The base environment is activated by default
conda config --set auto_activate_base True

# The base environment is not activated by default
conda config --set auto_activate_base False
```

# VS code

link vs code to conda‘s python interpreter 

install remote extension

```jsx
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack
```

on vs code 

```jsx
ctrl + shift + x // install wsl and python extention 
ctrl + shift + v // select python interpreter 
```

## Delete WSL distro with all its data

```bash
wsl --unregister <distroName>
```