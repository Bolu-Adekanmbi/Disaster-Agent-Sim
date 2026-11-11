Disaster Agent Sim


Starting Point:
  - Represent a 2D world grid with key events happening, then figure out how to resolve all things given (time), resource constraints.
    - Roads, buildings, events
  - Might add visual representation of the world later

Some later ideas:
- Perhaps instead of doing loops to try and understand the world given a config, perhaps it might be smarter to put the info that we loop for within the file we are passing, perhaps a JSON representation rather than CSV, or the CSV has a dedicated way it should be for stating things like player start, pathways, etc. Essentially whatever we would loop for. I don't think this affects many things longer term for actually turning this into a real viable solution. The main thing that this is being used for long term is representation of disaster maps, so given a disaster, map we already have it would be a pretty bad idea to then gradually check for different things, OR perhaps there are types of disasters where we are trying to figure everything out oneshot. But I want to imagine for now that everything else like start, disaster locations, etc. are precomputed. Adding search/check for these things after should be trivial

World Key:

player: p
boundary: #
path: =
diaster: *
