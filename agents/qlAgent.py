import numpy as np
import pandas as pd
import pickle
import os

from agents import AbstractAgent

class QLearningAgent(AbstractAgent):
    """
    Q Learning RL agent that produces actions based on the highest Q value, computes and saves sa-pairs in a Q table
    """
    def __init__(self, state_shape, action_shape,
            learning_rate=0.1, 
            discount_factor=0.99, 
            epsilon=1.0, 
            epsilon_decay=0.995, 
            epsilon_min=0.1):
        
        super().__init__(state_shape, action_shape)
                
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        
        # TODO: create the Q table e.g. as pandas.DataFrame or 2D numpy array

        
    def get_action(self, state):
        # TODO: Implement the action selection (Hint Epsilon Greedy)
        pass
        
    def update(self, state, action, reward, next_state, done):
        # TODO: Implement the update logic
        pass
    
    
    def save_model(self, path, filename="qlagent"):
        # TODO: Make your Q Table savable - probably best way for this: Pickle it to a file
        pass
    
    @classmethod
    def load_model(cls, path, filename="qlagent"):
        # TODO: Inverse of save_model -- load the pickled file if you chose pickling
        pass
    