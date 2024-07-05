import os
from datetime import datetime
import re
import pdb
from typing import List

import yaml

AUTHORS = ["johnsturgeon"]  # Global variable for authors

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)

def convert_metadata_from_jekyll_to_mkdocs(jekyll_file):
    with open(jekyll_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Extracting the YAML front matter
    front_matter = re.search(r"^---\s+(.*?)\s+---", content, re.DOTALL)
    if not front_matter:
        return None

    # Load YAML data
    yaml_data = yaml.safe_load(front_matter.group(1))

    tags: List = []
    if yaml_data.get("tags"):
        tags= yaml_data.get("tags").split()

    raw_categories: List = []
    if yaml_data.get("categories"):
        raw_categories = yaml_data.get("categories", []).split(',')
    categories: List = []
    category: str
    for category in raw_categories:
        if category == "hdtv":
            categories.append("HDTV")
        else:
            categories.append(category.strip().title())
    if not raw_categories:
        for tag in tags:
            if tag == "hdtv":
                categories.append("HDTV")
            else:
                categories.append(tag.strip().title())

    description: str = yaml_data.get("description", "")
    # Preparing MkDocs YAML header
    mkdocs_data = {
        "date": {
            "created": datetime.strptime(
                jekyll_file.split("/")[-1][:10], "%Y-%m-%d"
            ).date()
        },
        "authors": AUTHORS,
        "draft": True
    }
    if description:
        mkdocs_data['description'] = description
    if categories:
        mkdocs_data['categories'] = categories
    if tags:
        mkdocs_data['tags'] = tags


    # Add 'updated' date if 'last_modified_at' is present
    # and is a datetime object
    if "last_modified_at" in yaml_data and isinstance(
        yaml_data["last_modified_at"], datetime
    ):
        mkdocs_data["date"]["updated"] = yaml_data["last_modified_at"].date()

    # Handle draft status
    if not yaml_data.get("published", True):
        mkdocs_data["draft"] = True

    # Convert to YAML string
    mkdocs_yaml = yaml.dump(mkdocs_data, Dumper=MyDumper, default_flow_style=False).strip()

    # Combine new YAML with the original content without old YAML and
    # add Jekyll title as top-level header
    new_content = (
        "---\n"
        + mkdocs_yaml
        + "\n---\n\n# "
        + yaml_data.get("title", "")
        + re.sub(r"^---\s+.*?\s+---", "", content, flags=re.DOTALL)
    )

    return new_content


def main():
    os.makedirs("./docs/drafts", exist_ok=True)

    for root, dirs, files in os.walk("./myblog/_posts"):
        for filename in files:
            if filename.endswith(".markdown"):
                jekyll_file = os.path.join(root, filename)
                new_content = convert_metadata_from_jekyll_to_mkdocs(jekyll_file)

                if new_content:
                    # Fixing the path for new_root
                    new_root = root.replace("./myblog/old_jekyll_posts", "./docs/drafts")
                    os.makedirs(new_root, exist_ok=True)
                    with open(
                        os.path.join(new_root, filename), "w", encoding="utf-8"
                    ) as file:
                        file.write(new_content)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An exception occurred: {e}")
        pdb.post_mortem()