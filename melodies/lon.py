# Je n'est vivre

import os, math, time
from musical.theory import Note, Scale, Chord
from musical.audio import effect, playback
from timeline import Hit, Timeline
from musical.utils import notes_from_scale, extended_notes_from_scale, add_intervals_to_notes, add_random_float
import pprint, random

pp = pprint.PrettyPrinter(indent=4)

# Config vars
increment = random.uniform(0.2, 0.82) + math.cos(time.time()) * math.sin(0.19750)
time = 0.0  # Keep track of current note placement time in seconds
offset = 0.25
iterations = random.randint(12, 146)
timeline = Timeline()

measure_duration = 84.00
half_measure = measure_duration/2
duration = measure_duration/4
whole_note = duration
three_quarter_note = duration * 0.75
half_note = duration/2
quarter_note = duration/4
eighth_note = duration/8
sixteenth_note = duration/16

# Define key and scale
key_note = Note((random.choice(Note.NOTES), random.choice([0,2,4]))).note
key = Note(key_note)

scales = ['major', 'mixolydian', 'phrygian', 'augmented', 'augmentedfifth', 'melodicminor']

r_scale = random.choice(scales)
scale = Scale(key, r_scale)
notes = extended_notes_from_scale(key.note, scale.intervals, 2)
notes_with_intervals = add_intervals_to_notes(notes)

def reset():
  key_note = Note((random.choice(Note.NOTES), random.choice([2,3]))).note
  key = Note(key_note)
  r_scale = random.choice(scales)
  scale = Scale(key, r_scale)
  notes = notes_from_scale(key.note, scale.intervals)
  return notes

pp.pprint(key)
pp.pprint(r_scale)

time += sixteenth_note + random.uniform(0.2, 0.8)

intervals = [-4, -3, -2, 2, 3, 4]

notes = extended_notes_from_scale(key.note, scale.intervals, 2)  

for i in range(iterations):
  if i < 4:
    timeline.add(time + eighth_note, Hit(Note(notes[0]), duration))
  elif i < 8:
    timeline.add(time + eighth_note, Hit(Note(notes[0]), duration))
    timeline.add(time + eighth_note, Hit(Note(notes[2]), duration))
  elif i < 12:
    timeline.add(time + eighth_note, Hit(Note(notes[2]), duration))
    timeline.add(time + eighth_note, Hit(Note(notes[3]), duration))
  elif i < 16:
    timeline.add(time + eighth_note, Hit(Note(notes[4]), duration))
  elif i < 20:
    for j, note in enumerate(notes[::-3]):
      timeline.add(time + 0.2 * j*i, Hit(Note(notes[0]), duration))
      timeline.add(time + 0.2 * j*i, Hit(Note(note), duration))

  #elif i < 40:
  #  timeline.add(time + eighth_note, Hit(Note(notes[0]), duration))
  #  timeline.add(time + eighth_note, Hit(Note(notes[3]), duration))
  #  time += 0.025
  
  time += 1.025

print("Rendering audio...")
data = timeline.render()

from musical.utils import save_normalized_audio
save_normalized_audio(data, 44100, os.path.basename(__file__))

#playback.play(data)