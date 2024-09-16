from version import __version__

spec_content = f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

version_file = 'version.txt' 

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('src/img/idbuddy.ico', 'src/img'),  
        ('src/img/idbuddy_logo.png', 'src/img'), 
        ('src/img/2brackets.png', 'src/img')  
    ],
    hiddenimports=['PIL'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='idBuddy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='src/img/idbuddy.ico',
    version=version_file, 
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='idBuddy'
)
"""

with open('main.spec', 'w', encoding="utf-8") as spec_file:
    spec_file.write(spec_content)

print(f'Spec file generated successfully for version {__version__}')
