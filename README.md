# Stateful smart contract assignment
In this assignment, you will be tasked to complete stateful smart contract for a game. When the contract is deployed, a monster with a fixed amount of health is created. Participating accounts can repeatedly attack the monster till it dies. The account that does the most damage gets rewarded with Algos. 

## Stateful contract
Complete the code in `game_approval.py`. The smart contract should contain the following functions,

### Initialization
Creates a new monster with a specified amount of health (e.g. 5 to 50). The monster must have at least 5 health points. Also initialize the global state of the maximum damage dealt to 0. You should also prevent the player from making multiple opt in transactions.

### Attack monster
Reduces the monster's health by 2 if the monster's health is not 0. Contract will keep track of the player that does the most damage to that monster, as well as the maximum damage dealt. The player's local state should also keep track of the damage dealt to that monster.

### Reward player
Send 1 Algos to the player that does the most damage if the monster is dead. This function can only be accessed by the creator.

## Contract deployment
Complete the code in `scripts/deploy_game.js` to deploy contract and fund it with 1.1 Algos.

## Calling the smart contract

### Opt-In
Complete the code in `scripts/actions/optIn.js` so that `acc1` is able to participate as a game player.

### Attack
Complete the code in `scripts/actions/attack.js` so that `acc1` can peform an application call to perform attacks on the monster.

### Reward
Complete the code in `scripts/actions/reward.js` so that the smart contract can dispense reward to the player that does the most damage.

## Hints
1. The recipient of an inner transaction must be in the accounts array. This means that you will need to get the best player's address from the global state, process it (because it returns as base64 format) and pass it into the accounts array when rewarding the player.

## Setup instructions

### Install python packages via AlgoKit
run `algokit bootstrap poetry` within this folder

### Install JS packages
run `yarn install`

### Update environement variables
1. Copy `.env.example` to `.env`
2. Update Algorand Sandbox credentials in `.env` file
3. Update accounts in `.env` file

### Initialize virtual environment
run `poetry shell`

### Compile Contracts
1. run `python game_approval.py`
2. run `python game_clearstate.py`