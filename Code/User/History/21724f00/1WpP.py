#!/usr/bin/python
import subprocess, sys, configparser
from pathlib import Path

config_file = Path("/home/ju/.config/ytdl/config.conf")

if (config_file):
    config = configparser.RawConfigParser()
    config.read(config_file)
    MUSIC_PATH, PLAYLIST_PATH = Path(config.get('folders', 'music_folder')), Path(config.get('folders', 'playlist_folder'))
    VIDEO_PATH = Path(config.get('folders', 'video_folder'))
    AUDIO_TYPE, VIDEO_TYPE = config.get('types', 'preferred_audio_type'), config.get('types', 'preferred_video_type')
else:
    MUSIC_PATH, PLAYLIST_PATH = Path('~/'), Path('~/Playlists')
    VIDEO_PATH = Path('~/Videos')
    AUDIO_TYPE, VIDEO_TYPE = 'opus', 'mp4'

# Check if yt-dlp is already installed and if not try to install
check_installed = "pacman -Q | grep yt-dlp"
ci_shell = subprocess.Popen(check_installed, shell=True ,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
ci_output = ci_shell.communicate()[0].decode()
if ci_output == '':
    try:
        subprocess.Popen(['sudo','pacman','-S','yt-dlp'],stderr=subprocess.STDOUT)
    except Exception as e: 
        print(repr(e))
        pass

args = sys.argv[1:]

try:
    # Download whole Playlists
    if args[0] == '-p' and '&list=' in args[1]:
        print('Valid playlist URL. Downloading playlist.')
        
        # Get Playlist Title. There are probably better ways to do this though.
        get_title = f"yt-dlp --flat-playlist --skip-download -o %(playlist_title)s {args[1]}"
        get_title = get_title.split(' ')
        title = subprocess.check_output(get_title).decode().split('Finished downloading playlist: ')[1].split('\n')[0]

        # Create folder for new Playlist (Name: Playlist Title)
        new_path = PLAYLIST_PATH / title.replace(' ','-')
        new_path.mkdir(parents=True, exist_ok=True)
        print(new_path)
        
        # Do the actual file download
        cmd = f"yt-dlp -x --no-warnings -f bestaudio -o {new_path}/%(title)s.%(ext)s {args[1]}"
        cmd = cmd.split(' ')

        try:
            subprocess.call(cmd)
            print("Done downloading.")
            sys.exit()
        except Exception as e:
            print(repr(e))

    
    # Download single youtube videos or audio
    elif ('youtube.com/watch' in args[0] or 'youtube.com/watch' in args[1]) and ('&list=' not in args[0] or '&list=' not in args[1]):
        print('Valid Youtube URL. Downloading video')

        if args[0] == '-v':
            dl_path = VIDEO_PATH / '%(title)s.%(ext)s'
            if VIDEO_TYPE == 'mp4':
                format = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
                cmd = f"yt-dlp -f bestvideo -f {format} -o {dl_path} {args[1]}"
                cmd = cmd.split(' ')
        else:
            dl_path = MUSIC_PATH / '%(title)s.%(ext)s'
            if AUDIO_TYPE == 'opus':
                print(dl_path)
                cmd = f"yt-dlp -x -f bestaudio -o {dl_path} {args[0]}"
                cmd = cmd.split(' ')

            elif AUDIO_TYPE == 'mp3':
                cmd = f"yt-dlp -x -f bestaudio --audio-format mp3 -o {dl_path} {args[0]}"
        
        try:
            subprocess.call(cmd)
            print("Done downloading.")
            sys.exit()
        except Exception as e:
            print(repr(e))

except IndexError:
    print('You need to run this script with arguments')
except:
    print("Error", sys.exc_info()[0])
    raise
