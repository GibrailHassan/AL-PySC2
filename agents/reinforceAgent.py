import numpy as np
import pickle
import os
import torch
from torch import nn

from agents.abstractAgent import AbstractAgent

class REINFORCEAgent(AbstractAgent):
    """
    The simple policy gradient method based on Monte Carlo methods called REINFORCE that uses gradient of the policy to update its parameters.
    """
    def __init__(self, state_shape: tuple[int,...], action_shape: tuple[int,...], learning_rate: float=0.01, discount_factor: float=0.99):
        super().__init__(state_shape, action_shape)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.policy = None

    def get_action(self, state: np.ndarray):
         # TODO: Sample action
        pass

    def update(self, state: np.ndarray, action: int, reward: float, next_state: np.ndarray, done: bool):
        # TODO: Update the policy
        pass
    
    def save_model(self, path, filename: str="reinforceagent"):
         # TODO: Store the parameters and hyperparameters
        pass

    @classmethod
    def load_model(cls, path, filename: str="reinforceagent"):
        # TODO: Load the parameters and hyperparameters
       pass

class DeepREINFORCEAgent(AbstractAgent):
    """
    Deep-version of REINFORCE algorithm: it uses a neural network as a function approximator for the policy.
    That idea is the absolute base for the top modern DRL policy-based algorithms like SAC or PPO.
    """
    def __init__(self, state_shape: tuple[int,...], action_shape: tuple[int,...], learning_rate: float=0.01, discount_factor: float=0.99):
        super().__init__(state_shape, action_shape)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
   

    def get_action(self, state: np.ndarray):
        # TODO: Sample action
        pass

    def update(self, state: np.ndarray, action: int, reward: float, next_state: np.ndarray, done: bool):
        # TODO: Update the policy
        pass

    def save_model(self, path, filename: str="reinforce.pt"):
        # TODO: Store the parameters and hyperparameters
        pass

    @classmethod
    def load_model(cls: AbstractAgent, path, filename: str="reinforce.pt", reset_timesteps: bool=False):
       # TODO: Load the parameters and hyperparameters
       pass