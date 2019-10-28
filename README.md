# myDiary-python
[![Build Status](https://travis-ci.com/andrewinsoul/myDiary-python.svg?branch=develop)](https://travis-ci.com/andrewinsoul/myDiary-python)
[![Coverage Status](https://coveralls.io/repos/github/andrewinsoul/myDiary-python/badge.svg?branch=develop)](https://coveralls.io/github/andrewinsoul/myDiary-python?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/bf604ed70bea26359416/maintainability)](https://codeclimate.com/github/andrewinsoul/myDiary-python/maintainability)



myDiary-python is a GraphQL API that allows user create diaries and stuff the diary with entries built with Python Django
<p align="center"> 
  <li><a href="#Technologies Used">Hosted Application</a></li>
  <li><a href="#Technologies Used">Technologies Used</a></li>
  <li><a href="#Installation">How to Use</a></li>
  <li><a href="#Tests">How to Test</a></li>
  <li><a href="#Coding Style">Code Style</a></li>
  <li><a href="#How to Contribute">How to Contribute</a></li>
  <li><a href="#Author">Meet me!</a></li>
  <li><a href="#License">License</a></li>
</p>


## Hosted Application
https://mydiary666-api.herokuapp.com/graphql/



## Technologies Used
- Python
- Django
- Graphene

## Installation

```bash
1. Git clone this repository `https://github.com/andrewinsoul/myDiary-python.git`
2. Change your directory `cd myDiary-python`
3. Create a virtual environment using the command `pipenv shell` 
3. Install all dependencies using `pipenv install`
4. Start the app by running `python manage.py runserver` for development
5. Navigate to `localhost:8000/graphql/` in your browser
6. Use the the GraphQL introspection feature to see the queries supported by the schema 
```
<b>NOTE:</b> 
- To exit from the virtual environment, simply type exit and to enter the virtual environment, run `pipenv shell`
- Ensure the HTTP Header `Authorization` is present with the token generated during the user authorization as value for every query that requires user to be authenticated 

## Tests

- Run test using `python manage.py test`


## How to Contribute

```bash
- Fork this repository.
- Clone it.
- Create your feature branch on your local machine with ```git checkout -b your-feature-branch```
- Push your changes to your remote branch with ```git push origin your-feature-branch```
- Open a pull request to the master branch, and describe how your feature works
````
Ensure your codes hasno linting issues flaged by pylint linter


## Author

- Andrew Okoye

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details
