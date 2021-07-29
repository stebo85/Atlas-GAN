import numpy as np
import SimpleITK as sitk
import os

files = ['ourdata/' + f for f in os.listdir('ourdata') if f.endswith('mn_skull_stripped_rescaled-0-1.nii.gz')]

print(files)

age = np.array([29,26,23,31,34,29,21,23,22,26,24,32,25,29,25,23,23,27,23,22,29,24,27,27,29,32,23,31,24])
gender = np.array([0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1])

for i, file in enumerate(files):
    simg = sitk.ReadImage(file)

    #read and crop
    npy_img = sitk.GetArrayFromImage(simg)[0:160,0:192,0:160]
    out_file = file.replace('.nii.gz','.npz')

    np.savez_compressed(
        out_file,
        vol=npy_img,
        age=age[i],
        attribute=gender[i],
    )