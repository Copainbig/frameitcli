## frameit cli

Usage :
```
poetry run python3 -m frameit.cli ~/Desktop/synced/photos/merlimont_2023_exports -r
```

Test : 
```
poetry run pytest --cov=frameit --cov-report=term-missing
```

Create executable :
```
poetry run pyinstaller --onefile src/frameit/cli.py \
  --name frameit-cli \
  --hidden-import=multiprocessing \
  --hidden-import=zlib \
  --hidden-import=argparse \
  --hidden-import=webcolors \
  --hidden-import=typing \
  --hidden-import=pathlib \
  --runtime-tmpdir .
```