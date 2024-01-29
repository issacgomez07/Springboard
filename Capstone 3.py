import time
import rtmidi


# the function call rtmidi.Midiout() creates the handler that we'll use to send midi signals
midiout = rtmidi.MidiOut()

# check and get the ports which are open
available_ports = midiout.get_ports()

# print(available_ports)

# Attempt to open the port
if available_ports:
    midiout.open_port(1) # number here should match list index

# This is how you create a midi note, the specs are: [command, note, velocity]
note_on = [0x90, 60, 112]
note_off = [0x80, 60, 0]

midiout.send_message(note_on)

#Here you need to insert a short delay before turning the note off to make sure that the note_on signal was received
time.sleep(0.5)
midiout.send_message(note_off)