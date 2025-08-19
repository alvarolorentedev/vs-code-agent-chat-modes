#!/usr/bin/env python3

import re

def url_encode_filename(filename):
    """URL encode filename for GitHub raw URLs"""
    return filename.replace(' ', '%2520').replace('[', '%5B').replace(']', '%5D')

def create_install_link(agent_name, filepath):
    """Create VS Code install link for an agent"""
    encoded_path = url_encode_filename(filepath)
    return f"[install link](https://vscode.dev/redirect?url=vscode%3Achat-mode%2Finstall%3Furl%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2Falvarolorentedev%2Fvs-code-agent-chat-modes%2Frefs%2Fheads%2Fmain%2Fmodes%2F{encoded_path})"

# Read the README file
with open('/Users/lorentea/Workspace/vs-code-agent-chat-modes/README.md', 'r') as f:
    content = f.read()

# Define the sections to update (skip engineering since it's already done)
sections = [
    ('Engineering Department', '[engineering]'),
    ('Marketing Department', '[marketing]'),
    ('Design Department', '[design]'),
    ('Business Department', '[business]'),
    ('Product Department', '[product]'),
    ('Project Management', '[project-management]'),
    ('Studio Operations', '[studio-operations]'),
    ('Security Department', '[security]'),
    ('Data Department', '[data]'),
    ('Testing & Benchmarking', '[testing]'),
    ('Miscellaneous', '[misc]'),
    ('Bonus Agents', '[bonus]')
]

# Process each section
for section_title, prefix in sections:
    # Find the section
    section_pattern = f"### {section_title}.*?\n(.*?)(?=### |## |$)"
    section_match = re.search(section_pattern, content, re.DOTALL)
    
    if section_match:
        section_content = section_match.group(1)
        
        # Find all agent lines in this section
        agent_pattern = r"- \*\*(\[.*?\] .*?)\*\* - (.*?)$"
        
        def replace_agent(match):
            agent_full = match.group(1)
            description = match.group(2)
            
            # Extract just the filename part
            agent_name = agent_full.replace('**', '').replace('[', '').replace(']', '')
            filename = f"{agent_full.split('] ')[0]}] {agent_full.split('] ')[1]}.chatmode.md"
            
            install_link = create_install_link(agent_name, filename)
            
            return f"- **{agent_full}** ({install_link}): {description}"
        
        updated_section = re.sub(agent_pattern, replace_agent, section_content, flags=re.MULTILINE)
        
        # Replace the section in the full content
        content = content.replace(section_content, updated_section)

# Write the updated content back
with open('/Users/lorentea/Workspace/vs-code-agent-chat-modes/README.md', 'w') as f:
    f.write(content)

print("Added install links to all agent sections!")
