import numpy as np
import argparse
import os
import sys
sys.path.insert(0, os.path.abspath("../ml-agents/python/"))
from unityagents import UnityEnvironment

parser = argparse.ArgumentParser(description='Unity Env Test')
parser.add_argument('-e', '--env-name', default='../envs/pyenv',
                    help='environment path')
args = parser.parse_args()

env = UnityEnvironment(file_name=args.env_name)
default_brain = env.brain_names[0]
brain = env.brains[default_brain]
print('Loaded environment from: %s' % args.env_name)
print(str(env))
print('action space size per limb = ', brain.action_space_size)
print('state space size per limb = ', brain.state_space_size)
train_mode = False

# joinDist means merge action
# forceScale means scale torque in the environment
# autoJoin is to join automatically if dist <= joinDist else via merge action
expID = 0.0
saveEnv = 0.0
loadEnv = 0.0
env_config = {"maxLimb": 7, "joinDist":4.0, "forceScale":10.0,
    "autoJoin": 0.0, "dynamicFriction":0.6, "staticFriction":0.6,
    "saveEnv":saveEnv, "loadEnv":loadEnv, "expID":expID}
if saveEnv != 0.0:
    print('EnvData Save dir: ./SaveData/%05d/%05d.dat' % (expID, saveEnv))
if loadEnv != 0.0:
    print('EnvData Load dir: ./SaveData/%05d/%05d.dat' % (expID, loadEnv))
if 'multiagent_N' in args.env_name:
    env_config["N"] = 8
print('Env config:', env_config)

for episode in range(10):
    print('='*60)
    env_info = env.reset(train_mode=train_mode, config=env_config)[default_brain]
    print('Starting Episode: %d' % (episode+1))
    if "N" in env_config:
        env_config["N"] = 0  # to add only once
    done = False
    episode_rewards = 0
    for i in range(100):
        if brain.action_space_type == 'continuous':
            act = np.random.randn(len(env_info.agents), brain.action_space_size)
        else:
            act = np.random.randint(0, brain.action_space_size,
                                                  size=(len(env_info.agents)))
        env_info = env.step(act)[default_brain]
        episode_rewards += env_info.rewards[0]
    print("Total reward this episode: {}".format(episode_rewards))

env.close()
