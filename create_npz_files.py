import numpy as np
import SimpleITK as sitk
import os

files = ['ourdata/' + f for f in os.listdir('ourdata') if f.endswith('mn_skull_stripped_rescaled-0-1.nii.gz')]

target_path='/mnt/FileSystem-DeepLearning/vnm/qsm28_data/train_npz/'

if not os.path.exists(target_path):
    os.mkdir(target_path)

for file in files:
    simg = sitk.ReadImage(file)
    npy_img = sitk.GetArrayFromImage(simg)
    out_file = file.replace('.nii.gz','.npz')

    np.savez_compressed(
        out_file,
        vol=npy_img,
    )