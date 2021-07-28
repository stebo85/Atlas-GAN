import numpy as np
import SimpleITK as sitk
import os

simg = sitk.ReadImage('/mnt/FileSystem-DeepLearning/vnm/qsm28_data/rbcscr_mean.nii.gz')
npy_img = sitk.GetArrayFromImage(simg)

np.savez_compressed(
    '/mnt/FileSystem-DeepLearning/vnm/qsm28_data/rbcscr_mean.npz',
    arr_0=npy_img,
)