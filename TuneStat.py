import os
import sys
import lyricsgenius as genius
from tinytag import TinyTag
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TALB, TPE1, TPE2, COMM, USLT, TCOM, TCON, TDRC
import datetime



def getInfoArtists(pathSong, artistsCollection):
	try:
		metadata = TinyTag.get(pathSong)

		if(not metadata.artist in artistsCollection.keys()):
			artistsCollection[metadata.artist] = {}

		if(not metadata.album in artistsCollection[metadata.artist].keys()):
			artistsCollection[metadata.artist][metadata.album]={
				"genre":metadata.genre,
				"date":metadata.year[0:4] if metadata.year!=None else None,
				"nrOfSongs": 1 ## starts from 1 cause we're scanning songs (so the first one creates the entry and counts itself)
			}
		else:
			artistsCollection[metadata.artist][metadata.album]["nrOfSongs"] += 1

		return artistsCollection
	except Exception as e:
		print(e)
		return None


def showStats(artistsCollection):
	for i in artistsCollection.keys():
		print(i)
		print("Nr of albums:",len(artistsCollection[i].keys()))
		for j in artistsCollection[i]:
			print(artistsCollection[i][j])
'''
Future
Nr of albums: 10
{'genre': 'Hip-Hop/Rap', 'date': '2012', 'nrOfSongs': 16}
{'genre': 'Hip Hop, Trap', 'date': '2015', 'nrOfSongs': 8}
{'genre': 'Hip-Hop / Rap', 'date': '2016', 'nrOfSongs': 1}
{'genre': 'Hip-Hop', 'date': '2017', 'nrOfSongs': 17}
{'genre': 'Hip-Hop/Rap', 'date': None, 'nrOfSongs': 18}
{'genre': 'Hip-Hop / Rap', 'date': '2020', 'nrOfSongs': 21}
{'genre': 'Hip-Hop / Rap', 'date': '2016', 'nrOfSongs': 1}
{'genre': 'Hip-Hop/Rap', 'date': '2022', 'nrOfSongs': 22}
{'genre': 'Hip-Hop / Rap', 'date': '2019', 'nrOfSongs': 1}
{'genre': 'Hip Hop, Trap', 'date': '2017', 'nrOfSongs': 17}
'''


def main(path):
	dictSongs = {
		"numSongs":0,
	}
	artistsCollection ={

	}
	for root, directories, files in os.walk(path, topdown=True):
			for name in files:
				pathTmp=str(os.path.join(root, name))	
				if(pathTmp.endswith(".m4a") or pathTmp.endswith(".mp3")):
					dictSongs["numSongs"]+=1
					getInfoArtists(pathTmp, artistsCollection)


	showStats(artistsCollection)




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