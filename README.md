# Flappy-Bird-AI
![Flappy Bird AI](images/flappy_bird_ai.png)

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)

## Overview

This project implements an AI agent to play the popular Flappy Bird game using the 1-Step SARSA (State-Action-Reward-State-Action) algorithm and a 2-layer neural network as the model. The AI agent aims to learn to control the flappy bird to navigate through the pipes autonomously.

![Flappy Bird Gameplay](flappy_bird_gameplay.gif)

The 1-Step SARSA algorithm is an on-policy reinforcement learning technique used to learn the optimal action-value function in a Markov Decision Process (MDP) environment. The 2-layer neural network serves as the function approximator for the action-value function, helping the AI agent make decisions on when to flap the bird's wings.

## How it Works

The Flappy Bird AI is built using Python and PyTorch, and it follows these steps:

1. **Environment Setup**: The game environment is created using a simple game engine.

2. **Data Collection**: The AI agent interacts with the environment, observing states, taking actions, and receiving rewards. The agent collects experience data in the form of (state, action, reward, next state, next action) tuples.

3. **Feature Engineering**: The game state and action spaces are transformed into appropriate feature vectors to be used as input to the neural network.

4. **Neural Network Architecture**: The 2-layer neural network is constructed using PyTorch. The input layer takes the feature vectors, and the output layer predicts the action-values for each possible action.

5. **Training**: The AI agent uses the 1-Step SARSA algorithm to update the neural network parameters (weights and biases) by minimizing the Mean Squared Error (MSE) loss between the predicted action-values and the target action-values.

6. **Gameplay**: After training, the AI agent can autonomously play Flappy Bird by using the neural network to choose actions based on the current state.