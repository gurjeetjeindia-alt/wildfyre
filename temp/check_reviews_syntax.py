import re, subprocess, tempfile, os, sys
path = r'g:\proj\gurjeetDhillon\wildfyre\blocks\ai_gen_block_198ec01.liquid'
text = open(path, encoding='utf-8').read()
match = re.search(r'<script>(.*?)</script>', text, re.S)
if not match:
    print('NO_SCRIPT_BLOCK')
    sys.exit(1)
script = match.group(1)
script = re.sub(r'\{%\s*if\s+customer\s*%\}true\{%\s*else\s*%\}false\{%\s*endif\s*%\}', 'true', script)
script = re.sub(r'\{\{[^\}]+\}\}', '"dummy"', script)
with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
    f.write(script)
    name = f.name
print(name)
res = subprocess.run(['node', '--check', name], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
print('EXIT', res.returncode)
os.remove(name)
sys.exit(res.returncode)
