import base64
import io
# sys.path.append('/home/li/.conda/envs/li/lib/python3.7/site-packages')
import django.http
import matplotlib.pyplot as plt
import matplotlib.image as mimage
import matplotlib.cbook as cbook
# datafile = cbook.get_sample_data('logo2.png', asfileobj=False)
# im = mimage.imread(datafile)
from django.http.response import HttpResponse
from rdkit import Chem
from rdkit.Chem import Draw

smis = ['CN1C=NC2=C1C(=O)N(C(=O)N2C)C']
fig, ax = plt.subplots(figsize=(5.,5.))


def smlies2Img(smis):
    # for i in open ("/home/li/draw_molecule_picture/moses2_smiles.txt"):
    #     smis.append(i)

    mols = []
    for smi in smis:
        mol = Chem.MolFromSmiles(smi)
        mols.append(mol)

    for j in range(1):
        print(j)
        # output picture
        try:
            mols[j] = mols[j * 50:(j + 1) * 50]
            img = Draw.MolsToGridImage(mols[j], molsPerRow=5, subImgSize=(300, 300))
            img.save('C:\\Users\\ll\Desktop\\' + str(j) + '.png')
        except:
            print("第" + str(j) + "张图片显示不出来")


def smlies2ImgBs64(smis):
    # for i in open ("/home/li/draw_molecule_picture/moses2_smiles.txt"):
    #     smis.append(i)

    mols = []
    for smi in smis:
        mol = Chem.MolFromSmiles(smi)
        mols.append(mol)

    for j in range(1):
        print(j)
        # output picture
        # try:
        mols[j] = mols[j * 50:(j + 1) * 50]
        img = Draw.MolsToGridImage(mols[j], molsPerRow=5, subImgSize=(50, 300))

        # 居中
        myaximage = ax.imshow(img,
                              aspect='auto',
                              extent=(20, 80, 120, 180),
                              alpha=0.5)
        plt.show()
        # img.save('C:\\Users\\ll\Desktop\\' + str(j) + '.png')
        out = io.BytesIO()
        img.save(out, format="png")
        # imgBs64 = base64.b64encode(img.__str__().encode()).decode()
        imgBs64 = base64.b64encode(out.getvalue()).decode()
        print(type(img))
        print(imgBs64)
        return imgBs64
        # except:
        #     print("第" + str(j) + "张图片显示不出来")


if __name__ == "__main__":
    # smlies2Img(smis)
    smlies2ImgBs64(smis)
