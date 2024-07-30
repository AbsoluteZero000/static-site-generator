from copystatic import copy_files_recursive
import os
import shutil
from generate_content import generate_page_recursive



dir_path_static = "./static"
dir_path_public = "./public"

content_path = "./content"
template_path = "./template.html"

def main():
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_files_recursive(dir_path_static, dir_path_public)
    generate_page_recursive(content_path, template_path, dir_path_public)

main()
