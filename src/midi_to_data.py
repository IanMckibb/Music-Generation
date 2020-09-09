import os
from mido import MidiFile

midi_dir = "midi_files"

data_file = open("midi_data", 'w')

for filename in os.listdir(midi_dir): #Iterates over each file in midi_files directory
    if filename.endswith(".mid"):
        song = MidiFile("%s/%s" % (midi_dir, filename), clip=True)
        data_file.write("$\n") #delim for songs
        for track in song.tracks:
            for element in track:
                if (element.type == 'note_on' or element.type == 'note_off'):
                    data_file.write(str(element) + '\n')

data_file.close()