### How to run this code ?
Use a Singularity Container :)
- In the machine which has singularity,
mkdir train_vince
cd train_vince
git clone https://github.com/gabrielsluz/POC1.git
sudo singularity build --sandbox train_vince ./POC1/train_vince/Singularity

- Clone forked vince and get into the container
git clone https://github.com/gabrielsluz/vince.git
singularity shell -B /storage_path/:/datasets/ --nv /container_path/train_vince.simg
chmod +x ./vince/vince/train_mmnist.sh
cd ./vince
./vince/train_mmnist.sh
