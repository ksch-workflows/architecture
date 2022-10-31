#!/usr/bin/env python3

import unicodedata
import re
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

# https://stackoverflow.com/a/295466/2339010
# https://github.com/django/django/blob/main/LICENSE
def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def read_summary():
    f = open("SUMMARY.md", "r")
    result = f.readlines()
    f.close()
    return result

def write_summary(lines):
    f = open("SUMMARY.md", "w")
    f.writelines(lines)
    f.close()

def is_link(line):
    if "[]()" in line:
        return False

    m = re.match(".*\[.*\]\(.*\).*", line)
    if m:
        return True
    else:
        return False

def is_link_href_empty(line):
    m = re.match(".*\[.*?\]\((\S+)\)", line)
    if not m:
        return True
    return False

def is_link_href_absolute(line):
    return "http" in line

def is_link_href_relative(line):
    m = re.match(".*\[.*?\]\(\.(\S+)\)", line)
    if not m:
        return False
    return True

def parse_link_level(line):
    m = re.match("^\[.*?\]\(.*", line)
    if m:
        return 0

    m = re.match("(\s+)- \[.*", line)
    if (not m):
        return 2
    number_of_whitespaces = len(m.group(1))
    return int(number_of_whitespaces / 2) + 2

def parse_link_name(line):
    m = re.match(".*\[(.*?)\].*", line)
    return m.group(1)

def parse_link_href(line):
    m = re.match(".*\[.*?\]\((.*?)\).*", line)
    return m.group(1)

def to_relative_path(absolute_path):
    return re.sub(".*?/src/", "./", absolute_path).replace("././", "./")

def walk_tree_down(levels):
    cmd = []
    for i in range(levels):
        cmd.append("..")
    cmd = "/".join(cmd)
    os.chdir(cmd)

def walk_tree_up(slug):
    os.chdir(slug)

def walk_tree_root():
    os.chdir(SCRIPT_DIR + "/../src")

class Entry:
    def __init__(self, name, level, href):
        self.name = name
        self.level = level
        self.slug = slugify(name)
        self.href = href
        
        if not os.path.isdir(self.slug) and not self.slug == "summary":
            os.mkdir(self.slug)

        index = f"{self.slug}/index.md"
        if not os.path.isfile(index) and not level == 1:
            f = open(index, "w")
            f.write(f"# {name}\n")
            if (href):
                f.write("\n")
                f.write("## References\n\n")
                f.write(f"- [{href}]({href})")
            f.close()

        self.index = os.path.realpath(index)

    def text(self):
        link = to_relative_path(self.index)

        if self.level == 0:
            return f"[{name}]({link})\n"

        indentation = ""
        for i in range(level - 2):
            indentation += "  "
        return f"{indentation}- [{name}]({link})\n"

if __name__ == "__main__":
    walk_tree_root()
    original_summary = read_summary()
    updated_summary = []

    previous_entry = None

    for line in original_summary:
       
        if is_link(line):
            href = None
            name = parse_link_name(line)
            level = parse_link_level(line)

            if level == 0 or line.startswith("- ["):
                walk_tree_root()
            else:
                if level < previous_entry.level:
                    walk_tree_down(previous_entry.level - level)
                if level > previous_entry.level:
                    walk_tree_up(previous_entry.slug)

            if is_link_href_absolute(line):
                m = re.match(".*\((.*)\).*", line)
                if m:
                    href = m.group(1)
                else:
                    raise ValueError('Failed to parse href from ' + line)

            if is_link_href_relative(line):
                href = parse_link_href(line)
                expected_base_dir = os.getcwd().replace(SCRIPT_DIR[:len(SCRIPT_DIR) - 3] + "src", ".")
                expected_index_file = expected_base_dir + "/" + f"{slugify(name)}/index.md"
                index_file_path = SCRIPT_DIR + "../src/" + href[1:]
                if (not href == expected_index_file):
                    print(f"\nThe following line doesn't match with the expected index file '{expected_index_file}':\n")
                    print(line)
                    sys.exit(1)

            entry = Entry(name, level, href)

            if is_link_href_empty(line) or is_link_href_absolute(line):
                line = entry.text()
            
            previous_entry = entry

        updated_summary.append(line)

    walk_tree_root()
    write_summary(updated_summary)
    