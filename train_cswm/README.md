### How to run this code ?
Use a Singularity Container :)
Building the container:
- In the machine which has singularity,
git clone https://github.com/gabrielsluz/POC1.git
mkdir train_cswm
cd train_cswm
sudo singularity build --sandbox train_cswm ../POC1/train_cswm/Singularity

- Running on the server:
git clone https://github.com/tkipf/c-swm.git
