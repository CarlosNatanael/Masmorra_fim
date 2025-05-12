# -*- mode: python ; coding: utf-8 -*-
# pyinstaller masmorra.spec

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Niveis
        ('models/nivel1.py', 'models'),
        ('models/nivel2.py', 'models'),
        ('models/nivel3.py', 'models'),
        ('models/nivel4.py', 'models'),
        ('models/nivel5.py', 'models'),
        ('models/nivel6_1.py', 'models'),
        ('models/nivel6_2.py', 'models'),
        ('models/nivel6_3.py', 'models'),
        ('models/nivel7_h.py', 'models'),
        ('models/nivel7_s.py', 'models'),
        ('models/nivel8.py', 'models'),
        ('models/nivel9.py', 'models'),
        ('models/nivel9_s.py', 'models'),

        # Musicas
        ('game_sound_py/game_over.py', 'game_sound_py'),
        ('game_sound_py/menu_sound.py', 'game_sound_py'),
        ('game_sound_py/sound1.py', 'game_sound_py'),
        ('game_sound_py/sound2.py', 'game_sound_py'),
        ('game_sound_py/sound3.py', 'game_sound_py'),
        ('game_sound_py/sound4.py', 'game_sound_py'),
        ('game_sound_py/sound5.py', 'game_sound_py'),
        ('game_sound_py/sound6_1.py', 'game_sound_py'),
        ('game_sound_py/sound6_2.py', 'game_sound_py'),
        ('game_sound_py/sound6_3.py', 'game_sound_py'),
        ('game_sound_py/sound7.py', 'game_sound_py'),
        ('game_sound_py/sound8.py', 'game_sound_py'),
        ('game_sound_py/sound9.py', 'game_sound_py'),

        # Utilirios
        ('utils/combate.py', 'utils'),
        ('utils/creditos.py', 'utils'),
        ('utils/personagem.py', 'utils'),
        ('utils/utils.py', 'utils'),

        # Pegando as imagens e txt da conquistas_imag
        ('conquistas_imag/*.png', 'conquistas_imag'),
        ('conquistas_imag/__init__.py', 'conquistas_imag'),
        ('conquistas_imag/conquista.py', 'conquistas_imag'),
        ('conquistas_imag/sistema_conquistas.py', 'conquistas_imag'),
        ('conquistas_imag/*.txt', 'conquistas_imag'),

        # Pegando as músicas
        ('sound/*.mp3', 'sound'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Masmorra do Fim',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Se quiser tirar o console, mudar pra False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icone.ico',
)
