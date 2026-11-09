from pathlib import Path

current_dir = Path.cwd()
current_file = Path(__file__).name

for filepath in current_dir.iterdir:
    if filepath.name == Path(__file__).name:
        continue

    print(f"file name: {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text('encoding=utf-8')
        print(f'    Content: {content}')