import yaml
from jinja2 import Template
import mkdocs_gen_files
import re

# Load YAML commands data from file
def load_commands(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Generate a mapping of commands to Markdown links
def create_command_links(commands):
    return {
        command['command']: f"[`@{command['command']}`](../commands/{command['command']}_{command['type']}.md)"
        for command in commands
    }

# Auto-link command mentions within notes
def auto_link_notes(notes, command_links):
    for command, link in command_links.items():
        notes = re.sub(rf"(?<!\w)@{command}(?!\w)", link, notes)
    return notes

# Render Markdown for each command using the template
def render_command(template, command, command_links):
    command['notes'] = auto_link_notes(command.get('notes', ''), command_links)
    return template.render(
        command=command.get('command', 'Unknown Command'),
        description=command.get('description', 'No description available.'),
        syntax=command.get('syntax', 'No syntax available.'),
        parameters=command.get('parameters', []),
        notes=command['notes'],
        output=command.get('output', ''),
        related_commands=command.get('related_commands', [])
    )

# Write the generated Markdown to the appropriate file
def write_markdown(command, content):
    file_path = f"./commands/{command['command']}_{command['type']}.md"
    with mkdocs_gen_files.open(file_path, 'w') as f:
        f.write(content)
    print(f"Generated: {file_path}")

# Execute the generation process
commands = load_commands('./rlv_commands.yml')
command_links = create_command_links(commands)

with open('./templ/rlv_command.j2', 'r') as template_file:
    template = Template(template_file.read())

for command in commands:
    output = render_command(template, command, command_links)
    write_markdown(command, output)
