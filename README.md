# Lab A Work
# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
**What I built:**
    created the cspc repository structure , set the conda enviroment , implemented decay simulation tests
**Speed comparison (loop vs NumPy):**
- loop: 1.6266 s
- numpy: 0.0003 s
- speed-up: 6175.26x faster
**Tests:** all passing? yes
**Conclusion:**
the numpy vectorized implementation significantly outperforms the pure python loop.