#Build  ML application as a package and useful for deployment

from setuptools  import find_packages,setup


HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:

    '''this will return  the list of requirements'''

    requirements=[]
    
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()

        requirements= [req.replace("\n"," ") for req in requirements.t]


        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ML_Project',
    version='0.0.1',
    author='HARSHA',
    packages=find_packages(),
    # install_requirements=['pandas','numpy','matplotlib','seaborn','seaborn'] , # if working on a simple application

    install_requirements=get_requirements('requirements.txt')
)


'''when requirements.txt runs setup.py should also run simultaneously'''