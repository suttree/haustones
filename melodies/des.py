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
iterations = random.randint(12, 46)
timeline = Timeline()

measure_duration = 36.00
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

notes = extended_notes_from_scale(key.note, scale.intervals, 2)  

for i in range(iterations):
  timeline.add(time, Hit(Note(notes[0]).shift_down_octave(1), measure_duration))
  timeline.add(time + 0.45, Hit(Note(notes[3]).shift_down_octave(1), half_measure))

  time += half_note
  
  for j, note in enumerate(notes[::2]):
    timeline.add(time + 0.25, Hit(Note(notes[2]), duration))
    timeline.add(time + 0.33, Hit(Note(notes[0]), duration))

  time += half_note
    
  for k, note in enumerate(notes[::2]):
    timeline.add(time + 0.25, Hit(Note(notes[4]), duration))
    timeline.add(time + 0.34, Hit(Note(notes[0]), duration))

  time += half_note

  if j % 5 == 0 and i > 0:
    notes = reset()
  
  if j % 4 == 0 and i > 0:
    time -= 1.0 + math.cos(time)
    
print("Rendering audio...")
data = timeline.render(13)
data = effect.modulated_delay(data, data, 0.02, 0.7)
data = effect.shimmer(data, 0.54)
data = effect.reverb(data, 0.08, 0.9)

from musical.utils import save_normalized_audio
save_normalized_audio(data, 44100, os.path.basename(__file__))

#playback.play(data)
