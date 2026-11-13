Disaster Agent Sim

Right now:
One player to One world (duplicate worlds for multiple players to try and resolve same disaster config/scenario) <- that way I don't really have to start thinking about parallel world states existing for the same world.

Although this does beg the question about what would happen if we want multiple agents to play in the same world and interact with each other, so rather than having multiple states of the same world that exist in parallel (which really is just a waste to try and manage <- I don't see any computational benefits to this for now < passing thought), we would keep 1 state where agents have to employ strategies to work together to resolve the disaster.

Starting Point:
  - Represent a 2D world grid with key events happening, then figure out how to resolve all things given (time), resource constraints.
    - Roads, buildings, events
  - Might add visual representation of the world later

Fix later (not the biggest priority right now):
 - Current config doesn't have proper try/catch for when the config is not valid, or if the file doesn't exist or is not readable. This should be added later, but for now, I am just going to assume that the config is valid and exists.

Some later ideas:
- Perhaps instead of doing loops to try and understand the world given a config, perhaps it might be smarter to put the info that we loop for within the file we are passing, perhaps a JSON representation rather than CSV, or the CSV has a dedicated way it should be for stating things like player start, pathways, etc. Essentially whatever we would loop for. I don't think this affects many things longer term for actually turning this into a real viable solution. The main thing that this is being used for long term is representation of disaster maps, so given a disaster, map we already have it would be a pretty bad idea to then gradually check for different things, OR perhaps there are types of disasters where we are trying to figure everything out oneshot. But I want to imagine for now that everything else like start, disaster locations, etc. are precomputed. Adding search/check for these things after should be trivial

- Ideas of better abstraction: should I potentially create a separate Solver class, then separate the World class from the Agent class as a whole so that the World and Agent classes are parameters that go into the Solver class which will be in charge of actually running experiments. This could also be useful for having one Solver Class that has multiple Agents and one World and then runs the Agent-World pairings, and saves all solutions within one class/representation?

> ^ _Right now though, the Agent Class is acting as an attribute of the world under "player"_

- Another future idea is creating the Disaster Class (should it be separate from World?) where we specify things like the nature of the disaster, some unique characteristics such as spread from each turn (e.g. wildfire), probability spread, susceptibility maps, etc. Essentially just adding more information about how our disaster develops beyond just a static disaster that we are trying to get to. Even live earthquakes which have multi-scene spread/regions that it affects

- Another idea is choosing between whether or not the next step action is separated to the Agent Class itself or if it is just a part of the World Class. So the choice is between given the agent some knowledge of what moves can I make next, vs the World asking what next states is possible for me to achieve based on what my particular agent can do. However, since I'm thinking that strategy should be based on the Agent it could be better to just have the Agent be the one that makes the choice based on its own programming.

^-- Nedd to check over some of these over the weekend, and make sure that I have everything consolidated

---

World Key:

player: p
boundary: #
path: =
diaster: *
