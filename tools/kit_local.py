# -*- coding: utf-8 -*-
"""Особое для набора в общей проверке skill-skill/tools/check_docs.py.

Всё необязательно; ненужное удалить, пустой файл тоже можно удалить.
GENERIC — слова имени папки проекта, не считающиеся его приметой;
TEXT_EXT — дополнительные текстовые расширения для сверки со стоп-листом;
PROJECT_EXT — расширения файлов проекта, чьи имена становятся стоп-словами;
project_words(project_dir) -> set — свои приметы из папки проекта;
extra_checks(root) -> list[str] — свои расхождения.
"""
GENERIC = set()
TEXT_EXT = ()
PROJECT_EXT = ()


def extra_checks(root):
    return []
