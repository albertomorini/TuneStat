import os
import sys
import lyricsgenius as genius
from tinytag import TinyTag
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC




def getInfoSong(pathSong, artist):
	try:
		metadata = TinyTag.get(pathSong)

		if(not metadata.artist in artist.keys()):
			artist[metadata.artist] = {}

		if(not metadata.album in artist[metadata.artist].keys()):
			#print(metadata)
			artist[metadata.artist][metadata.album]={
				"genre":metadata.genre,
				"date":metadata.year,
				"nrOfSongs": 1 ## starts from 1 cause we're scanning songs (so the first one creates the entry and counts itself)
			}
		else:
			artist[metadata.artist][metadata.album]["nrOfSongs"] += 1

		return artist
	except Exception as e:
		print(e)
		return None


def main(path):
	dictSongs = {
		"numSongs":0,
	}
	artists ={

	}
	for root, directories, files in os.walk(path, topdown=True):
			for name in files:
				pathTmp=str(os.path.join(root, name))	
				if(pathTmp.endswith(".m4a") or pathTmp.endswith(".mp3")):
					dictSongs["numSongs"]+=1
					getInfoSong(pathTmp, artists)


	print(artists)




main("/Volumes/MEDIA/MUSIC/Music/Future/")



'''
{'Future': 
	{
	'Pluto': {'genre': 'Hip-Hop/Rap', 'date': '2012-04-17T07:00:00Z'}, 
	'Beast Mode': {'genre': 'Hip Hop, Trap', 'date': '2015'}, 
	'EVOL': {'genre': 'Hip-Hop / Rap', 'date': '2016-02-06T08:00:00Z'}, 
	'HNDRXX': {'genre': 'Hip-Hop', 'date': '2017'}, 
	'Honest (Deluxe)': {'genre': 'Hip-Hop/Rap', 'date': None}, 
	'High Off Life': {'genre': 'Hip-Hop / Rap', 'date': '2020-05-15T07:00:00Z'}, 
	'Wicked - Single': {'genre': 'Hip-Hop / Rap', 'date': '2016-04-13T07:00:00Z'}, 
	'I NEVER LIKED YOU': {'genre': 'Hip-Hop/Rap', 'date': '2022-04-29T07:00:00Z'}, 
	'Crushed Up - Single': {'genre': 'Hip-Hop / Rap', 'date': '2019-01-04T08:00:00Z'}, 
	'Future': {'genre': 'Hip Hop, Trap', 'date': '2017'}
	}
}
'''