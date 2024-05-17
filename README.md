# Build a Login Application using Vue3 & Python Flask

Build a login and register application using Vue 3, and Flask mainly. The frontend and backend can interact with each other via API requests/responses. Use MySQL database to save test user information.

## Prerequisites Environment

Here is the PC environment setup in order to setup the project locally.

| Packages/OS | Version          | Usage                                                  |
| ----------- | ---------------- | ------------------------------------------------------ |
| PC          | MacBook Air (M2) | -                                                      |
| macOS       | 14.1 (23B74)     | -                                                      |
| Docker      | 24.0.5           | Used to setup a `mysql` container for data persistance |
| Node        | v18.18.2         | Used for frontend                                      |
| NPM         | 9.8.1            | NPM package manager                                    |
| Python      | Python 3.11.9    | User for backend                                       |
| Pip         | pip 23.2.1       | Python package installer                               |
| [Pipenv][1] | 2023.6.12        | Python package management tool                         |

Below table shows the main frameworks/tools used in the project.

| Technical Stacks    | Tool/Framework | Link                                                                  |
| ------------------- | -------------- | --------------------------------------------------------------------- |
| Frontend Framework  | Vue 3.4.21     | <https://vuejs.org/guide/introduction.html>                           |
| Frontend Build Tool | Vite 5.2.0     | <https://vitejs.dev/guide/>                                           |
| Frontend UI         | Vuetify 3      | <https://vuetifyjs.com/en/getting-started/installation/#installation> |
| Backend Framework   | Flask 3.0      | <https://flask.palletsprojects.com/en/3.0.x/>                         |

## Get Started

### Database

In the project, to simplify the demo, we use Docker to create a `mysql` container in the local machine to save user data. Use below command to create a `mysql` container.

For more information, see <https://hub.docker.com/_/mysql>.

```bash
docker run --name local-mysql -e MYSQL_ROOT_PASSWORD=mysql123 -d mysql:tag
```

### Frontend

In the `vue-app` component, we use `npm` to manage frontend dependencies.

```bash
cd vue-app
# Install dependencies
npm install
# Start the server
npm run dev
```

The frontend server is running on <http://localhost:5173/>.

### Backend

In the `api` component, we use `pipenv` to manage backend dependencies.

```bash
cd api
# Create a virtualenv at the first time (one-time action)
pipenv install
# Activate virtualenv
pipenv shell
# Install dependencies in Pipfile
pipenv install
# Start server
flask run
```

The Flask server is running on <http://127.0.0.1:5000>.

## References

[1]: https://pipenv.pypa.io/en/latest/index.html
