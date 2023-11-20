import logging
import os

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)

INPUT_DIR = "/opt/app/input"
OUTPUT_DIR = "/opt/app/output"


def list_directory(directory):
    for (dirpath, dirnames, filenames) in os.walk(directory):
        LOG.info(f"""Directory: {directory}
            Input path: {dirpath}
            Sub directories: {dirnames}
            Files: {filenames}
        """)
        return dirpath, dirnames, filenames
    LOG.error("Path doesn't exists")
    raise Exception("Path doesn't exists")


def save_output(directory):
    if not os.path.isdir(directory):
        LOG.error("Directory should exists")
        raise Exception("Directory should exists")

    output_path = os.path.join(directory, "output.txt")

    with os.fdopen(os.open(output_path, os.O_WRONLY | os.O_CREAT), 'w') as f:
        f.truncate()
        f.write("Hi, this file will have some output")
        LOG.info(f"Successfully write to {directory}")


def main():
    LOG.info("Hello from Azure Template")
    list_directory(INPUT_DIR)
    save_output(OUTPUT_DIR)
    list_directory(OUTPUT_DIR)


if __name__ == '__main__':
    main()
