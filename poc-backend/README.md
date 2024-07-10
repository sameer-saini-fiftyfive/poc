## POC Backend (Build with django)

- This is the backend for our POC frontend.

### Local setup

- Setup local virtual envirnoment by using `python -m venv venv` command. (`. ./venv/bin/activate` to activate and `deactivate` to deactivate)
- Install dependecies by running `make install`.
- To run the server use `make run` command, this will also migrate the models before running the project so no need to migrate separately before running the project.
- The backend can be accessed on http://localhost:8000 if the port is not defined specifically other than 8000.
