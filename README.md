This project is used for the **[Generic Video Game Competition (GVGAI)](http://www.gvgai.net/) Learning Competition** from the year 2019. For more about the competition legs, rules and rank, please visite the [AI in Games website](http://www.aingames.cn/), maintained by [Hao Tong](https://github.com/HawkTom) and [Jialin Liu](https://github.com/ljialin). 

# Disclamer

This project is forked from [GVGAI Gym](https://github.com/rubenrtorrado/GVGAI_GYM), which is an [OpenAI Gym](gym.openai.com) environment for games written in the [Video Game Description Language (VGDL)](http://www.gvgai.net/vgdl.php), including the GVGAI framework. 

Please refer to the paper [Deep Reinforcement Learning for General Video Game AI](https://arxiv.org/abs/1806.02448) for more about the GVGAI GYM framework and some initial results of Reinforcement Learning (RL) agents. This paper should be cited if code from this project or the [original GVGAI GYM project](https://github.com/rubenrtorrado/GVGAI_GYM) is used in any way:

```
@inproceedings{torrado2018deep,
  title={Deep Reinforcement Learning for General Video Game AI},
  author={Torrado, Ruben Rodriguez and Bontrager, Philip and Togelius, Julian and Liu, Jialin and Perez-Liebana, Diego},
  booktitle={Computational Intelligence and Games (CIG), 2018 IEEE Conference on},
  year={2018},
  organization={IEEE}
}
```

# GVGAI Learning Competition in 2020

Two competition legs at IEEE CoG2020 and PPSN2020:
http://www.aingames.cn/gvgai/ppsn_cog2020

# Latest Updates 

* **2020.3.24:**  We have fixed a bug in the game logic file [treasurekeeper.txt](https://github.com/SUSTechGameAI/GVGAI_GYM/blob/master/gym_gvgai/envs/games/treasurekeeper_v0/treasurekeeper.txt) . Please use the newly updated version. 
* **2020.3.4:**   The map of **level1** in game waterpuzzle has been changed to the same size as **level0**


# Installation

**Way 1: using Docker**

Please refer to the step-by-step [guidelines](https://github.com/SUSTechGameAI/GVGAI_GYM/blob/master/docs/Guidelines-Docker-GVGAI-RLbaselines.md) for setting up the framework and RL baselines with Docker (using GPU or CPU only).

**Way 2: git clone** 
  * Clone this repository to your local machine
  * Run ```pip install -e <package-location>``` to install the package
  * Install a Java compiler(e.g. ```sudo apt install openjdk-9-jdk-headless```)
  
# Requirements

* **Anaconda:**　The version published after 2019.10 is recomended 
* **Java:**　JDK 9 is recommended
* **Python:**　The version Python3 (3.6 or 3.7 are recomended) is acceptable. (**Python2 can't be used!!!**)

# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/SUSTechGameAI/GVGAI_GYM.

# Resources

[GVGAI website](http://www.gvgai.net)

[original GVGAI-Gym (master branch)](https://github.com/rubenrtorrado/GVGAI_GYM) 

[Demo video on YouTube](https://youtu.be/O84KgRt6AJI)

[AI in Games website for more about competition updates](http://www.aingames.cn/#sources)

[*Deep Reinforcement Learning for General Video Game AI*](https://arxiv.org/abs/1806.02448) published at IEEE CIG2018

# References

1. [G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba, “Openai gym,” 2016.](https://github.com/openai/gym)
2. [A. Hill, A. Raffin, M. Ernestus, A. Gleave, A. Kanervisto, R. Traore, P. Dhariwal, C. Hesse, O. Klimov, A. Nichol, M. Plappert, A. Radford, J. Schulman, S. Sidor, and Y. Wu, “Stable baselines,” https://github.com/hill-a/stable-baselines, 2018.](https://github.com/hill-a/stable-baselines)
3. [R. R. Torrado, P. Bontrager, J. Togelius, J. Liu, and D. Perez-Liebana, “Deep reinforcement learning for general video game ai,” in Computational Intelligence and Games (CIG), 2018 IEEE Conference on. IEEE,
   2018.](https://github.com/rubenrtorrado/GVGAI_GYM)
