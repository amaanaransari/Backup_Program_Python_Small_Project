# Python File Backup Script

A simple Python script to create compressed backups of a directory using Python's built-in libraries.

## Features

- Creates compressed `.tar.gz` backup archives.
- Automatically adds a timestamp to each backup filename.
- Uses Python's `os`, `datetime`, and `shutil` modules.
- Runs on Windows using Python or Git Bash.

## Requirements

- Python 3.x
- Windows OS (tested with Git Bash)

## Usage

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <repository-name>
   ```

3. Update the `source` and `destination` paths in `backup.py` to match your directories.

4. Run the script:

   ```bash
   python backup.py
   ```

## Example

The script creates a compressed backup with a timestamp in the destination directory.

```text
backups/
└── backup_2026-10-15_17-30-45.tar.gz
```

After successful execution, the script prints:

```text
Backup completed!
```

## Technologies Used

- Python
- OS module
- Datetime module
- Shutil module

## Future Improvements

- Add automatic scheduled backups.
- Add error handling.
- Add backup cleanup to remove old archives.

---

**Author:** Amaan Ansari
