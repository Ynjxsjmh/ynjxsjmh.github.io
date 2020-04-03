import re
import os

__author__ = "Ynjxsjmh"
__version__ = "1.0"
__maintainer__ = "Ynjxsjmh"
__email__ = "ynjxsjmh@gmail.com"
__status__ = "Production"

# TODO Only in-place replace class in `class=""`

tarpath = "./html"
despath = "./build"


def get_all_files_in_folder(folder):
    file_absolute_path_list = []
    print(folder)
    print(next(os.walk(folder)))
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_absolute_path_list.append(os.path.join(dirpath, filename))
        for dirname in dirnames:
            sub_file_absolute_path_list = get_all_files_in_folder(os.path.join(dirpath, dirname))
            file_absolute_path_list.extend(sub_file_absolute_path_list)
    return file_absolute_path_list


def upgrade_bsv3_to_bsv4(content):
    # [Grid system](https://getbootstrap.com/docs/4.0/migration/#grid-system)
    # Added a new sm grid tier below 768px for more granular control. We now have xs, sm, md, lg, and xl.
    # This also means every tier has been bumped up one level (so .col-md-6 in v3 is now .col-lg-6 in v4).
    # https://getbootstrap.com/docs/3.3/css/#grid-options
    # https://getbootstrap.com/docs/4.1/layout/grid/
    bsv3_grid = ["xs", "sm", "md", "lg"]
    bsv4_grid = ["sm", "md", "lg". "xl"]

    for i in range(3, -1, -1):
        # You can only run this code once
        content = re.sub(r"col-{0}-(\d+)".format(bsv3_grid[i]), r"col-{0}-\1".format(bsv4_grid[i]))

    content = re.sub(r"col-[a-z]+-offset-(\d+)", r"offset-\1", content)
    content = re.sub(r"col-[a-z]+-push-(\d+)", r"order-\1-2", content)
    content = re.sub(r"col-[a-z]+-pull-(\d+)", r"order-\1-1", content)

    content = content.replace("panel", "card")
    content = content.replace("panel-heading", "card-header")
    content = content.replace("panel-title", "card-title")
    content = content.replace("panel-body", "card-body")
    content = content.replace("panel-footer", "card-footer")
    content = content.replace("panel-primary", "card bg-primary text-white")
    content = content.replace("panel-success", "card bg-success text-white")
    content = content.replace("panel-info", "card text-white bg-info")
    content = content.replace("panel-warning", "card bg-warning")
    content = content.replace("panel-danger", "card bg-danger text-white")
    content = content.replace("well", "card card-body")
    content = content.replace("thumbnail", "card card-body")

    # https://stackoverflow.com/questions/40178386/bootstrap-4-navbar-items-on-right-side
    content = content.replace("navbar-right", "ml-auto")
    content = content.replace("navbar-toggle", "navbar-toggler")
    content = content.replace("navbar-default", "navbar-light")
    content = content.replace("navbar-btn", "nav-item")
    content = content.replace("navbar-fixed-top", "fixed-top")
    content = content.replace("nav-stacked", "flex-column")

    content = content.replace("btn-default", "btn-secondary")
    content = content.replace("img-responsive", "img-fluid")
    content = content.replace("img-circle", "rounded-circle")
    content = content.replace("img-rounded", "rounded")
    content = content.replace("form-horizontal", "removed)")
    content = content.replace("radio", "form-check")

    # 注意
    content = content.replace("checkbox", "form-check")

    content = content.replace("input-lg", "form-control-lg")
    content = content.replace("input-sm", "form-control-sm")
    content = content.replace("control-label", "col-form-label")
    content = content.replace("table-condensed", "table-sm")

    # 注意
    content = content.replace("item", "carousel-item")
    content = content.replace("help-block", "form-text")

    # https://getbootstrap.com/docs/4.0/migration/#utilities
    content = content.replace("pull-right", "float-right")
    content = content.replace("pull-left", "float-left")

    content = content.replace("center-block", "mx-auto d-block")

    # https://stackoverflow.com/questions/35351353/missing-visible-and-hidden-in-bootstrap-v4
    content = content.replace("hidden-xs", "d-none")
    content = content.replace("hidden-sm", "d-sm-none")
    content = content.replace("hidden-md", "d-md-none")
    content = content.replace("hidden-lg", "d-lg-none")
    content = content.replace("visible-xs", "d-block d-sm-none")
    content = content.replace("visible-sm", "d-none d-sm-block d-md-none")
    content = content.replace("visible-md", "d-none d-md-block d-lg-none")
    content = content.replace("visible-lg", "d-none d-lg-block d-xl-none")

    content = content.replace("label", "badge")
    content = content.replace("badge", "badge badge-pill")

    return content


file_list = get_all_files_in_folder(tarpath)

for tar_file in file_list:
    with open(tar_file, 'r', encoding="utf-8") as f:
        content = f.read()

    content = upgrade_bsv3_to_bsv4(content)

    des_file = tar_file.replace(tarpath, despath)
    os.makedirs(os.path.dirname(des_file), exist_ok=True)
    print(des_file)
    with open(des_file, 'w', encoding="utf-8") as f:
        f.write(content)
