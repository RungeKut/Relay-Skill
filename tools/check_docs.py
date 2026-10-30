# -*- coding: utf-8 -*-
"""Обёртка: общая проверка скилла лежит в соседнем скилле skill-skill.

    python tools/check_docs.py [--project <папка проекта>]

Одинакова во всех наборах; своё — в tools/kit_local.py.
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = os.path.join(os.path.dirname(ROOT), "skill-skill", "tools",
                     "check_docs.py")

if __name__ == "__main__":
    if not os.path.exists(CHECK):
        print("нужен соседний скилл skill-skill: git clone "
              "https://github.com/RungeKut/Skill-Skill.git "
              "<папка скиллов>/skill-skill")
        sys.exit(2)
    sys.exit(subprocess.call([sys.executable, CHECK, "--root", ROOT]
                             + sys.argv[1:]))
