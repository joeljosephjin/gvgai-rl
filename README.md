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


# Installation

## Way 1: using Docker
### CPU only
Please refer to the file ``[Guidelines-Docker-GVGAI-RLbaselines.md](https://github.com/HawkTom/Notes/blob/master/Guidelines-Docker-GVGAI-RLbaselines.md)`` for setting up the framework and RL baselines using Docker.
### GPU
Please refer to the file ``[Guidelines-Docker-GVGAI-RLbaselines-GPU.md](https://github.com/HawkTom/Notes/blob/master/Guidelines-Docker-GVGAI-RLbaselines-GPU.md)`` for setting up the framework and RL baselines using Docker.

## Way 2: 
Install GVGAI GYM following the instructions provided by the [original GVGAI GYM project](https://github.com/rubenrtorrado/GVGAI_GYM).

# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/SUSTechGameAI/GVGAI_GYM.

# Resources

[GVGAI website](http://www.gvgai.net)

[original GVGAI-Gym (master branch)](https://github.com/rubenrtorrado/GVGAI_GYM) 

[Demo video on YouTube](https://youtu.be/O84KgRt6AJI)

[AI in Games website for more about competition updates](http://www.aingames.cn/#sources)

[*Deep Reinforcement Learning for General Video Game AI* published at IEEE CIG2018](https://arxiv.org/abs/1806.02448)

# References

1. [G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman, J. Tang, and W. Zaremba, “Openai gym,” 2016.](https://github.com/openai/gym)
2. [A. Hill, A. Raffin, M. Ernestus, A. Gleave, A. Kanervisto, R. Traore, P. Dhariwal, C. Hesse, O. Klimov, A. Nichol, M. Plappert, A. Radford, J. Schulman, S. Sidor, and Y. Wu, “Stable baselines,” https://github.com/hill-a/stable-baselines, 2018.](https://github.com/hill-a/stable-baselines)
3. [R. R. Torrado, P. Bontrager, J. Togelius, J. Liu, and D. Perez-Liebana, “Deep reinforcement learning for general video game ai,” in Computational Intelligence and Games (CIG), 2018 IEEE Conference on. IEEE,
   2018.](https://github.com/rubenrtorrado/GVGAI_GYM)
