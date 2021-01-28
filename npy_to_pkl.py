import pickle
import numpy as np

def npy_to_pkl(state_file_pth, action_file_pth):
    states = np.load(state_file_pth)
    actions = np.load(action_file_pth)
    r = 1
    assert len(states) == len(actions)
    all_info = []
    for s, a in zip(states, actions):
        tup = (s, a, r, False)
        all_info.append(tup)
    
    f = open('demos_spaceinvaders.pkl', 'wb')
    pickle.dump(all_info, f)
    f.close()

if __name__ == '__main__':
    npy_to_pkl('obs_SpaceInvadersNoFrameskip-v4_seed=69_ntraj=20.npy', 'acs_SpaceInvadersNoFrameskip-v4_seed=69_ntraj=20.npy')
