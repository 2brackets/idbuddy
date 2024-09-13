[Setup]
AppName=ID Buddy
AppVersion=1.0.0
DefaultDirName={pf}\ID Buddy
DefaultGroupName=ID Buddy
OutputBaseFilename=setup

[Files]
Source: "dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "src\img\idbuddy.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\ID Buddy"; Filename: "{app}\main.exe"; IconFilename: "{app}\icon.ico"
Name: "{userdesktop}\ID Buddy"; Filename: "{app}\main.exe"; IconFilename: "{app}\icon.ico"; Tasks: desktopicon
