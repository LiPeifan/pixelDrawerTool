from pathlib import Path 

language = "zh_cn"
path = Path(f'app/i18n/{language}.json')
contents = path.read_text()

print(contents)