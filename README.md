# Linear Regression model creation and deployment

Let's see how to create and deploy a linear regression model in python with the help of flask onto Heroku. For the sake of simplicity, we are going to use the heroku git method rather than creating a pipline to github or github actions.

## Thing to have upfront
- [python3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)  or [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- [git](https://git-scm.com/downloads)
- [heroku account](https://signup.heroku.com/)
- [heroku cli](https://devcenter.heroku.com/articles/heroku-cli)
- [jupter](https://jupyter.readthedocs.io/en/latest/install/notebook-classic.html) # optional

## Python packages
- flask
- gunicorn
- pandas
- scikit-learn

## Model creation
- Run either of [model_creator.py](https://github.com/gauthamp10/mldeploy/blob/master/src/model/model_creator.py) or [model_creator.ipynb](https://github.com/gauthamp10/mldeploy/blob/master/src/model/model_creator.ipynb) in[src/model](https://github.com/gauthamp10/mldeploy/tree/master/src/model) to create a model file

## Deployment
- Clone the repo
- Initialize the [/src](https://github.com/gauthamp10/mldeploy/blob/master/src) with git
- Add a [.gitignore](https://github.com/gauthamp10/mldeploy/edit/master/.gitignore) file
- Make a virtual environment
- Activate it
- Install necessary [packages](https://github.com/gauthamp10/mldeploy/blob/master/src/requirements.txt) 
- Login to your heroku account and authenticate with heroku cli
- Add the files, commit and push to cloud.

Voila!. You've just deployed a flask app onto the web.

## __Author__

 **Gautham Prakash**
 
  My other projects: [github.com/gauthamp10](https://github.com/gauthamp10)

  Website: [gauthamp10.github.io](https://gauthamp10.github.io)

  Blog: [gauthamp10/blog](https://gauthamp10.github.io/blog)

## __License__  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
