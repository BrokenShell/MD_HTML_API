from markdown2 import markdown


class MarkdownToHTML:
    extras = ["tables", "fenced-code-blocks"]

    def __call__(self, markdown_string: str) -> str:
        return markdown(markdown_string, extras=self.extras)


md_to_html = MarkdownToHTML()


def md_file_to_html_file(markdown_filepath: str, html_filepath: str) -> str:
    with open(markdown_filepath, "r") as file:
        result = md_to_html(file.read())
    with open(html_filepath, "w") as file:
        file.write(result)
    return result


if __name__ == '__main__':
    md_file_to_html_file("input.md", "output.html")
