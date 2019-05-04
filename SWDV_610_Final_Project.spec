# -*- mode: python -*-

block_cipher = None


a = Analysis(['SWDV_610_Final_Project.py'],
             pathex=['C:\\Users\\HPelite800G1\\Documents\\GitHub\\Maryville-SWDV-610-week-8-final-project-jmsfrancies'],
             binaries=[],
             datas=[],
             hiddenimports=['graphics.py'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='SWDV_610_Final_Project',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='SWDV_610_Final_Project')
