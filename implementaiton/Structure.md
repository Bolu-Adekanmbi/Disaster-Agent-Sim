# Phase 1

Right now the idea I have is this:

We have a simulator class that is in charge of running the simulation.

Within the simulator class we have a World class that is in charge of the current representation of the world, and an Agent class that represents the player/agent that is trying to resolve the situation.

---

The agent class has its own set of rules/thinking, and the agent in particular has a method called something like next_step/move and the idea is that the agent observes the world (~not sure if to give it the whole world, or just a part that it can see~, perhaps these are 2 different approaches for evaluating the agent's performance based on partial vs fully known world) and uses that to determine it's next course of action.

Right now: the agent is given the whole world, and it can see everything (will be helpful for agents that consider everything)

This branches out into two types of disaster response situations: full visibility vs partial visibility. These are 2 separate scenarios that are applicable to real life

Move class?
--
The agent might need a move class? Instead of just returning a string, it would be helpful to be able to have moves like that translate the location of the agent (for now one step movement in the grid), actions that can be taken in the current grid locaiton, and modiiers that can be applied to moves such as the magnitude (amount of movement to do in specific direction), the amount of a particular step to take, etc. In the future I can include more complex moves like pathfinding to a particular entity/location, carrying things, etc.

Moves (for now): <-- focus is just getting to a particular location, so the moves are just simple movement in the grid
- up, down, left, right (no turning or diagonal movement just yet)

---
The simulator class is then in charge of taking the agent's next step and applying it to the world, and then updating the world state based on the agent's decision. 

The simulator class should have the ability to run 1 step, or continuously run either till the scenario is resolved, or the agent no longer has any valid moves to make.

The simulator class should keep track of the number of moves the agent has made as well.

Simulator class ideas:
- go back (revert world state to previous state)
- figuring out when the agent is going to go in a loop (perhaps using an algorithm to detect cycles in the world state/agent move <- especially when the agent is deterministic and doesn't have either randomness or memory of previous search paths to inspire informed change in decision-making)
- store multiple agents and run all their next steps (so this is longer term interaction between multiple agents and potentially the ability to work together)
- running multiple worlds with the same agent to evaluate performance of the agent across different scenarios **OR** running multiple agents with the same world to evaluate performance of different agents on the same scenario
- Simulate class might have some benchmarking capabilities or maybe I should make that a separate class that is in charge of benchmarking the agent's performance but can call the simulator class in different cotexts (specifications like number of agents, etc.)
- Benchmarking might also be important for evaluating agents that are non-deterministic and we can run multiple simulations to see how well they perform on average, or if they are able to resolve the scenario at all.

---

The world class just has a current representation of the world (right now array representation but might switch to a tree structure/nodes and have the world class build the node tree, with each state/place for the agent being its own object thing where we can call methods directly on the node/state)

The world class should definitely store information regarding player position, disaster locations, start, etc. Especially since the simulator class might have multiple worlds, so it's better that the World class owns this info.

The world class should also be able to respond whether or not it is solved. So the simulator class can call the is_solved method of the world class to determine if the agent has resolved things, whether to take another step, or if there are no more valid moves to make.

World class should also be able to be updated based on the agent's next step. So the simulator class may run something like next_step, but within that we have something like world.update(agent.next_step()) to update the world state based on the agent's decision.
