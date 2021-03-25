# mune &middot; ![Production](https://pyheroku-badge.herokuapp.com/?app=mune-production) [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/h-richard/mune/main/main.py) [![Build Status](https://travis-ci.com/H-Richard/mune.svg?branch=main)](https://travis-ci.com/H-Richard/mune) [![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

Mune is an open source python web application built to analyze stocks, named after [Homma Munehisa](https://en.wikipedia.org/wiki/Homma_Munehisa). Currently, the forecasting component is powered by [Prophet](https://github.com/facebook/prophet), but this is subject to change.


## Contents
- [Development](#development)
- [Contributing](#contributing)
- [Deployment](#deployment)
- [Features](#features)
- [Backlog](#backlog)
- [Known Issues](#known-issues)

## Development

Currently, this project uses [pipenv](https://pypi.org/project/pipenv/) to manage dependencies, once installed run `pipenv install --dev` to install depdendencies. Then you can either run `pipenv shell` to activate the dev environment or run `pipenv run start` to start the app. Once the app is up and running, streamlit has an auto reload feature that makes development easy.

Learn more about streamlit [here](https://streamlit.io/)!

## Contributing

Feel free to open pull requests and raise new issues. 

All kinds of PRs are welcome, just make sure `pipenv run lint` passes :smile:. For high risk PRs, please make the base branch `staging` instead of `main`. 

## Deployment

Currently, `staging` and `main` are being auto deployed with heroku (only if travis is happy with the changes). See the **Environment** panel or click [here](https://github.com/H-Richard/mune/deployments) for the live instances as the urls are subject to change.

## Features

 - basic time series forecasting

## Backlog 

 - historical performance against indices
 - divident payout adjustments
 - warning against leveraged etfs
 - better caching
 - automated tests
 - improve chart performance
 - acquire massive amounts of wealth, then deploy to a better cloud server

## Known Issues
 - pipenv fails to install `fbprophet` the first time, retry always works
 - code sucks
 - pineapples don't belong on pizza
