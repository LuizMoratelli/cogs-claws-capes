"""Build the single-player Minecraft 1.21.1 pack from its pinned lock."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request
import zipfile
from keybinds import generate

ROOT = Path(__file__).resolve().parents[1]

def fetch(mod):
    target = ROOT / '.cache' / mod['file']
    if target.exists() and hashlib.sha512(target.read_bytes()).hexdigest() == mod['sha512']:
        return
    target.parent.mkdir(exist_ok=True)
    request = urllib.request.Request(mod['url'], headers={'User-Agent': 'CogsClawsCapes/0.6-singleplayer'})
    with urllib.request.urlopen(request, timeout=180) as response:
        data = response.read()
    if hashlib.sha512(data).hexdigest() != mod['sha512']:
        raise RuntimeError('Hash mismatch: ' + mod['file'])
    target.write_bytes(data)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify-downloads', action='store_true')
    args = parser.parse_args()
    generate()
    lock = json.loads((ROOT / 'pack/mods.lock.json').read_text())
    plan = json.loads((ROOT / 'pack/pack.json').read_text())
    mods = list(lock['mods'].values())
    if args.verify_downloads:
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            list(executor.map(fetch, mods))
    files = [{
        'path': 'mods/' + mod['file'],
        'hashes': {'sha1': mod['sha1'], 'sha512': mod['sha512']},
        'env': {'client': 'required', 'server': 'unsupported'},
        'downloads': [mod['url']], 'fileSize': mod['size'],
    } for mod in mods]
    index = {
        'formatVersion': 1, 'game': 'minecraft', 'versionId': plan['version'],
        'name': plan['name'], 'summary': plan['summary'],
        'dependencies': {'minecraft': lock['minecraft'], 'neoforge': lock['loader_version']},
        'files': files,
    }
    output = ROOT / 'dist/cogs-claws-capes-0.6.0-singleplayer.mrpack'
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.writestr('modrinth.index.json', json.dumps(index, indent=2))
        for source in sorted((ROOT / 'overrides').rglob('*')):
            if source.is_file():
                archive.write(source, 'overrides/' + source.relative_to(ROOT / 'overrides').as_posix())
    print(str(output))
    print(str(len(mods)) + ' pinned mods. Single-player distribution; no server bundle.')

if __name__ == '__main__':
    main()
