# micVolumeGuard.py

Automatically restores your microphone to 100% volume whenever it drops.

---

## Requirements

- Windows
- Python 3.7+

---

## Installation

### 1. Install Python
Download Python 3.7+:
https://www.python.org/downloads/

**IMPORTANT:**
During installation, check **Add Python to PATH**

### 2. Download the program
- Download the repository as a ZIP
- Extract the folder somewhere easy (Desktop recommended)

### 3. Install dependencies (one time only)
Double-click **install.bat** and wait for it to finish.

### 4. Run the program
Double-click **start.bat**

---

## What it does

- Monitors your default microphone every 0.5s
- Instantly restores volume to 100% if a drop is detected
- Logs every restore with a timestamp and counter
- Automatically recovers if your mic is unplugged and replugged

---

## Output
```
Microphone Volume Guard
──────────────────────────────
Target: 100%  |  Polling: every 0.5s
──────────────────────────────
[14:22:09] Drop: 45% → 100%  (#1)
[14:22:14] Drop: 0% → 100%   (#2)
──────────────────────────────
Stopped. 2 restore(s) made.
```

---
