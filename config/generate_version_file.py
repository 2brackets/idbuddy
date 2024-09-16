from version import __version__

version_info = f'''
# UTF-8
#
# Comments can be included here with the '#' symbol.
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=({__version__.replace('.', ', ')}, 0), 
    prodvers=({__version__.replace('.', ', ')}, 0),  
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          '040904b0', [
            StringStruct('CompanyName', '2brackets.com'),
            StringStruct('FileDescription', 'Description of your application'),
            StringStruct('FileVersion', '{__version__}'),
            StringStruct('InternalName', 'idBuddy'),
            StringStruct('LegalCopyright', '© 2brackets.com. All rights reserved.'),
            StringStruct('OriginalFilename', 'idBuddy.exe'),
            StringStruct('ProductName', 'idBuddy'),
            StringStruct('ProductVersion', '{__version__}'),
          ]
        )
      ]
    ),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
'''

with open("version.txt", "w", encoding="utf-8") as version_file:
    version_file.write(version_info)

print(f'Version file generated successfully for version {__version__}')
