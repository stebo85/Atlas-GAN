conda activate atlas-GAN
export CUDA_VISIBLE_DEVICES=0
python train_script.py --name test-qsm --dataset qsm --nonorm_reg --clip --losswt_gp 5e-4 --gen_config ours
