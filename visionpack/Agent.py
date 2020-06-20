from stable_baselines3 import PPO
import numpy as np
from random import randint
import subprocess
from PIL import Image

subprocess.call('echo 1 > /proc/sys/vm/overcommit_memory', shell=True)

#use the saved model to form an agent
class Agent:

    def __init__(self):
        self.name = "PPOAgent"
        # self.x = np.zeros((2048,1,150,270))
        # raise Exception('did not won over loading yo')
        self.model1 = PPO.load("./best_model_gold_digger_lvl0.pkl")
        self.model2 = PPO.load("./best_model_treasurekeeper_lvl0.pkl")
        # raise Exception('won over loading yo')

    def act(self, stateObs, actions):
        # stateObs = stateObs[0][0]
        # stateObs = stateObs.reshape(150,270,4)
        if (stateObs.shape == (150,270,4)):
        	action, _states = self.model1.predict(stateObs[:,:,2])
        elif (stateObs.shape == (90,130,4)):
        	action, _states = self.model2.predict(stateObs[:,:,2])
        else:
        	action = randint(0,len(actions)-1)

        return action