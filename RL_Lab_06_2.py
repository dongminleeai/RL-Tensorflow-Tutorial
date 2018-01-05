# CartPole를 아무것도 없이 돌려보겠습니다.

import gym

env = gym.make('CartPole-v0') # 게임을 불러옵니다.
env.reset() # 초기화를 시켜줍니다.
random_episodes = 0
reward_sum = 0
while random_episodes < 10: # 10번에 나누어서 학습을 시킵니다.
    env.render() # 초기화된 맵을 보여줍니다.
    action = env.action_space.sample() # action을 sample로 돌립니다.
    observation, reward, done, _ = env.step(action) # 각 스탭마다 action을 취했을 때의 값들을 불러옵니다.
    print(observation, reward, done)
    reward_sum += reward # 잘했을 때의 reward 받은 값들을 합칩니다.
    if done:
        random_episodes += 1 # 끝났을 때 에피소드를 1 올립니다.
        print("Reward for this episode was:", reward_sum) # 받았던 총 reward 값을 출력합니다.
        reward_sum = 0 # reward를 다시 0으로 돌립니다.
        env.reset() # 다시 초기화를 시켜줍니다.

# 밑에 보시는 것은 임의의 하나의 episode의 출력물을 가져왔습니다.

# [-0.00048771 -0.15082993 -0.04016158  0.25505349] 1.0 False
# [-0.00350431  0.04484174 -0.03506051 -0.05002168] 1.0 False
# [-0.00260747  0.24044843 -0.03606094 -0.35355707] 1.0 False
# [ 0.0022015   0.4360641  -0.04313208 -0.65738943] 1.0 False
# [ 0.01092278  0.24156824 -0.05627987 -0.37859387] 1.0 False
# [ 0.01575414  0.43744241 -0.06385175 -0.68847749] 1.0 False
# [ 0.02450299  0.24326204 -0.0776213  -0.41656015] 1.0 False
# [ 0.02936823  0.04932103 -0.0859525  -0.14932233] 1.0 False
# [ 0.03035465  0.24556191 -0.08893895 -0.46783591] 1.0 False
# [ 0.03526589  0.05180164 -0.09829567 -0.20445785] 1.0 False
# [ 0.03630193  0.24818184 -0.10238482 -0.52645863] 1.0 False
# [ 0.04126556  0.44458415 -0.112914   -0.84956789] 1.0 False
# [ 0.05015724  0.25116815 -0.12990535 -0.59441763] 1.0 False
# [ 0.05518061  0.05808077 -0.14179371 -0.3453118 ] 1.0 False
# [ 0.05634222  0.25490504 -0.14869994 -0.67913305] 1.0 False
# [ 0.06144032  0.06212731 -0.1622826  -0.43671439] 1.0 False
# [ 0.06268287  0.25912962 -0.17101689 -0.77583719] 1.0 False
# [ 0.06786546  0.06672058 -0.18653364 -0.5414681 ] 1.0 False
# [ 0.06919987  0.26390679 -0.197363   -0.88663995] 1.0 False
# [ 0.07447801  0.07193209 -0.2150958  -0.66191683] 1.0 True
# Reward for this episode was: 20.0

# 각 state마다 4가지의 실수로 표현이 되고 있습니다. 바로 observation입니다.
# 1.0은 reward를 뜻합니다.
# False는 계속 진행상태를 뜻하고, True가 되었을 때 done이 되어 종료됩니다.
# 마지막으로 'Reward for this episode was: 20.0'라는 출력물로 종료되는데, 여기서 20.0은 받았던 총 reward 값을 말합니다.
# '20번 정도했더니 넘어졌다.'라는 뜻이 됩니다.

# 각 state마다 찍히는 4가지의 실수에 대해서 설명해드리겠습니다. 각 열에 맞춘 설명입니다.
# 첫 번째로 찍히는 열(ex. '-0.00048771')은 '트랙에서의 Cart의 위치, x'를 말합니다.
# 두 번째로 찍히는 열(ex. '-0.15082993')은 '수직에서의 Pole의 각도, B'를 말합니다.
# 세 번째로 찍히는 열(ex. '-0.04016158')은 '카트의 속도, dx/dt'를 말합니다.
# 네 번째로 찍히는 열(ex. '0.25505349')은 '각도의 변화율, dB/dt'를 말합니다.

# 보통 200을 넘으면 성공이라고 하는데요. 20밖에 나오지 않네요. Q-learning을 통해 학습해보겠습니다. 