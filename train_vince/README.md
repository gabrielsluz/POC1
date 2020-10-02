### How to run this code ?
Use a Singularity Container :)
- In the machine which has singularity,
mkdir train_vince
cd train_vince
git clone https://github.com/gabrielsluz/POC1.git
sudo singularity build train_vince.simg ./POC1/train_vince/Singularity

- Get into the container
singularity shell -B /datasets/:/datasets/ mnist_test.simg 
python ./POC1/gpu_test/teste_gpu.py --epochs 1

- To test on a server: **Always check everything needed
scp to the server or just get the container to the server
ssh
git clone https://github.com/gabrielsluz/POC1.git
singularity shell -B /srv/storage/datasets/gabrielsluz/:/datasets/ --nv mnist_test.simg 
python3 ./POC1/gpu_test/teste_gpu.py --epochs 1