from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
shutil.copyfile(root/'dist/index.html',root/'index.html')
print('PASS: Pages entry synchronized')
