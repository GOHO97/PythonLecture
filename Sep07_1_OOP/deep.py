# -*- coding:utf-8 -*-
def reward_function(params):
    speed = params["speed"]
    isOfftrack = params["is_offtrack"]
    isAllWheelsOnTrack = params["all_wheels_on_track"]
    reward = 0;
    
    if speed >= 3:
        reward += 10
        if not isOfftrack:
            reward += 10
            if not isAllWheelsOnTrack:
                reward +=50
    
    else:
        reward = 0        
    return float(reward)
        