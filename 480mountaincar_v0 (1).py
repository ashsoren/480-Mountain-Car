import gym 
import random 
#Create our MountainCar environment 
env = gym.make('MountainCar-v0') 
env.reset() 

def RandomAgent(): 
    
    #each episode is a game that is run to its end 
    randomAction=1
    
    for epoch in range (10): 
        
        #now we break up the frames 
        for t in range (500): 
            env.render() 

            #state = env.obversation_space
            #print(state)
            if randomAction ==1:
                action = env.action_space.sample() 
                randomAction == 0
            else:
                if next_state[1]<0:
                    if next_state[0] < -0.9:
                         action=2
                    else:
                        action = 0
                else:
                    action=2

            print (action)

            #the next state, rewards, done flag, and info are all returned 
            next_state, reward, done, info = env.step(action) 
            print(t, next_state, reward, done, info, action) 
         
            if done: 
                env.reset() 
                randomAction = 0
                break

RandomAgent()