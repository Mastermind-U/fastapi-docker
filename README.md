# fastapi-docker

This is a template to create simple fastapi web apps.

It powered by traefik, both dev and prod.

To run code, just type:

```bash
docker-compose -f docker-compose.dev.yml up
```

The uvicorn will automatically update and restart after changes in files.

To manage dependencies, use [poetry](https://github.com/python-poetry/poetryhttps://) .

To add dependencies, just type

```bash
poetry add <dep_name>

# or

poetry add <dep_name> --dev
```

For manual installation and using in shell, use

```bash
poetry install
poetry shell
```

You can export requirements manually, using

```bash
poetry export -f requirements.txt --output requirements.txt
```

For adding enviroment variables, edit `.env` file. It's recommended to add this file to `.gitignore` to prevent leak of secret variables into repository. For big projects, use [vault](https://www.vaultproject.io/) and hvac library.

For VSCode users, select virtual enviroment created by poetry. Mypy and flake8 will be there.
