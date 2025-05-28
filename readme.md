# Project Setup

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution) (recommended)
- Python 3.9+ (Anaconda includes Python)

## Setup Instructions

### 1. Create and Activate a Conda Environment

```sh
# Create a new conda environment named 'myenv' with Python 3.9
conda create -n myenv python=3.9

# Activate the environment
conda activate myenv
```

### 2. Install Requirements

```sh
pip install -r requirements.txt
```

### 3. Deactivate the Environment

```sh
conda deactivate
```

## Notes

- Make sure to ignore your virtual environment directory (e.g., `venv/`) in `.gitignore` before uploading to GitHub.
- You can change `myenv` to any environment name you prefer.