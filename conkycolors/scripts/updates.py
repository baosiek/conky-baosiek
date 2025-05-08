import subprocess


def count_updates():
    """
    Counts the number of packages available for update on an Ubuntu system.

    Returns:
        int: Number of packages available for update.
    """
    try:
        # Run the command to check for updates
        result = subprocess.run(
            ['apt', 'list', '--upgradable'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check if the command executed successfully
        if result.returncode != 0:
            raise RuntimeError(
                f"Error checking updates: {result.stderr.strip()}"
            )

        # Parse the output to count the number of upgradable packages
        lines = result.stdout.strip().split('\n')
        # The first line is a header, so subtract 1 from the total count
        return max(0, len(lines) - 1)

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


if __name__ == "__main__":
    updates_count = count_updates()
    print(f"{updates_count}")
