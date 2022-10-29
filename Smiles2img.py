import io
from rdkit import Chem
from rdkit.Chem import Draw
import base64


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
        try:
            mols[j] = mols[j * 50:(j + 1) * 50]
            img = Draw.MolsToGridImage(mols[j], molsPerRow=5, subImgSize=(60, 60))
            # img.save('C:\\Users\\ll\Desktop\\' + str(j) + '.png')
            out = io.BytesIO()
            img.save(out, format="png")
            # imgBs64 = base64.b64encode(img.__str__().encode()).decode()
            imgBs64 = base64.b64encode(out.getvalue()).decode()
            # 错误
            # imgBs64 = base64.b64encode(img.tobytes()).decode("UTF-8")
            # print(type(img))
            print(imgBs64)
            return imgBs64
        except:
            print("第" + str(j) + "张图片显示不出来")


def smlies2ImgBs642(smis):
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
            img = Draw.MolsToGridImage(mols[j], molsPerRow=5, subImgSize=(60, 60))
            # img.save('C:\\Users\\ll\Desktop\\' + str(j) + '.png')
            out = io.BytesIO()
            img.save(out, format="png")
            return img
        except:
            print("第" + str(j) + "张图片显示不出来")
