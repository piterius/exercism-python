import re


def parse_markdown(text):
    lines = text.split("\n")
    for i in range(len(lines)):
        bold = re.findall("__", lines[i])
        for _ in range(len(bold) // 2):
            lines[i] = re.sub("__", "<strong>", lines[i], 1)
            lines[i] = re.sub("__", "</strong>", lines[i], 1)
        italic = re.findall("_", lines[i])
        for _ in range(len(italic) // 2):
            lines[i] = re.sub("_", "<em>", lines[i], 1)
            lines[i] = re.sub("_", "</em>", lines[i], 1)
        header = re.match("(#+) ", lines[i])
        if header:
            lines[i] = "<h" + str(len(header.group(1))) + ">" + lines[i][len(header.group(1)) + 1:] + "</h" + str(
                len(header.group(1))) + ">"
        elif lines[i].startswith("* "):
            if lines[i - 1].startswith("<ul>") or lines[i - 1].startswith("<li>"):
                lines[i] = "<li>" + lines[i][2:] + "</li>"
            else:
                lines[i] = "<ul><li>" + lines[i][2:] + "</li>"
            if len(lines) == i + 1 or not lines[i + 1].startswith("*"):
                lines[i] += "</ul>"
        else:
            lines[i] = "<p>" + lines[i] + "</p>"
    return "".join(lines)
