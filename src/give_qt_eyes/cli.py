"""Compare saved Qt measurements or add the Codex skill."""
import argparse
import json
from pathlib import Path
import sys

from . import __version__
from .compare import compare, read_capture
from .install import install_skill


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--version', action='version', version=__version__)
    commands = parser.add_subparsers(dest='command', required=True)
    diff = commands.add_parser('compare', help='Compare measurements; review images separately')
    diff.add_argument('before', type=Path)
    diff.add_argument('after', type=Path)
    install = commands.add_parser('install-skill', help='Add the skill without replacing existing files')
    scope = install.add_mutually_exclusive_group(required=True)
    scope.add_argument('--user', action='store_true', help='Use ~/.agents/skills/give-qt-eyes')
    scope.add_argument('--project', type=Path, help='Use PROJECT/.agents/skills/give-qt-eyes')
    args = parser.parse_args(argv)
    try:
        if args.command == 'compare':
            result = compare(read_capture(args.before), read_capture(args.after))
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            base = Path.home() if args.user else args.project
            destination = install_skill(base / '.agents' / 'skills' / 'give-qt-eyes')
            print('Installed skill:', destination)
            print('Use $give-qt-eyes in Codex. Install Qt separately if capture needs it.')
    except (OSError, ValueError) as error:
        print('give-qt-eyes:', error, file=sys.stderr)
        return 2
    except KeyboardInterrupt:
        print('Cancelled; check any partial install before trying again.', file=sys.stderr)
        return 130
    return 0
