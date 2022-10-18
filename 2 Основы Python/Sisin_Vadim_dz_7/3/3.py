import os
import shutil

ROOT_DIR = 'my_project/templates'

if os.path.exists(ROOT_DIR):
    shutil.rmtree(ROOT_DIR)

for root, dirs, files in os.walk('my_project'):
    if root.endswith('templates'):
        shutil.copytree(
            os.path.join(root, dirs[0]), 
            os.path.join(ROOT_DIR,dirs[0])
        )
    