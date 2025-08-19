#!/usr/bin/env python3

import os
import re
from pathlib import Path

def parse_claude_agent(content):
    """Parse a Claude agent file and extract metadata and content."""
    lines = content.strip().split('\n')
    
    # Parse frontmatter
    if not lines[0].strip() == '---':
        return None, None, None
    
    frontmatter = {}
    content_start = 1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            content_start = i + 1
            break
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip().strip('"')
    
    # Get main content
    main_content = '\n'.join(lines[content_start:]).strip()
    
    return frontmatter.get('name', ''), frontmatter.get('description', ''), main_content

def categorize_agent(name, description):
    """Categorize agent based on name and description."""
    name_lower = name.lower()
    desc_lower = description.lower()
    
    # Engineering categories
    if any(term in name_lower for term in ['pro', 'developer', 'engineer', 'architect', 'devops', 'debugger', 'reviewer', 'automator']):
        return 'eng'
    elif any(term in desc_lower for term in ['code', 'programming', 'development', 'software', 'api', 'database', 'infrastructure']):
        return 'eng'
    
    # Marketing categories  
    elif any(term in name_lower for term in ['marketer', 'seo', 'content', 'social']):
        return 'marketing'
    elif any(term in desc_lower for term in ['marketing', 'seo', 'content', 'social media', 'growth']):
        return 'marketing'
    
    # Business categories
    elif any(term in name_lower for term in ['analyst', 'manager', 'support', 'hr', 'legal', 'sales']):
        return 'business'
    elif any(term in desc_lower for term in ['business', 'analysis', 'support', 'legal', 'sales', 'finance']):
        return 'business'
    
    # Design categories
    elif any(term in name_lower for term in ['designer', 'ui', 'ux']):
        return 'design'
    
    # Testing categories
    elif any(term in name_lower for term in ['test', 'qa']):
        return 'testing'
    elif any(term in desc_lower for term in ['testing', 'test', 'quality assurance']):
        return 'testing'
    
    # Security categories
    elif any(term in name_lower for term in ['security', 'auditor']):
        return 'security'
    elif any(term in desc_lower for term in ['security', 'audit', 'vulnerability']):
        return 'security'
    
    # Data categories
    elif any(term in name_lower for term in ['data', 'ml', 'ai']):
        return 'data'
    elif any(term in desc_lower for term in ['data', 'machine learning', 'ai', 'analytics']):
        return 'data'
    
    # Default to misc
    else:
        return 'misc'

def convert_to_chatmode(name, description, content):
    """Convert Claude agent format to GitHub Copilot chat mode format."""
    
    # Extract tools based on content analysis
    tools = ['editFiles', 'codebase', 'search']
    
    # Add specific tools based on content
    if any(term in content.lower() for term in ['terminal', 'command', 'run', 'execute', 'deploy']):
        tools.append('runCommands')
    if any(term in content.lower() for term in ['test', 'testing', 'spec']):
        tools.append('findTestFiles')
    if any(term in content.lower() for term in ['build', 'compile', 'task']):
        tools.append('runTasks')
    if any(term in content.lower() for term in ['issue', 'problem', 'error', 'bug']):
        tools.append('problems')
    if any(term in content.lower() for term in ['web', 'url', 'fetch', 'api']):
        tools.append('fetch')
    
    # Remove duplicates while preserving order
    tools = list(dict.fromkeys(tools))
    
    # Create enhanced description
    enhanced_desc = description
    if not enhanced_desc.endswith('.'):
        enhanced_desc += '.'
    
    # Convert content format
    chatmode_content = f"""---
description: '{enhanced_desc}'
tools: {tools}
---

You are a {name.replace('-', ' ')} with deep expertise in your specialized domain. {description}

Your primary responsibilities:

{content}

**Key Principles**:
- Deliver high-quality, production-ready solutions
- Follow industry best practices and standards
- Provide comprehensive and actionable guidance
- Focus on practical implementation over theory
- Ensure solutions are maintainable and scalable

**When to Engage**:
Use this agent proactively when working in your domain of expertise to get specialized guidance, implementations, and best practices."""

    return chatmode_content

def main():
    claude_dir = Path('./claude')
    modes_dir = Path('./modes')

    # Get all markdown files in claude directory
    claude_files = list(claude_dir.glob('*.md'))
    
    # Skip README
    claude_files = [f for f in claude_files if f.name != 'README.md']
    
    converted_count = 0
    skipped_count = 0
    
    for claude_file in claude_files:
        try:
            with open(claude_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            name, description, main_content = parse_claude_agent(content)
            
            if not name or not description:
                print(f"Skipping {claude_file.name}: Could not parse metadata")
                skipped_count += 1
                continue
            
            # Check if already converted (looking for existing chatmode files)
            category = categorize_agent(name, description)
            output_filename = f"[{category}] {name.replace('_', '-')}.chatmode.md"
            output_path = modes_dir / output_filename
            
            if output_path.exists():
                print(f"Skipping {name}: Already exists as {output_filename}")
                skipped_count += 1
                continue
            
            # Convert to chatmode format
            chatmode_content = convert_to_chatmode(name, description, main_content)
            
            # Write output file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(chatmode_content)
            
            print(f"Converted {name} -> {output_filename}")
            converted_count += 1
            
        except Exception as e:
            print(f"Error converting {claude_file.name}: {str(e)}")
            skipped_count += 1
    
    print(f"\nConversion complete!")
    print(f"Converted: {converted_count}")
    print(f"Skipped: {skipped_count}")

if __name__ == "__main__":
    main()
