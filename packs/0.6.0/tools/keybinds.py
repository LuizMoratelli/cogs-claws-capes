import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def generate():
    layout = json.loads((ROOT / 'pack/keybinds.json').read_text())
    bindings = layout['bindings']
    required = {
        'key_key.sprint': 'key.keyboard.left.shift',
        'key_key.sneak': 'key.keyboard.left.control',
    }
    for action, value in required.items():
        if bindings.get(action) != value:
            raise ValueError('Unexpected movement binding: ' + action)
    for setting in ('toggleSprint', 'toggleCrouch'):
        if layout['options'].get(setting) is not False:
            raise ValueError(setting + ' must be false')
    primary = collections.defaultdict(list)
    for action in layout['primary_actions']:
        primary[bindings[action]].append(action)
    conflicts = {key: actions for key, actions in primary.items() if len(actions) > 1}
    if conflicts:
        raise ValueError('Competing primary shortcuts: ' + json.dumps(conflicts))
    lines = ['version:' + str(layout['data_version'])]
    for setting, value in layout['options'].items():
        lines.append(setting + ':' + str(value).lower())
    for action, value in bindings.items():
        parts = value.split(':')
        if not value.startswith(('key.keyboard.', 'key.mouse.')):
            raise ValueError('Invalid key: ' + value)
        if len(parts) > 2 or (len(parts) == 2 and parts[1] not in ('ALT', 'CONTROL', 'SHIFT')):
            raise ValueError('Invalid modifier: ' + value)
        lines.append(action + ':' + value)
    output = ROOT / 'overrides/options.txt'
    output.write_text('\n'.join(lines) + '\n')
    return len(bindings)


if __name__ == '__main__':
    print('Generated', generate(), 'keybindings. Hold Shift to sprint; Ctrl to crouch.')
