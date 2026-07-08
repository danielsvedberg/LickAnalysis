# Git Setup and Repository Clone Guide

This guide covers installing Git and cloning this repository from GitHub.

## Table of Contents
1. [Installing Git](#installing-git)
2. [Configuring Git](#configuring-git)
3. [Cloning the Repository](#cloning-the-repository)
4. [Verifying the Clone](#verifying-the-clone)

---

## Installing Git

### Windows

#### Method 1: Using Git for Windows Installer (Recommended)

1. **Download the installer**
   - Visit [git-scm.com](https://git-scm.com)
   - Click "Download for Windows"
   - The latest stable version will download automatically

2. **Run the installer**
   - Double-click the downloaded `.exe` file
   - Click "Yes" if prompted by User Account Control

3. **Installation wizard**
   - Click "Next" through the welcome screen
   - Select installation location (default is fine): `C:\Program Files\Git`
   - Click "Next"
   - Choose components (default selections are fine)
   - Click "Next"
   - Select start menu folder (or skip)
   - Click "Next"

4. **Line ending configuration**
   - Choose "Checkout Windows-style, commit Unix-style line endings" (recommended for cross-platform projects)
   - Click "Next"

5. **Terminal emulator**
   - Select "Use Windows' default console window"
   - Click "Next"

6. **Extra options**
   - Keep default settings
   - Click "Next" then "Install"

7. **Complete installation**
   - Uncheck "View Release Notes" if desired
   - Click "Finish"

#### Method 2: Using Windows Package Manager (winget)

Open PowerShell as Administrator and run:
```powershell
winget install Git.Git
```

#### Method 3: Using Chocolatey

If you have Chocolatey installed, run in Administrator PowerShell:
```powershell
choco install git
```

### macOS

#### Method 1: Using Homebrew (Recommended)

1. Install Homebrew if you don't have it:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. Install Git:
   ```bash
   brew install git
   ```

#### Method 2: Using Git Installer

1. Visit [git-scm.com](https://git-scm.com)
2. Download the macOS installer
3. Run the `.dmg` file and follow the installation wizard

#### Method 3: Command Line Tools

Run in Terminal:
```bash
xcode-select --install
```

This installs Git as part of Xcode Command Line Tools.

### Linux

#### Ubuntu/Debian

```bash
sudo apt-get update
sudo apt-get install git
```

#### Fedora/CentOS/RHEL

```bash
sudo dnf install git
```

#### Arch Linux

```bash
sudo pacman -S git
```

---

## Configuring Git

After installing Git, configure it with your identity. This information will be attached to your commits.

### 1. Set Your Name and Email

Open Terminal/PowerShell/Command Prompt and run:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

**Example:**
```bash
git config --global user.name "Dan Svedberg"
git config --global user.email "dan.ake.svedberg@gmail.com"
```

### 2. Verify Configuration

Check your configuration:
```bash
git config --global user.name
git config --global user.email
```

### 3. Optional: Set Default Text Editor

For Windows (Notepad):
```bash
git config --global core.editor "notepad"
```

For Windows (VS Code):
```bash
git config --global core.editor "code --wait"
```

For macOS/Linux (Nano):
```bash
git config --global core.editor "nano"
```

---

## Cloning the Repository

### Basic Clone

1. **Navigate to where you want the repository**

   **Windows (PowerShell/Command Prompt):**
   ```powershell
   cd C:\Users\YourUsername\Documents\Projects
   ```

   **macOS/Linux (Terminal):**
   ```bash
   cd ~/Documents/Projects
   ```

2. **Clone the repository**

   Replace `USERNAME` and `REPO_NAME` with the actual GitHub username and repository name:
   ```bash
   git clone https://github.com/USERNAME/REPO_NAME.git
   ```

   **Example:**
   ```bash
   git clone https://github.com/username/LickAnalysis.git
   ```

3. **Navigate into the cloned repository**
   ```bash
   cd REPO_NAME
   ```

   **Example:**
   ```bash
   cd LickAnalysis
   ```

### Clone with SSH (Advanced)

If you have SSH keys set up with GitHub, you can clone using SSH (faster for repeated operations):

```bash
git clone git@github.com:USERNAME/REPO_NAME.git
```

To set up SSH keys:
1. Visit [GitHub SSH Key Setup](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
2. Follow the official GitHub documentation

---

## Verifying the Clone

### Check Repository Status

Navigate into your cloned repository and run:
```bash
git status
```

Expected output:
```
On branch main
nothing to commit, working tree clean
```

### View Repository Information

```bash
git remote -v
```

Should show:
```
origin  https://github.com/USERNAME/REPO_NAME.git (fetch)
origin  https://github.com/USERNAME/REPO_NAME.git (push)
```

### View Commit History

```bash
git log --oneline -n 5
```

Shows the last 5 commits.

### List Branches

```bash
git branch -a
```

Shows all local and remote branches.

---

## Troubleshooting

### Git command not found

**Windows:** 
- Restart your terminal/PowerShell after installation
- Verify installation: `git --version`
- Check System PATH includes Git installation directory

**macOS/Linux:**
- Run `which git` to verify location
- If not found, reinstall using your package manager

### Permission denied (publickey)

This occurs when using SSH without proper key setup:
- Use HTTPS clone instead: `git clone https://github.com/...`
- Or set up SSH keys following [GitHub's guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### SSL certificate problem

Usually occurs on corporate networks:
- Temporarily disable SSL verification: `git config --global http.sslVerify false`
- Better solution: Get your network administrator to help configure Git for your corporate network

### Repository already exists

If you try to clone into a folder that already exists:
- Clone into a different folder: `git clone https://github.com/USERNAME/REPO_NAME.git new-folder-name`
- Or remove the existing folder first

---

## Next Steps

After cloning, you may want to:

1. **Read the README**
   ```bash
   cat README.md
   ```

2. **Check for setup instructions**
   Look for files like `SETUP.md`, `CONTRIBUTING.md`, or `requirements.txt`

3. **Install dependencies** (if applicable)
   For Python projects:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a new branch for your work**
   ```bash
   git checkout -b feature/my-feature
   ```

---

## Common Git Commands Reference

```bash
# Check status of files
git status

# View commit history
git log

# Create and switch to a new branch
git checkout -b branch-name

# Switch to existing branch
git checkout branch-name

# Stage files for commit
git add filename
git add .                    # Stage all changes

# Commit changes
git commit -m "Commit message"

# Push changes to remote
git push origin branch-name

# Pull latest changes
git pull origin branch-name

# View differences
git diff
git diff --staged
```

---

## Additional Resources

- [Official Git Documentation](https://git-scm.com/doc)
- [GitHub Git Guides](https://github.com/git-tips/tips)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
