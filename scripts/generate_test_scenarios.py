import yaml
from jinja2 import Template
import mkdocs_gen_files
import re

# Load YAML test data from file
def load_tests(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Render Markdown for each test using the template
def render_test(template, test):
    return template.render(
        id=test.get('id'),
        title=test.get('title'),
        preconditions=test.get('preconditions', []),
        test_steps=test.get('test_steps', []),
        expected_result=test.get('expected_result', ''),
        notes=test.get('notes', [])
    )

# Write the generated Markdown to the appropriate file
def write_markdown(test, content):
    file_path = f"./development/tests/{test['id']}.md"
    with mkdocs_gen_files.open(file_path, 'w') as f:
        f.write(content)
    print(f"Generated: {file_path}")

# Execute the generation process
tests = load_tests('./rlva_tests.yml')

with open('./templ/rlva_test.j2', 'r') as template_file:
    template = Template(template_file.read())

for test in tests:
    output = render_test(template, test)
    write_markdown(test, output)
