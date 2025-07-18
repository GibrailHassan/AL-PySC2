import sys
from absl import flags

from agents.reinforceAgent import REINFORCEAgent, DeepREINFORCEAgent
from env.env_discrete import MoveToBeaconDiscreteEnv
from env.env_full import MoveToBeaconEnv
from runner.runner import Runner

# pysc2 routine, do not touch
FLAGS = flags.FLAGS
FLAGS(sys.argv)

# here define your run configs

# fullenv = MoveToBeaconEnv(
#     distance_range=8,
#     screen_size=16,
#     step_mul=8,
#     is_visualize=False
# )

env = MoveToBeaconDiscreteEnv(
    distance_discrete_range=10,
    distance=1,
    screen_size=32,
    step_mul=8,
    is_visualize=False
)

agent = REINFORCEAgent(
    state_shape=env.state_shape,
    action_shape=env.action_shape
)

runner = Runner(
    agent=agent,
    env=env,
    save_model_each_episode_num=-1
)

runner.run(1000)