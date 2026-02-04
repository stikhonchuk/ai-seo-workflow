#!/usr/bin/env python3
"""
Anonymization script for SEO workflow template.
Replaces project-specific data with placeholders.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

# Replacement rules: (pattern, replacement)
# Order matters - more specific patterns should come first
#
# CUSTOMIZE THIS for your project:
# 1. Replace example.com with your actual domain
# 2. Add your owner/business names
# 3. Add any project-specific patterns
#
REPLACEMENTS: List[Tuple[str, str]] = [
    # Domain variations - REPLACE example.com WITH YOUR DOMAIN
    # (r'https?://(?:www\.)?example\.com', 'https://[YOUR-DOMAIN]'),
    # (r'www\.example\.com', '[YOUR-DOMAIN]'),
    # (r'example\.com', '[YOUR-DOMAIN]'),
    # (r'[Ee]xample-project', '[YOUR-PROJECT]'),

    # Contact information (generic patterns)
    (r'\+7\s*\(\d{3}\)\s*\d{3}-\d{2}-\d{2}', '[PHONE]'),  # Russian phone
    (r'\+1\s*\(\d{3}\)\s*\d{3}-\d{4}', '[PHONE]'),  # US phone
    (r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '[EMAIL]'),  # Any email

    # Russian business names (generic pattern)
    (r'ИП\s+[А-Яа-яЁё]+\s+[А-Яа-яЁё]+\s+[А-Яа-яЁё]+', 'ИП [OWNER_NAME]'),

    # Add your specific patterns below:
    # (r'Your Name Here', '[OWNER_NAME]'),
    # (r'Your Address', '[ADDRESS]'),
    # (r'YourBrand', '[BRAND]'),
]

# File extensions to process
ALLOWED_EXTENSIONS = {'.py', '.md', '.txt', '.json', '.yaml', '.yml', '.sh', '.html', '.css', '.js'}

# Files/directories to skip
SKIP_PATTERNS = {
    '__pycache__',
    '.git',
    'venv',
    'node_modules',
    '.pyc',
    'config.py',  # Skip config as it's meant to be customized
    'anonymize.py',  # Skip self
}


def should_process_file(filepath: Path) -> bool:
    """Check if file should be processed."""
    # Skip by extension
    if filepath.suffix not in ALLOWED_EXTENSIONS:
        return False

    # Skip by pattern
    for pattern in SKIP_PATTERNS:
        if pattern in str(filepath):
            return False

    return True


def anonymize_content(content: str, replacements: List[Tuple[str, str]] = None) -> Tuple[str, int]:
    """
    Apply anonymization replacements to content.
    Returns (new_content, number_of_replacements).
    """
    if replacements is None:
        replacements = REPLACEMENTS

    total_replacements = 0
    result = content

    for pattern, replacement in replacements:
        new_result, count = re.subn(pattern, replacement, result)
        total_replacements += count
        result = new_result

    return result, total_replacements


def anonymize_file(filepath: Path, dry_run: bool = False) -> int:
    """
    Anonymize a single file.
    Returns number of replacements made.
    """
    try:
        content = filepath.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        print(f"  Skipping (binary): {filepath}")
        return 0

    new_content, count = anonymize_content(content)

    if count > 0:
        if dry_run:
            print(f"  Would modify: {filepath} ({count} replacements)")
        else:
            filepath.write_text(new_content, encoding='utf-8')
            print(f"  Modified: {filepath} ({count} replacements)")

    return count


def anonymize_directory(directory: Path, dry_run: bool = False) -> Dict[str, int]:
    """
    Anonymize all files in directory recursively.
    Returns stats dict.
    """
    stats = {
        'files_processed': 0,
        'files_modified': 0,
        'total_replacements': 0,
    }

    for filepath in directory.rglob('*'):
        if not filepath.is_file():
            continue

        if not should_process_file(filepath):
            continue

        stats['files_processed'] += 1
        count = anonymize_file(filepath, dry_run=dry_run)

        if count > 0:
            stats['files_modified'] += 1
            stats['total_replacements'] += count

    return stats


def find_unanonymized(directory: Path) -> List[Tuple[Path, str, str]]:
    """
    Find remaining instances of project-specific data.
    Returns list of (filepath, line, match).
    """
    # Patterns to search for (simpler versions for detection)
    # CUSTOMIZE: Add your domain/project patterns here
    search_patterns = [
        # r'your-domain',  # Add your domain pattern
        r'\+7\s*\(\d{3}\)',  # Russian phone numbers
        r'\+1\s*\(\d{3}\)',  # US phone numbers
        # r'@yourdomain\.com',  # Your email domain
    ]

    findings = []

    for filepath in directory.rglob('*'):
        if not filepath.is_file() or not should_process_file(filepath):
            continue

        try:
            content = filepath.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue

        for line_num, line in enumerate(content.splitlines(), 1):
            for pattern in search_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append((filepath, line_num, line.strip()[:100]))
                    break

    return findings


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Anonymize project-specific data')
    parser.add_argument('directory', nargs='?', default='.',
                        help='Directory to process (default: current)')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='Show what would be changed without modifying files')
    parser.add_argument('--check', '-c', action='store_true',
                        help='Check for remaining unanonymized data')
    parser.add_argument('--list-patterns', '-l', action='store_true',
                        help='List current replacement patterns')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')

    args = parser.parse_args()
    directory = Path(args.directory).resolve()

    if not directory.is_dir():
        print(f"Error: {directory} is not a directory")
        sys.exit(1)

    print(f"Processing: {directory}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    if args.list_patterns:
        print("Current replacement patterns:\n")
        for pattern, replacement in REPLACEMENTS:
            status = "active" if not pattern.startswith('#') else "commented"
            print(f"  {pattern}")
            print(f"    → {replacement}\n")
        print(f"Total: {len(REPLACEMENTS)} patterns")
        print("\nEdit REPLACEMENTS list in this file to customize.")
        sys.exit(0)

    if args.check:
        print("Checking for unanonymized data...")
        findings = find_unanonymized(directory)

        if findings:
            print(f"\nFound {len(findings)} potential issues:\n")
            for filepath, line_num, line in findings:
                rel_path = filepath.relative_to(directory)
                print(f"  {rel_path}:{line_num}")
                print(f"    {line}\n")
            sys.exit(1)
        else:
            print("No unanonymized data found!")
            sys.exit(0)

    stats = anonymize_directory(directory, dry_run=args.dry_run)

    print(f"\nSummary:")
    print(f"  Files processed: {stats['files_processed']}")
    print(f"  Files modified: {stats['files_modified']}")
    print(f"  Total replacements: {stats['total_replacements']}")

    if args.dry_run and stats['total_replacements'] > 0:
        print(f"\nRun without --dry-run to apply changes")


if __name__ == '__main__':
    main()
