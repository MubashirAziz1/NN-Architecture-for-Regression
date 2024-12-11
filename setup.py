from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_req(filepath):
    req = []
    with open(filepath) as file_obj:
        req = file_obj.readlines()
        req = [r.replace('\n','') for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)
    
    return req


setup(
name='NN_Regression',
version='0.0.1',
author = 'mubashir',
author_email = 'cs.mubashir.a@gmail.com',
packages = find_packages(),
install_requires = get_req('requirements.txt')
)