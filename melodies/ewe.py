import os, math
from musical.theory import Note, Scale, Chord
from musical.audio import effect, playback
from timeline import Hit, Timeline
from musical.utils import notes_from_scale, extended_notes_from_scale, add_intervals_to_notes, add_random_float
import pprint, random

pp = pprint.PrettyPrinter(indent=4)

# Config vars
time = 0.0  # Keep track of current note placement time in seconds
offset = 0.0
iterations = random.randint(4, 18)
duration = 2.4287
measure_duration = 8.826
timeline = Timeline()

# Define key and scale
key_note = Note((random.choice(Note.NOTES), random.choice([2]))).note
key = Note(key_note)
scale = Scale(key, 'pentatonicmajor')
notes = extended_notes_from_scale(key.note, scale.intervals, 1)
notes_with_intervals = add_intervals_to_notes(notes)

time += 0.38 + random.uniform(0.3, 1.3)

for i in range(iterations):
  for note in enumerate(notes_with_intervals):
      n = note[1]
      timeline.add(time, Hit(Note(n[0]), measure_duration))
      timeline.add(time + 0.7, Hit(Note(n[0]).shift_up_octave(1), measure_duration))
  time += measure_duration * 2
  
  if i % 4 == 0:
    notes_with_intervals = add_intervals_to_notes(notes[::2])
    
  if i % 8 == 0:
    notes_with_intervals = add_intervals_to_notes(notes[::-1])

print("Rendering audio...")
data = timeline.render()
data = effect.tremolo(data, freq=0.7)
data = effect.shimmer_wobble(data, 0.34)
#data = effect.wah(data, (800, 2000))
data = effect.simple_delay(data, 500, 0.2, 1.77)
data = effect.reverb(data, 0.8, 0.025)

data = data * 0.85

from musical.utils import save_normalized_audio
save_normalized_audio(data, 44100, os.path.basename(__file__))

#playback.play(data)
